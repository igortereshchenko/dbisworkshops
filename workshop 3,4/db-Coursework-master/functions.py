import cx_Oracle
from datafororacle import *

def getUsers(nick=None):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    if not nick:

        query = 'SELECT * FROM table(user_package.get_user())'
        cursor.execute(query)
    else:
        query = 'SELECT * FROM table(user_package.get_user(:nick))'
        cursor.execute(query, nick=nick)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

def is_user(user_nick, user_pass):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    count = cursor.callfunc("user_package.is_user", cx_Oracle.NATIVE_INT, [user_nick, user_pass])

    cursor.close()
    connection.close()

    return count

def add_user(u_nickname, u_login, u_pass, u_name, u_surname, u_faculty, u_course):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    result = cursor.callfunc("user_package.add_user", cx_Oracle.STRING, [u_nickname, u_login, u_pass, u_name, u_surname, u_faculty, u_course])
    cursor.close()
    connection.close()
    return result


def del_user(u_nickname):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    cursor.callproc("user_package.deluser", [u_nickname])
    cursor.close()
    connection.close()

def add_resourse(u_resourse):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    result = cursor.callfunc("resourse_package.add_resourse", cx_Oracle.STRING, [u_resourse])
    cursor.close()
    connection.close()
    return result

def del_resourse(u_resourse):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callproc("resourse_package.del_resourse", [u_resourse])
    cursor.close()
    connection.close()

def get_resourse(u_resourse=None):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    if not u_resourse:

        query = 'SELECT * FROM table(resourse_package.get_resourse())'
        cursor.execute(query)
    else:
        query = 'SELECT * FROM table(resourse_package.get_resourse(:u_resourse))'
        cursor.execute(query, u_resourse=u_resourse)

    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def update_resourse(new_resourse, old_resourse):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    result = cursor.callfunc("resourse_package.update_resourse", cx_Oracle.STRING, [new_resourse, old_resourse])
    cursor.close()
    connection.close()
    return result

def add_theme(u_theme):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    result = cursor.callfunc("lection_theme_package.add_theme", cx_Oracle.STRING, [u_theme])
    cursor.close()
    connection.close()
    return result

def del_theme(u_theme):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callproc("lection_theme_package.del_theme", [u_theme])
    cursor.close()
    connection.close()

def get_theme(u_theme=None):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    if not u_theme:

        query = 'SELECT * FROM table(lection_theme_package.get_lection_theme())'
        cursor.execute(query)
    else:
        query = 'SELECT * FROM table(lection_theme_package.get_lection_theme(:u_theme))'
        cursor.execute(query, u_theme=u_theme)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def update_theme(new_theme, old_theme):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    result = cursor.callfunc("lection_theme_package.update_theme", cx_Oracle.STRING, [new_theme, old_theme])
    cursor.close()
    connection.close()
    return result

def add_info(i_nickname, i_lec_name, i_resourse, i_link):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    result = cursor.callfunc("information_package.add_info",cx_Oracle.STRING, [i_nickname, i_lec_name, i_resourse, i_link])
    cursor.close()
    connection.close()
    return result

def del_info(i_nickname, i_id):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callproc("information_package.del_info", [i_nickname, i_id])
    cursor.close()
    connection.close()

def get_information(nick=None, theme=None):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    if (not nick) and (not theme):
        query = 'SELECT * FROM table(information_package.get_information(NULL, NULL))'
        cursor.execute(query)
    else:
        if not nick:
            query = 'SELECT * FROM table(information_package.get_information(NULL,:theme))'
            cursor.execute(query, theme=theme)
        elif not theme:
            query = 'SELECT * FROM table(information_package.get_information(:nick,NULL))'
            cursor.execute(query, nick=nick)
        else:
            query = 'SELECT * FROM table(information_package.get_information(:nick,:theme))'
            cursor.execute(query, theme=theme, nick=nick)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def add_UhT(u_nick,u_theme):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    result = cursor.callfunc("uht_package.add_uht", cx_Oracle.STRING, [u_nick, u_theme])
    cursor.close()
    connection.close()
    return result

def del_UhT(u_theme, u_nick):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callproc("uht_package.del_uht", [u_theme, u_nick])
    cursor.close()
    connection.close()


def update_UhT(new_theme, old_theme):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    result = cursor.callfunc("uht_package.update_uht", cx_Oracle.STRING, [new_theme, old_theme])
    cursor.close()
    connection.close()
    return result

def add_UhR(u_nick,u_resourse):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    result = cursor.callfunc("uhr_package.add_uhr", cx_Oracle.STRING, [u_nick, u_resourse])
    cursor.close()
    connection.close()
    return result

def del_UhR(u_resourse, u_nick):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    cursor.callproc("uhr_package.del_uhr", [u_resourse, u_nick])
    cursor.close()
    connection.close()


def update_UhR(new_resourse, old_resourse):
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()

    result = cursor.callfunc("uhr_package.update_uhr", cx_Oracle.STRING, [new_resourse, old_resourse])
    cursor.close()
    connection.close()
    return result

def get_res():
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    query = 'select information.resource_name, count(*) from information GROUP BY information.resource_name'
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def get_res_1():
    connection = cx_Oracle.connect(username, password, databaseName)
    cursor = connection.cursor()
    query = 'select COURSE_NUMBER, count(*) from "User" GROUP BY COURSE_NUMBER'
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result