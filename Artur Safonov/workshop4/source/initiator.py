from database_connection import engine
from sqlalchemy.orm import sessionmaker
from model import UserProfile, Card, Supply, WaterSupply, PowerSupply, GasSupply
from sqlalchemy import func

Session = sessionmaker(bind=engine)
session = Session()

bob = UserProfile(user_name='Bob', user_phone='+380123456789', user_email='bob@gmail.com')
boba  = UserProfile(user_name='Boba', user_phone='+380123456780', user_email='boba@gmail.com')

session.add(bob)
session.commit()
session.add(boba)
session.commit()

bob_id = (session.query(UserProfile).filter(UserProfile.user_phone == '+380123456789')[0]).user_id
boba_id = (session.query(UserProfile).filter(UserProfile.user_phone == '+380123456780')[0]).user_id

bobs_card = Card(user_id_fk = bob_id, card_number = '1234567890123456', card_name = 'Bob Bobovich', card_date = func.current_date(), card_ccv ='123')
bobas_card = Card(user_id_fk = boba_id, card_number = '0987654321098765', card_name = 'Boba Bobovna', card_date = func.current_date(), card_ccv ='777')
bobs_supply = Supply(user_id_fk = bob_id, water_supply_id = 123456, power_supply_id = 123, gas_supply_id = 5321123)
bobas_supply = Supply(user_id_fk = boba_id, water_supply_id = 654321, power_supply_id = 321, gas_supply_id = 3211235)

water1 = WaterSupply(water_supply_id = 123456, water_hot_previous = 1.1, water_hot_current=1.5)
power1 = PowerSupply(power_supply_id = 123, power_reading=11)
gas1 = GasSupply(gas_supply_id = 5321123, gas_reading=4)
water2 = WaterSupply(water_supply_id = 654321, water_cold_previous = 0.5, water_cold_current= 0.7)
power2 = PowerSupply(power_supply_id = 321, power_reading=6)
gas2 = GasSupply(gas_supply_id = 3211235, gas_reading=3)


instances = [bobs_card, bobs_supply, bobas_card, bobas_supply, water1, power1, gas1, water2, power2, gas2]
for ins in instances:
    session.add(ins)
    session.commit()

