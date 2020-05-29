CREATE OR REPLACE TRIGGER item_quantity
BEFORE INSERT ON wish_items_list
FOR EACH ROW
DECLARE
    item_quantity integer;
    new_item_id wish_items_list.ITEM_ID%TYPE := :new.ITEM_ID;
BEGIN
    SELECT count(ITEM_ID) INTO item_quantity FROM wish_items_list WHERE ITEM_ID = new_item_id;
    IF item_quantity > 200 THEN
        raise_application_error(-20001,'User can not add more then 200 items.');
    END IF;
END;


CREATE OR REPLACE TRIGGER item_price
BEFORE INSERT ON wish_items_list
FOR EACH ROW
DECLARE
    new_price integer := :new.item_price;
BEGIN
    IF new_price < 1 THEN
        raise_application_error(-20002,'The item price cannot be smaller than 1.');
    END IF;
END;


CREATE OR REPLACE TRIGGER item_price1
BEFORE INSERT ON purchased_items_list
FOR EACH ROW
DECLARE
    new_price integer := :new.item_price;
BEGIN
    IF new_price < 1 THEN
        raise_application_error(-20002,'The item price cannot be smaller than 1.');
    END IF;
END;
