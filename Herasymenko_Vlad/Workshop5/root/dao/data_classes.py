import cx_Oracle
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from root.dao.decrypt_credentials import Name, Pass, Path
from sqlalchemy.orm import relationship

connection = cx_Oracle.connect(Name, Pass, Path)
cursor = connection.cursor()


#39080209; 27/30
def get_filtred_year_date(year,v_ed_fk,mat_id):
    result = []
    message = 'Знайдено успішно'
    for mm in range(1,13):
        try:
            query = f"SELECT price FROM Prices_History WHERE v_ed_fk = {v_ed_fk} AND mat_id_fk = {mat_id} AND RECORD_MONTH = {mm} AND RECORD_YEAR = {year}"
            cursor.execute(query)
        except:
            query = f"SELECT price FROM Prices_History WHERE v_ed_fk = 39080209 AND mat_id_fk = 27 AND RECORD_MONTH = {mm} AND RECORD_YEAR = 2019"
            cursor.execute(query)
            message = "Нічого не знайдено"
        result.append(cursor.fetchall()[0][0])
    return result,message


engine = create_engine("oracle+cx_oracle://"+Name+":"+Pass+"@"+Path)
Base = declarative_base()

class User(Base):
    __tablename__ = "USERS_T"

    USER_ID = Column(Integer,primary_key = True, nullable = False)
    USER_LOGIN = Column(String(100), nullable = False)
    USER_EMAIL = Column(String(100), nullable = False)
    USER_PASS = Column(String(100), nullable = False)

    @classmethod
    def register_user(cls,login ,email ,pass1,pass2):

        for var in [login ,email ,pass1,pass2]:
            if var == '':
                var = None

        if pass1 == pass2:
            msg = cursor.var(cx_Oracle.STRING)
            cnt = cursor.var(cx_Oracle.NUMBER)
            cursor.callproc("registration_p.register_user", [login, email, pass1, pass2,cnt,msg])
            connection.commit()
            return msg.getvalue()
        else:
            return "Введені паролі не співпадають"


    @classmethod
    def perform_authorisation(cls,email_or_login, password):

        for var in [email_or_login, password]:
            if var == '':
                var = None

        user_id = cursor.callfunc("authorisation_p.authorisation", cx_Oracle.NUMBER, [email_or_login,password])
        return int(user_id)

    @classmethod
    def get_username(cls,user_id):

        if user_id == '':
            user_id = None

        if user_id == -1:
            return "Такого користувача не існує"
        user_name = cursor.callfunc("authorisation_p.get_username", cx_Oracle.STRING, [user_id])
        return user_name

    @classmethod
    def delete_user(cls,user_id):

        if user_id=='':
            user_id = None

        msg = cursor.var(cx_Oracle.STRING)
        if user_id == -1:
            return "Неможливо видалити неіснуючого користувача"
        cursor.callproc("authorisation_p.delete_user", [user_id,msg])
        connection.commit()
        return msg.getvalue()

    @classmethod
    def change_pass(cls,user_id, new_pass1,new_pass2):

        for var in [user_id, new_pass1,new_pass2]:
            if var == '':
                var = None

        msg = cursor.var(cx_Oracle.STRING)
        if user_id == -1:
            return "Потрібно авторизувтися, перш ніж змінювати пароль"
        cursor.callproc("authorisation_p.change_pass", [user_id,new_pass1,new_pass2,msg])
        connection.commit()
        return msg.getvalue()

    @classmethod
    def change_email(cls,user_id, new_email):

        for var in [user_id, new_email]:
            if var == '':
                var = None

        msg = cursor.var(cx_Oracle.STRING)
        if user_id == -1:
            return "Потрібно авторизувтися, перш ніж змінювати e-mail"
        cursor.callproc("authorisation_p.change_email", [user_id,new_email,msg])
        connection.commit()
        return msg.getvalue()


class Material(Base):
    __tablename__ = "MATERIALS_T"


    MATERIAL_NAME = Column(String(150), nullable = False)
    MATERIAL_ID = Column(Integer,primary_key = True, nullable = False)


    # Цей клас буде отримувати id з роута, який обробляє сторінку матеріалів. Але для тесту задамо його вручну
    def __init__(self, mat_id):
        self.mat_id = mat_id

    @classmethod
    def add_material(cls, name,description):

        if name == '':
            name = None

        msg = cursor.var(cx_Oracle.STRING)
        cnt = cursor.var(cx_Oracle.NUMBER)
        cursor.callproc("materials_p.add_material", [name,description,cnt,msg])
        connection.commit()
        return msg.getvalue()

    def delete_material(self):
        msg = cursor.var(cx_Oracle.STRING)
        cursor.callproc("materials_p.delete_material", [self.mat_id,msg])
        connection.commit()
        return msg.getvalue()

    def update_material(self, new_name):

        cnt1 = cursor.var(cx_Oracle.NUMBER)
        msg = cursor.var(cx_Oracle.STRING)
        cnt2 = cursor.var(cx_Oracle.NUMBER)
        cursor.callproc("materials_p.update_material", [self.mat_id,new_name,cnt1,msg,cnt2])
        connection.commit()
        return msg.getvalue()

    def update_material_description(self, new_description):

        cnt1 = cursor.var(cx_Oracle.NUMBER)
        msg = cursor.var(cx_Oracle.STRING)
        cnt2 = cursor.var(cx_Oracle.NUMBER)
        cursor.callproc("materials_p.update_material_description", [self.mat_id,new_description,cnt1,msg,cnt2])
        connection.commit()
        return msg.getvalue()

    @classmethod
    def find_material_id(cls, name_pattern):

        typeObj = connection.gettype("id_array")
        result = cursor.callfunc("materials_p.find_mat_id", typeObj, [name_pattern])
        if result.aslist() == []:
            print('Не знайдено матеріалів!')
        return result.aslist()

    @classmethod
    def find_vend_edrpou(cls, mat_id):

        typeObj = connection.gettype("id_array")
        result = cursor.callfunc("materials_p.find_vend_edrpou", typeObj, [mat_id])
        if result.aslist() == []:
            print('Не знайдено постачальників!')
        return result.aslist()

    @classmethod
    def get_mat_name(cls,mat_id):
        mat_name = cursor.var(cx_Oracle.STRING)
        result = cursor.callfunc("materials_p.get_mat_name", mat_name, [mat_id])
        return mat_name.getvalue()

    def get_mat_description(self):
        description = cursor.var(cx_Oracle.STRING)
        result = cursor.callfunc("materials_p.get_mat_description", description, [self.mat_id])
        return description.getvalue()

    def get_self_name(self):
        mat_name = cursor.var(cx_Oracle.STRING)
        result = cursor.callfunc("materials_p.get_mat_name", mat_name, [self.mat_id])
        return mat_name.getvalue()

    def get_vendors_price(self, edrpou):
        price = cursor.var(cx_Oracle.NUMBER)
        result = cursor.callfunc("materials_p.get_mat_price", price, [self.mat_id, edrpou])
        return price.getvalue()

    @classmethod
    def get_mat_price(cls, mat_id, edrpou):
        price = cursor.var(cx_Oracle.NUMBER)
        result = cursor.callfunc("materials_p.get_mat_price", price, [mat_id, edrpou])
        return price.getvalue()

    @classmethod
    def get_vendors_price_globally(cls, mat_id, edrpou):
        price = cursor.var(cx_Oracle.NUMBER)
        result = cursor.callfunc("materials_p.get_mat_price", price, [mat_id, edrpou])
        return price.getvalue()

class Vendors(Base):
    __tablename__ = "VENDORS_T"

    VEND_NAME = Column(String(150), nullable = False)
    VEND_EDRPOU = Column(Integer,primary_key = True, nullable = False)
    VEND_ADRESS = Column(String(200))
    VEND_CITY = Column(String(100), nullable = False)
    TELEPHONE = Column(String(20))
    MANAGER_NAME = Column(String(100))
    EMAIL = Column(String(320))


    # Цей клас буде отримувати edrpou з роута, який обробляє сторінку матеріалів. Але для тесту задамо його вручну
    def __init__(self, v_edrpou):
        self.v_edrpou = v_edrpou

    @classmethod
    def add_vendor(cls, v_name, v_edrpou, v_adress, v_city,v_tel, v_manager, v_email):

        msg = cursor.var(cx_Oracle.STRING)
        cnt = cursor.var(cx_Oracle.NUMBER)

        for var in [v_name, v_edrpou, v_adress, v_city,v_tel, v_manager, v_email]:
            if var == '':
                var = None

        cursor.callproc("vendors_p.add_vendor", [v_name, v_edrpou, v_adress, v_city,v_tel, v_manager, v_email,cnt,msg])
        connection.commit()

        return msg.getvalue()

    def delete_vendor(self):
        msg = cursor.var(cx_Oracle.STRING)
        cursor.callproc("vendors_p.delete_vendor", [self.v_edrpou,msg])
        connection.commit()

        return msg.getvalue()

    def update_vendor(self, new_name, new_adress, new_city, new_tel, new_manager, new_email):

        cnt1 = cursor.var(cx_Oracle.NUMBER)
        msg = cursor.var(cx_Oracle.STRING)
        cnt2 = cursor.var(cx_Oracle.NUMBER)

        for var in [new_name, new_adress, new_city, new_tel, new_manager, new_email]:
            if var == '':
                var = None

        cursor.callproc("vendors_p.update_vendor", [self.v_edrpou, new_name, new_adress, new_city, new_tel, new_manager, new_email,cnt1,msg,cnt2])
        connection.commit()
        return msg.getvalue()

    @classmethod
    def get_edrpou(cls, name_pattern):

        typeObj = connection.gettype("id_array")
        result = cursor.callfunc("vendors_p.get_edrpou", typeObj, [name_pattern])
        return result.aslist()

    @classmethod
    def get_products(cls, v_edrpou):

        typeObj = connection.gettype("id_array")
        result = cursor.callfunc("vendors_p.get_products", typeObj, [v_edrpou])
        return result.aslist()

    @classmethod
    def get_vend_name(cls,v_edrpou):
        vend_name = cursor.var(cx_Oracle.STRING)
        result = cursor.callfunc("vendors_p.get_vend_name", vend_name, [v_edrpou])
        return vend_name.getvalue()

    @classmethod
    def get_vend_city(cls, v_edrpou):
        vend_city = cursor.var(cx_Oracle.STRING)
        result = cursor.callfunc("vendors_p.get_vend_city", vend_city, [v_edrpou])
        return vend_city.getvalue()

    @classmethod
    def get_vend_adress(cls, v_edrpou):
        vend_adr = cursor.var(cx_Oracle.STRING)
        result = cursor.callfunc("vendors_p.get_vend_adress", vend_adr, [v_edrpou])
        return vend_adr.getvalue()

    @classmethod
    def get_vend_tel(cls, v_edrpou):
        vend_tel = cursor.var(cx_Oracle.STRING)
        result = cursor.callfunc("vendors_p.get_vend_tel", vend_tel, [v_edrpou])
        return vend_tel.getvalue()

    @classmethod
    def get_vend_email(cls, v_edrpou):
        vend_email = cursor.var(cx_Oracle.STRING)
        result = cursor.callfunc("vendors_p.get_vend_email", vend_email, [v_edrpou])
        return vend_email.getvalue()

    @classmethod
    def get_vend_m_name(cls, v_edrpou):
        vend_m_name = cursor.var(cx_Oracle.STRING)
        result = cursor.callfunc("vendors_p.get_vend_m_name", vend_m_name, [v_edrpou])
        return vend_m_name.getvalue()

class Bank(Base):
    __tablename__ = "BANK_T"

    VEND_BANK_NAME = Column(String(100), nullable = False)
    ROZ_RAH = Column(Integer, primary_key= True, nullable = False)
    MFO = Column(Integer, nullable = False)
    VEND_EDRPOU_FK = Column(Integer, nullable = False)

    #vendor = relationship("Vendors", back_populates="BANK_T")

    @classmethod
    def add_bank(cls,bank_name, bank_rah,bank_mfo,v_ed_fk):

        cnt1 = cursor.var(cx_Oracle.NUMBER)
        cnt2 = cursor.var(cx_Oracle.NUMBER)
        msg = cursor.var(cx_Oracle.STRING)

        for var in [bank_name, bank_rah,bank_mfo,v_ed_fk]:
            if var == '':
                var = None

        cursor.callproc("helper_tables_p.add_bank", [bank_name, bank_rah,bank_mfo,v_ed_fk,cnt1,cnt2,msg])
        connection.commit()

        return msg.getvalue()


    @classmethod # Цей метод поки що не працює коректно. Але до моменту здачі наступної лаби я його дороблю
    def update_bank(cls,new_bank_name, new_bank_rah,new_bank_mfo,v_ed_fk):

        cnt1 = cursor.var(cx_Oracle.NUMBER)
        cnt2 = cursor.var(cx_Oracle.NUMBER)
        msg = cursor.var(cx_Oracle.STRING)

        for var in [new_bank_name, new_bank_rah,new_bank_mfo,v_ed_fk]:
            if var == '':
                var = None

        cursor.callproc("helper_tables_p.update_bank", [new_bank_name, new_bank_rah,new_bank_mfo,v_ed_fk,cnt1,cnt2,msg])
        connection.commit()

        return msg.getvalue()


    @classmethod
    def delete_bank(cls, v_ed_fk):

        if v_ed_fk == '':
            v_ed_fk = None

        msg = cursor.var(cx_Oracle.STRING)
        cursor.callproc("helper_tables_p.delete_bank", [v_ed_fk,msg])
        connection.commit()

        return msg.getvalue()

    @classmethod
    def get_bank_roz_rah(cls, v_ed):
        bank_roz_rah = cursor.var(cx_Oracle.NUMBER)
        try:
            result = cursor.callfunc("helper_tables_p.get_bank_roz_rah", bank_roz_rah, [v_ed])
            return int(bank_roz_rah.getvalue())
        except:
            return "Не знайдено банківського запису"


class Vendor_Material(Base):
    __tablename__ = "VEND_MAT_T"

    MATERIAL_ID_FK = Column(Integer, primary_key= True, nullable = False)
    VEND_EDRPOU_FK = Column(Integer, primary_key= True, nullable = False)

    #vendor = relationship("Vendors", back_populates="VEND_MAT_T")
    #material = relationship("Material", back_populates="VEND_MAT_T")

    @classmethod
    def add_vend_mat(cls,mat_id_fk,v_ed_fk,price):

        cnt = cursor.var(cx_Oracle.NUMBER)
        msg = cursor.var(cx_Oracle.STRING)

        cursor.callproc("helper_tables_p.add_vend_mat", [mat_id_fk,v_ed_fk,price,cnt,msg])
        connection.commit()

        return msg.getvalue()

    @classmethod
    def update_vend_mat(cls,new_mat_id_fk,v_ed_fk,new_price):

        cnt = cursor.var(cx_Oracle.NUMBER)
        msg = cursor.var(cx_Oracle.STRING)

        cursor.callproc("helper_tables_p.update_vend_mat", [new_mat_id_fk,v_ed_fk,new_price,cnt,msg])
        connection.commit()

        return msg.getvalue()

    @classmethod
    def delete_vend_mat(cls,mat_id, v_ed_fk):
        msg = cursor.var(cx_Oracle.STRING)

        cursor.callproc("helper_tables_p.delete_vend_mat", [mat_id,v_ed_fk,msg])
        connection.commit()

        return msg.getvalue()

    @classmethod
    def get_bank_name(cls, v_ed_fk):
        bank_name = cursor.var(cx_Oracle.STRING)

        result = cursor.callfunc("helper_tables_p.get_bank_name", bank_name, [v_ed_fk])
        connection.commit()

        return bank_name.getvalue()

    @classmethod
    def get_bank_mfo(cls, v_ed_fk):
        mfo = cursor.var(cx_Oracle.NUMBER)

        try:
            result = cursor.callfunc("helper_tables_p.get_bank_mfo", mfo, [v_ed_fk])
            connection.commit()
            return mfo.getvalue()
        except:
            return 'Інформації не знайдено'

"""

if __name__ == '__main__':
    # ТЕСТ (так, не юніт-тест, зате працює)

    # Некоректні дані
    user_message = User.register_user('Tester_2','my_testemail','15','12345')
    print(user_message)
    incorrect_user_id = User.perform_authorisation('Tester_2','12345')
    print('Неправильне id=',incorrect_user_id)

    # Коректні дані
    user_message = User.register_user('Tester_1337','my_test@email','12345','12345')
    print(user_message)

    correct_user_id = User.perform_authorisation('Tester_1337','12345')
    print('Правильне id=',correct_user_id)

    user_name = User.get_username(correct_user_id)
    print('Користувач з логіном:',user_name,' увійшов')

    user_message = User.change_email(correct_user_id,'123_incorect_email')
    print(user_message)
    user_message = User.change_email(correct_user_id,'123@corect_email')
    print(user_message)

    user_message = User.change_pass(correct_user_id,'1','1')
    print(user_message)
    user_message = User.change_pass(correct_user_id,'54321','54321')
    print(user_message)

    user_message = User.delete_user(correct_user_id)
    print(user_message)

    print("Завершено тестування таблиці користувачів \n")
    material_message = Material.add_material('Test material')
    print(material_message)
    some_material_id = Material.find_material_id('Test material')[0]
    print('id матеріалу:',some_material_id)
    current_material_page = Material(some_material_id)

    material_message = current_material_page.update_material('Test2 material')
    print(material_message)
    material_message = current_material_page.update_material('New test material')
    print(material_message)

    material_message = current_material_page.delete_material()
    print(material_message)

    print("Завершено тестування таблиці матеріалів \n")

    vendor_message = Vendors.add_vendor('Test Company_invalid',1234,None,'Київ',None,None,None)
    print(vendor_message)
    vendor_message = Vendors.add_vendor('Test Company',12344321,'','Київ','','','')
    print(vendor_message)

    current_ed = Vendors.get_edrpou('Test Company')[0]
    print('ЄДРПОУ створеного постачальника:', current_ed)
    current_vendor_page = Vendors(current_ed)

    vendor_message = current_vendor_page.update_vendor('Cooler test name','','Львів',None,None,None)
    print(vendor_message)
    vendor_message = current_vendor_page.update_vendor('Cooler test name','','Київ',None,None,None)
    print(vendor_message)

    vendor_message = current_vendor_page.delete_vendor()
    print(vendor_message)
    print("Завершено тестування таблиці постачальників \n")



    bank_message = Bank.add_bank('New_Bank_invalid',1111,1,41115963)
    print(bank_message)
    bank_message = Bank.add_bank('New_Bank',11111111,111111,41115963)
    print(bank_message)

    bank_message = Bank.delete_bank(41115963)
    print(bank_message)


    print("Завершено тестування таблиці банків \n")


    material_message = Material.add_material('Test material')
    some_material_id = Material.find_material_id('Test material')[0]

    material_message2 = Material.add_material('Test material_new')
    new_mat = Material.find_material_id('Test material')[0]

    vendor_message = Vendors.add_vendor('Test Company',12344321,'','Київ','','','')
    current_ed = Vendors.get_edrpou('Test Company')[0]

    vend_mat_message = Vendor_Material.add_vend_mat(some_material_id,current_ed)
    print(vend_mat_message)

    vend_mat_message = Vendor_Material.update_vend_mat(new_mat,current_ed)
    print(vend_mat_message)

    vend_mat_message = Vendor_Material.delete_vend_mat(current_ed)
    print(vend_mat_message)

    print('\n Завершено тестування')
    Base.metadata.create_all(engine)
    
"""