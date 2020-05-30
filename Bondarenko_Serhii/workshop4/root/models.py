import cx_Oracle
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Date, MetaData, ForeignKey
from sqlalchemy.sql.functions import *
from sqlalchemy.orm import relationship

ip = 'SERHII'
port = 1521
ser_name = 'cochalka'
dsn = cx_Oracle.makedsn(ip, port, service_name=ser_name)
oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

engine = create_engine(
    oracle_connection_string.format(

        username="TEST",
        password="240580",
        sid="cochalka",
        host="SERHII",
        port="1521",

    )
    , echo=True
)

connection = cx_Oracle.connect('TEST', '240580', dsn)
cursor = connection.cursor()

# engine = create_engine("oracle+cx_oracle://" + 'TEST' + ":" + '240580' + "@" + databaseName)

Base = declarative_base()


class User(Base):
    __tablename__ = 'USERS_T'
    user_id = Column(Integer, primary_key=True, nullable=False)
    user_name = Column(String(100), unique=True)
    full_name = Column(String(100), nullable=False)
    sex = Column(String(1), nullable=False)
    birthday = Column(Date, nullable=False, default=current_date)
    profile_photo = Column(String(255), nullable=False)
    profile_status = Column(String(1), nullable=False, default='N')
    friendly = Column(String(1), nullable=False, default='N')
    membership = relationship('Membership', uselist=False, back_populates="User")

    @classmethod
    def register_user(cls, u_name, f_name, u_sex, u_birtday, u_photo, u_friend):
        for var in [u_name, f_name, u_sex, u_birtday, u_photo, u_friend]:
            if var == '':
                var = None
        if int(current_date - datetime.strptime(u_birtday, '%m/%d/%y')) >= 18:
            sts = cursor.var(cx_Oracle.STRING)
            cnt = cursor.var(cx_Oracle.NUMBER)
            cursor.callproc("registration_p.register_user",
                            [u_name, f_name, u_sex, u_birtday, u_photo, u_friend, cnt, sts])
            connection.commit()
            return sts.getvalue()
        else:
            return "Користувач повининний бути повнолітнім"

    @classmethod
    def get_user_id(cls, u_name):
        if u_name == '':
            u_name = None
        user_id = cursor.callfunc("user_configurations_p.get_user_id", cx_Oracle.NUMBER, u_name)
        return int(user_id)

    @classmethod
    def delete_user(cls, u_name):
        if u_name == '':
            u_name = None
        sts = cursor.var(cx_Oracle.STRING)
        cursor.callproc("user_configurations_p.delete_user", [u_name, sts])
        connection.commit()
        return sts.getvalue()

    @classmethod
    def edit_user(cls, u_name, f_name, u_photo):
        for var in [u_name, f_name, u_photo]:
            if var == '':
                var = None
        sts = cursor.var(cx_Oracle.STRING)
        cursor.callproc("user_configurations_p.edit_user", [u_name, f_name, u_photo, sts])
        connection.commit()
        return sts.getvalue()

    @classmethod
    def change_profile_status(cls, u_name, u_profile):
        for var in [u_name, u_profile]:
            if var == '':
                var = None
        sts = cursor.var(cx_Oracle.STRING)
        cursor.callproc("user_configurations_p.change_profile_status", [u_name, u_profile, sts])
        connection.commit()


class Membership(Base):
    __tablename__ = 'MEMBERSHIPS'
    membsh_id = Column(Integer, primary_key=True, nullable=False)
    user_name = Column(String(100), ForeignKey('user_name'), unique=True, default=User.user_name)
    reg_date = Column(Date, nullable=False, default=current_date)
    qr_code = Column(String(255), nullable=False)
    memb_rank = Column(String(1), nullable=False)
    user = relationship("User", back_populates="Membership")

    @classmethod
    def create_membership(cls, m_name, m_qode, m_rank):
        for var in [m_name, m_qode, m_rank]:
            if var == '':
                var = None

        sts = cursor.var(cx_Oracle.STRING)
        cnt = cursor.var(cx_Oracle.NUMBER)
        cursor.callproc("create_membership_p.create_membership",
                        [m_name, m_qode, m_rank, cnt, sts])
        connection.commit()
        return sts.getvalue()

    @classmethod
    def get_membsh_id(cls, m_name):
        if m_name == '':
            m_name = None
        membsh_id = cursor.callfunc("membership_configurations_p.get_membsh_id", cx_Oracle.NUMBER, m_name)
        return int(membsh_id)

    @classmethod
    def delete_membership(cls, m_name):
        if m_name == '':
            m_name = None
        sts = cursor.var(cx_Oracle.STRING)
        cursor.callproc("membership_configurations_p.delete_membership", [m_name, sts])
        connection.commit()
        return sts.getvalue()

    @classmethod
    def check_and_del(cls, m_name, m_rank, m_rdate):
        for var in [m_name, m_rank, m_rdate]:
            if var == '':
                var = None
        sts = cursor.var(cx_Oracle.STRING)
        ch_date = current_date
        cursor.callproc("membership_configurations_p.check_and_del", [m_name, m_rank, m_rdate, sts, ch_date])
        connection.commit()
        return sts.getvalue()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    user_bob = User.register_user(u_name='Bob', f_name='Bobenko Bob Bobovich', u_sex='M', u_birtday='2000/03/14',
                                  u_photo='maybe another time', u_friend='no one')
    print(user_bob)
