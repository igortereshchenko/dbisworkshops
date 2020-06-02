from app import db


class Students(db.Model):
    __tablename__ = 'Students'

    stud_id_phone = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, db.CheckConstraint(
        'email LIKE ^([a-zA-Z0-9\\-]+\\.)*[a-zA-Z0-9_\\-]+@([a-zA-Z0-9_\\-]+\\.)+(com|org|edu|net|ca|au|coop|de|ee|es|fm|fr|gr|ie|in|it|jp|me|nl|nu|ru|uk|us|za)$'))
	age = db.Column(db.Integer, db.CheckConstraint('age>0.0', 'age<100.0', name='check_age'))
    stud_registers = db.relationship('Registers', backref='regist_stud')



    def __init__(self, stud_id_phone, name, email):
        self.stud_id_phone = stud_id_phone
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.stud_id_phone


class Groups(db.Model):
    __tablename__ = 'groups'

	group_name = db.Column(db.String(200), primary_key=True)
    level = db.Column(db.String(100), nullable=False)
    timetable = db.Column(db.String(200), nullable=False)
	teachers = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, db.CheckConstraint('price>0.0', name='check_price'))
    count_student = db.Column(db.Integer)

    ed_registers = db.relationship('Registers', backref='registers_ed')

    def __init__(self, group_name, level, timetable, teachers, price, count_student):
        self.group_name = group_name
        self.level = level
        self.timetable = timetable
		self.teachers = teachers
        self.price = price
        self.count_student = count_student

    def __repr__(self):
        return '<User %r>' % self.index



class Registers(db.Model):
    __tablename__ = 'Registers'

    id_regist = db.Column(db.String(50), primary_key=True)
    edGroup_name = db.Column(db.String(100), db.ForeignKey('groups.group_name'))
	edStud_name = db.Column(db.String(100), db.ForeignKey('student.student_name'))
    custId = db.Column(db.Integer, db.ForeignKey('customers.cust_id_phone'))
	studentcard = db.Column(db.String(100))
    register_date = db.Column(db.Date)
    price = db.Column(db.Integer, db.CheckConstraint('price>0.0', name='check_price'))


    def __init__(self, id_regist, edGroup_name, edStud_name, custId, studentcard, register_date, price):
        self.id_regist = id_regist
        self.edGroup_name = edGroup_name
        self.custId = custId
        self.edStud_name = edStud_name
        self.studentcard = studentcard
        self.register_date = register_date
        self.price = price

    def __repr__(self):
        return '<User %r>' % self.id_order


db.create_all()