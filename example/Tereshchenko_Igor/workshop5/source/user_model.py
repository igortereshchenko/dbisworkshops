from datetime import datetime

from root.source.ORM_relations import orm_users, db, orm_config, orm_actions


class user_model(object):

    @staticmethod
    def saveAction(user_id, action_type):
        orm_actions.add(user_id, action_type, datetime.now())
        return True


    @staticmethod
    def add(login, password):
        select = "SELECT * FROM users WHERE user_login = '{0}'".format(login)
        cursor = db.cursor.execute(select)
        results = cursor.fetchall()
        # check username
        if not results:
            user = orm_users.add(login, password, 0)
            orm_config.add(user.id, 400, 10, 10, 20, 5, 5, 5)
            return user
        else:
            return False

    @staticmethod
    def login(login, password):
        select = "SELECT * FROM users WHERE user_login = '{0}'".format(login)
        cursor = db.cursor.execute(select)
        results = cursor.fetchall()
        if results:
            select = "SELECT * FROM users WHERE user_login = '{0}' AND user_password = '{1}'".format(login, password)
            cursor = db.cursor.execute(select)
            results = cursor.fetchall()
            if results:
                return results
            else:
                return 'Неправильный пароль.'
        else:
            return 'Такого пользователя не существует.'

    @staticmethod
    def getConfig(user_id):
        select = "SELECT * FROM user_config WHERE user_id_fk = '{0}'".format(user_id)
        cursor = db.cursor.execute(select)
        results = cursor.fetchall()
        variables = dict()
        variables['balance'] = results[0][2]
        variables['profit_percent'] = results[0][3]
        variables['min_price'] = results[0][4]
        variables['max_price'] = results[0][5]
        variables['daily_sales'] = results[0][6]
        variables['balance_to_stop'] = results[0][7]
        variables['max_items_in_inventory'] = results[0][8]

        return variables

    @staticmethod
    def setConfig(user_id, profit_percent, min_price, max_price, sls_per_day, balance_to_stop, max_items_in_inventory):
        if not profit_percent or not min_price or not max_price or not sls_per_day or not balance_to_stop or not max_items_in_inventory:
            return "Заполните все поля."

        if not profit_percent.isdigit() or not min_price.isdigit() or not max_price.isdigit() or not sls_per_day.isdigit() or not balance_to_stop.isdigit() or not max_items_in_inventory.isdigit():
            return "Укажите значения правильно. Заполните все поля. Ставить 0 или буквы в поля запрещено."

        select = "SELECT count(*) FROM user_actions WHERE user_id_fk = '{0}' AND action_type = '{1}' AND action_date LIKE " \
                 "TO_DATE('{2}', 'YYYY MM DD')".format(user_id, 'filter_change', datetime.now().strftime("%Y-%m-%d"))
        cursor = db.cursor.execute(select)
        results = cursor.fetchall()
        if results[0][0] > 2:
            return "Менять настройки можно только 2 раза в сутки."

        if int(profit_percent) < 10:
            return "Процент профита не может быть меньше 10."

        if int(min_price) > int(max_price):
            return "Максимальная цена должна быть выше минимальной"

        else:
            update = """
                    UPDATE user_config 
                    SET profit_percent = '{0}',
                    min_price = '{1}',
                    max_price = '{2}',
                    daily_sales = '{3}',
                    balance_to_stop = '{4}',
                    max_items_in_inventory = '{5}'
                    WHERE user_id_fk = '{6}'
            """.format(profit_percent, min_price, max_price, sls_per_day, balance_to_stop, max_items_in_inventory,
                       user_id)
            # try:
            user_model.saveAction(user_id, 'filter_change')
            db.cursor.execute(update)
            db.connection.commit()
