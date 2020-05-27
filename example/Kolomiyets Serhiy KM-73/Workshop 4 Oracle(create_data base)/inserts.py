from models import *

db = OracleDb()

session = db.sqlalchemy_session

new_category = Category()
# new_category.add_category("test3", "test3_descr")
Category.get_all()

# print(session.query(Category).get(5).name)

new_product = Product()
# new_product.add_product(
#     name="Product1",
#     code=1,
#     price=2000,
#     description="product1_description",
#     color="yellow",
#     amount=2,
#     country="China",
#     material="Wood",
#     cat=1,
#     model="Kobein"
# )

new_product.add_product(
    name="Product2",
    code=2,
    price=4000,
    description="product2_description",
    color="yellow",
    amount=2,
    country="China",
    material="Wood",
    cat=1,
    model="Kobein"
)

# print(db.execute("select * from categories inner join products on categories.id = products.cat"))
# print(session.query(Product).get(1).name)

new_order = Order()
# new_order.add_order(
#     surname="KEK",
#     code=1,
#     phone="+380661258844",
#     email="order1@gmail.com",
#     amount=1,
#     city="Kiev",
#     street="Deribas"
# )

# new_order.add_order(
#     surname="KEK",
#     code=1,
#     phone="+380661258844",
#     email="order1gmail.com",
#     amount=1,
#     city="Kiev",
#     street="Deribas"
# )

# new_order.add_order(
#     surname="KEK",
#     code=1,
#     phone="380661258844",
#     email="order1@gmail.com",
#     amount=1,
#     city="Kiev",
#     street="Deribas"
# )
#
# print(db.execute("select name,price, phone, order_date from orders inner join products on orders.code = products.id"))
# print(session.query(Order).get(1).surname)


session.commit()
