create table dishes(
	dish_id integer not null,
	dish_name varchar2() not null,
	dish_price float not null,
	dish_describe varchar2() not null,

	constraint dishes_pk primary key (dish_id) 

);

create table orders(
	order_id integer not null,
	dish_id integer not null,
	user_phone varchar2 not null,
	user_name integer not null,
	amount_dishes integer not null

	constraint dishes_pk primary key (order_id)
);
