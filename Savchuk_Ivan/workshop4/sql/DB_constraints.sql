/*
    This block contains constraint creation,
    such as FOREIGN KEYs, CHECKs etc.
*/
ALTER TABLE orders
ADD CONSTRAINT check_orders_price
CHECK (price > 0);

ALTER TABLE snack
ADD CONSTRAINT check_snack_price
CHECK (price > 0);

ALTER TABLE ticket
ADD CONSTRAINT check_ticket_price
CHECK (price > 0);

ALTER TABLE comments
ADD CONSTRAINT check_comment_rate
CHECK (film_rate > 0);

ALTER TABLE app_user
ADD CONSTRAINT check_user_num
CHECK (orders_num > 0);

ALTER TABLE films
ADD CONSTRAINT check_film_num
CHECK (orders_num > 0);

ALTER TABLE cinema
ADD CONSTRAINT check_cinema_num
CHECK (orders_num > 0);

ALTER TABLE snack
ADD CONSTRAINT check_snack_num
CHECK (orders_num > 0);
/*
    ENDBLOCK
*/