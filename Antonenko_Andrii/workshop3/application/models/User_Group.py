from .. import db


Role_Enum = ('owner', 'participant', 'guest')


class User_Group(db.Model):

    __tablename__ = 'User_Group'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)
    role = db.Column(db.Enum(*Role_Enum, name='role_name_enum'))
