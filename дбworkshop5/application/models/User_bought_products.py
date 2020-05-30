from .. import db


class User_bought_products(db.Model):


    __tablename__ = 'user_bought_products'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(32), index=False, unique=True, nullable=False)
    first_name = db.Column(db.String(32), index=False, unique=False, nullable=False)
    last_name = db.Column(db.String(32), index=False, unique=False, nullable=False)

    def __repr__(self):
        return '<User_bought_products {}>'.format(self.last_name)
