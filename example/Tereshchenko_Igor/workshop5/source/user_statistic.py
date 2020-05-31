from root.source.ORM_relations import db


class user_statistic(object):
    @staticmethod
    def getUserPurchases(user_id):
        select = "SELECT count(*) FROM user_items WHERE user_id_fk = '{0}'".format(user_id)
        cursor = db.cursor.execute(select)
        results = cursor.fetchall()[0][0]
        return results

    @staticmethod
    def getAllPurchases():
        select = "SELECT count(*) FROM user_items"
        cursor = db.cursor.execute(select)
        results = cursor.fetchall()[0][0]
        return results

    @staticmethod
    def percentOfSimilarityConfigs(user_id):
        select = "SELECT count(*) FROM user_config"
        cursor = db.cursor.execute(select)
        configs_count = cursor.fetchall()[0][0]

        similarity_array = []

        z = ['profit_percent', 'min_price', 'max_price', 'daily_sales', 'balance_to_stop']
        for item in z:
            select = "SELECT count(*) FROM user_config WHERE {0} = (SELECT {0} FROM user_config where user_id_fk = {1})".format(item, user_id)
            cursor = db.cursor.execute(select)
            user_config = cursor.fetchall()[0][0]
            similarity_array.append(user_config)

        similarity = 0
        for item in similarity_array:
            similarity += item / configs_count * 100

        similarity = similarity / len(similarity_array)

        return round(similarity, 2)

    @staticmethod
    def getUserCount():
        select = "SELECT count(*) FROM users"
        cursor = db.cursor.execute(select)
        count_users = cursor.fetchall()[0][0]
        return count_users