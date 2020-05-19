from .. import db


class Group(db.Model):
    """Data model for Group."""

    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=False, unique=True, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    users = db.relationship('User', secondary='group_user', backref=db.backref('user'))

    def __repr__(self):
        return '<Group {}>'.format(self.name)
