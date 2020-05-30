import cx_Oracle

from db import OracleDb 

db_oracle = OracleDb()

def new_dish(dish_name, dish_price, dish_describe):

    dish_id = db_oracle.cursor.var(cx_Oracle.NATIVE_INT)
    status = db_oracle.cursor.var(cx_Oracle.STRING)

    db_oracle.cursor.callproc("orders_pkg.new_order", [
                                                        dish_id, 
                                                        status,
                                                        dish_name,
                                                        dish_price,
                                                        dish_describe
                                                        ] )
    db_oracle.cursor.close()
    db_oracle.connection.close()

    return dish_id.getvalue(), status.getvalue()


def new_order(dish_id, user_phone, user_name, amount_dishes):

    order_id = db_oracle.cursor.var(cx_Oracle.NATIVE_INT)
    status = db_oracle.cursor.var(cx_Oracle.STRING)

    db_oracle.cursor.callproc("orders_pkg.new_order", [
                                                        order_id, 
                                                        status,
                                                        dish_id,
				                                        user_phone,
                                                        user_name,
                                                        amount_dishes
                                                        ])
    db_oracle.cursor.close()
    db_oracle.connection.close()

    return order_id.getvalue(), status.getvalue()


def get_all_dishes():
    query = 'select * from dishes;'
    dishes = db_oracle.cursor.execute(query)
    return dishes