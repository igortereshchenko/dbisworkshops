from main import db


class app_user(db.Model):
    __tablename__ = 'app_user'
    user_id =db.Column(db.Integer,primary_key=True)
    user_name =db.Column(db.String(50), nullable=False)
    user_surname =db.Column(db.String(50), nullable=False)
    @classmethod
    def add_member(self, name, surname, status, new_id=None):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_member = app_user(user_id=new_id,
                            user_name=name,
                            user_surname=surname
        session.member(new_user)
        session.commit()

class series(db.Model):
    __tablename__ = 'series'
    series_id = db.Column(db.Integer, primary_key=True)
    series_title = db.Column(db.String(30), nullable=False)
    series_genre = db.Column(db.String(30), nullable=False)
    series_year = db.Column(db.String(30), nullable=False)
    series_grade = db.Column(db.String(30), nullable=False)
    @classmethod
    def add_series(self, title, genre, year, grade, new_id=None):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_series = series(series_id=new_id,
                            series_title=title,
                            series_genre=genre,
                            series_year=year,
                            series_grade=grade
                            )
        session.add(new_series)
        session.commit()
     