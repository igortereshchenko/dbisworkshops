alter table orders 
add constraint order_dish_fk foreign key (dish_id)
				references dishes(dish_id);

alter table dishes
add constraint check_price check dish_price > 0;

alter table orders 
add constraint check_amount check amount_dishes > 0;