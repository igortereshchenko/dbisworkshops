from .. import db


class Product(db.Model):


    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=False, unique=False, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    price = db.Column(db.Integer, index=False, unique=False,nullable=False)

    def __repr__(self):
        return '<Product {}>'.format(self.name)
