from root.source.ORM_relations import db
from root.source.user_model import user_model


class payments_model(object):


    @staticmethod
    def getBalance(user_id):
        select = "SELECT balance FROM user_config WHERE user_id_fk = '{0}'".format(user_id)
        cursor = db.cursor.execute(select)
        results = cursor.fetchall()
        return results[0][0]

    @staticmethod
    def setBalance(user_id, balance):
        update = "Update user_config SET balance = '{0}' WHERE user_id_fk = '{1}'".format(balance, user_id)
        db.cursor.execute(update)
        db.connection.commit()

    @staticmethod
    def withdrawBalance(user_id, summary):
        if not summary.isdigit():
            return 'Введите сумму число.'

        select = "SELECT balance FROM user_config WHERE user_id_fk = '{0}'".format(user_id)
        cursor = db.cursor.execute(select)
        results = cursor.fetchall()

        if int(results[0][0]) < int(summary):
            return 'Введите сумму корректно.'

        elif int(results[0][0]) - int(summary) < 5:
            return 'На балансе должно остаться больше 5$'

        else:
            balance = int(results[0][0]) - int(summary)
            update = "Update user_config SET balance = '{0}' WHERE user_id_fk = '{1}'".format(balance, user_id)
            user_model.saveAction(user_id, 'withdraw')
            db.cursor.execute(update)
            db.connection.commit()
            return True