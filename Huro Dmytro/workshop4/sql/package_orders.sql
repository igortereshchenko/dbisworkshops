create or replace package orders_pkg is

	procedure new_order(
		
		ord_id out integer,
		status out varchar2,
		
		dish_id in orders.dish_id%type,
		user_phone in orders.user_phone%type,
		user_name in orders.user_name%type,
		amount_dishes in orders.amount_dishes%type

);

end orders_pkg;

create or replace package body orders_pkg is
    procedure new_order(
        
        ord_id out integer,
		status out varchar2,
		
		dish_id in orders.dish_id%type,
		user_phone in orders.user_phone%type,
		user_name in orders.user_name%type,
		amount_dishes in orders.amount_dishes%type
	
	) is
	begin
	BEGIN
	insert into orders(order_id, dish_id, user_phone,
					   user_name, amount_dishes) 
		values(seq_student.nextval,dish_id, user_phone,
				user_name, amount_dishes)
	returning order_id into ord_id;

	commit;
	status:='ok';
	exception
		when dup_val_on_index then
			status:='student already exist';
		when others then
			status:=sqlerrm;
	END;

	end new_order;


end orders_pkg;
