from root.source.ORM_relations import orm_items
from root.source.payments_model import payments_model


class items_model(object):

    @staticmethod
    def buyItem(user_id, name, price, action):
        orm_items.add(user_id, name, price, action)

    @staticmethod
    def checkItems(user_id, config, guns):
        items = []

        balance = int(config['balance'])
        profin_percent = int(config['profit_percent'])
        min_price = int(config['min_price'])
        max_price = int(config['max_price'])
        daily_sales = int(config['daily_sales'])
        balance_to_stop = int(config['balance_to_stop'])
        for gun in guns:
            if int(gun['daily_sales']) >= daily_sales:
                if min_price <= int(gun['gun_price']) and max_price >= int(gun['gun_price']):
                    if balance_to_stop <= balance - int(gun['gun_price']):
                        profit = ( int(gun['gun_average_price']) - int(gun['gun_price']) ) / int(gun['gun_average_price']) * 100
                        if profit >= profin_percent:
                            balance = balance - int(gun['gun_price'])
                            items_model.buyItem(user_id, gun['gun_name'], gun['gun_price'], 'bought')
                            items.append(gun)
                            payments_model.setBalance(user_id, balance)
                    else:
                        break

        return items

