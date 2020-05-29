/*
    This block contains constraint creation,
    such as FOREIGN KEYs, CHECKs etc.
*/

set transaction isolation level read committed;

ALTER TABLE orders
ADD CONSTRAINT check_orders_price
CHECK (price > 0);

ALTER TABLE snack
ADD CONSTRAINT check_snack_price
CHECK (price > 0);

ALTER TABLE cinema
ADD CONSTRAINT check_cinema_num
CHECK (orders_num > 0);

ALTER TABLE snack
ADD CONSTRAINT check_snack_num
CHECK (orders_num > 0);

/*
    ENDBLOCK
*/