from .. import db


class User(db.Model):


    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), index=False, unique=False, nullable=False)
    last_name = db.Column(db.String(32), index=False, unique=False, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.email)

