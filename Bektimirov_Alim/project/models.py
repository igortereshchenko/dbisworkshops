from app import db



class Bot_user(db.Model):
    __tablename__ = 'bot_user'
    user_id =db.Column(db.Integer,primary_key=True)
    user_name =db.Column(db.String(30), nullable=False)
    first_name =db.Column(db.String(30), nullable=False)
    last_name =db.Column(db.String(30), nullable=True)
    liked_films = db.relationship('Liked_film_list', secondary='liked_users')
    expec_films = db.relationship('Expected_film_list', secondary='expected_users')
    @classmethod
    def add(self, user_id, user_name, first_name, last_name):
        session = db.session
        if session.query(self).filter_by(user_id=user_id).first():
            pass
        else:
            new_user = Bot_user(
                user_id=user_id,
                user_name=user_name,
                first_name=first_name,
                last_name=last_name,
            )
            session.add(new_user)
            session.commit()

class Liked_film_list(db.Model):
    __tablename__ = 'liked_film_list'
    film_id =db.Column(db.Integer, primary_key=True)
    film_name =db.Column(db.String(30), nullable=False)
    genre =db.Column(db.Integer, nullable=False)
    release_date =db.Column(db.Integer, nullable=False)
    rating =db.Column(db.Float(precision=1), nullable=False)
    user = db.relationship('Bot_user', secondary='liked_users')
    @classmethod
    def add(self, film_id, film_name, genre, release_date, rating):
        session = db.session
        if session.query(self).filter_by(film_id=film_id).first():
            pass
        else:
            new_film = Liked_film_list(
                film_id=film_id,
                film_name=film_name,
                genre=genre,
                release_date=release_date,
                rating=rating,
            )
            session.add(new_film)
            session.commit()

class Expected_film_list(db.Model):
    __tablename__ = 'expected_film_list'
    film_id =db.Column(db.Integer, primary_key=True)
    film_name =db.Column(db.String(30))
    genre =db.Column(db.Integer, nullable=False)
    release_date =db.Column(db.Integer, nullable=False)
    rating =db.Column(db.Float(precision=1), nullable=False)
    user = db.relationship('Bot_user', secondary='expected_users')
    @classmethod
    def add(self, film_id, film_name, genre, release_date, rating):
        session = db.session
        new_film = Expected_film_list(
            film_id=film_id,
            film_name=film_name,
            genre=genre,
            release_date=release_date,
            rating=rating,
        )
        session.add(new_film)
        session.commit()


class Liked_users(db.Model):
    __tablename__ = 'liked_users'
    film_id =db.Column(db.Integer,db.ForeignKey('liked_film_list.film_id'), primary_key=True)
    user_id =db.Column(db.Integer,db.ForeignKey('bot_user.user_id'), primary_key=True)
    @classmethod
    def add(self, film_id, user_id):
        session = db.session
        if bool(session.query(self).filter(db.and_(self.film_id == film_id, self.user_id == user_id)).first()):
            print(session.query(self).filter(db.and_(self.film_id == film_id, self.user_id == user_id)).first())
            pass
        else:
            print(session.query(self).filter(db.and_(self.film_id == film_id, self.user_id == user_id)).first())
            new_film = Liked_users(
                film_id=film_id,
                user_id=user_id
            )
            session.add(new_film)
            session.commit()

class Expec_users(db.Model):
    __tablename__ = 'expected_users'
    film_id =db.Column(db.Integer,db.ForeignKey('expected_film_list.film_id'), primary_key=True)
    user_id =db.Column(db.Integer,db.ForeignKey('bot_user.user_id'), primary_key=True)