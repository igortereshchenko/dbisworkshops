create or replace package dishes_pkg is

	procedure new_dish(
		
		di_id out integer,
		status out varchar2,
		
		dish_name in dishes.dish_id%type,
		dish_price in dishes.dish_price%type,
		dish_describe in dishes.dish_describe%type

);

end dishes_pkg;

create or replace package body dishes_pkg is
    procedure new_dish(
       
        di_id out integer,
		status out varchar2,
		
		dish_name in dishes.dish_id%type,
		dish_price in dishes.dish_price%type,
		dish_describe in dishes.dish_describe%type

	) is
	begin
	BEGIN
	insert into dishes(dish_id, dish_name, dish_price, dish_describe) 
		values(seq_dishes.nextval, dish_name, dish_price, dish_describe)
	returning dish_id into di_id;

	commit;
	status:='ok';
	exception
		when dup_val_on_index then
			status:='recom already exist';
		when others then
			status:=sqlerrm;
	END;

	end new_dish;


end dishes_pkg;
