from json import dumps

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from config import DB_URL_PATH
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine(DB_URL_PATH)
Base = declarative_base()

session = scoped_session(sessionmaker())
session.configure(bind=engine)
Base.query = session.query_property()


# Table objects and their associated schema constructs
class AppBase(Base):
    __abstract__ = True
    __table_args__ = {'extend_existing': True}
    convention = {
        "ix": 'ix_%(column_0_label)s',
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(column_0_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    }
    metadata = MetaData(naming_convention=convention)


# Main methods
class DbTools(object):

    session = session

    @classmethod
    def get_by_id(cls, id):
        return cls.session.query(cls).filter(cls.id == id).first()

    @classmethod
    def get_last_item(cls):
        return cls.session.query(cls).order_by(cls.id.desc()).first()

    @classmethod
    def find(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def find_all(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()

    @classmethod
    def get_all(cls):
        return cls.session.query(cls).all()

    @classmethod
    def delete_all(cls):
        cls.session.query(cls).delete()
        cls.session.commit()

    @classmethod
    def create(cls, **kwargs):
        obj = None
        try:
            instance = cls(**kwargs)
            obj = instance.save()
        except Exception as e:
            print(e.args)
            cls.session.rollback()
        return obj

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        self.session.add(self)
        if commit:
            self.session.commit()
        return self

    def delete(self, commit=True):
        self.session.delete(self)
        return commit and self.session.commit()

    @classmethod
    def query(cls):
        return cls.session.query(cls)

    @classmethod
    def query_distinct_in_column(cls, cls_column):
        return cls.session.query(cls).distinct(getattr(cls, cls_column))

    def __repr__(self):
        return "<{}(id={})>".format(self.__class__.__name__, self.id)

    def __str__(self):
        return self.__repr__()

    def to_json(self):
        """ Returns a JSON representation of an SQLAlchemy-backed object.
        """
        json = {}
        for col in self._sa_class_manager.mapper.mapped_table.columns:
            json[col.name] = getattr(self, col.name)

        return dumps([json])
