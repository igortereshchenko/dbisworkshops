/*
    This block contains constraint creation,
    such as FOREIGN KEYs, CHECKs etc.
*/
ALTER TABLE orders
ADD CONSTRAINT check_orders_price
CHECK (price > 0);

ALTER TABLE comments
ADD CONSTRAINT check_comment_rate
CHECK (film_rate > 0);

ALTER TABLE app_user
ADD CONSTRAINT check_user_num
CHECK (orders_num > 0);

ALTER TABLE dish
ADD CONSTRAINT check_dish_num
CHECK (orders_num > 0);

/*
    ENDBLOCK
*/
