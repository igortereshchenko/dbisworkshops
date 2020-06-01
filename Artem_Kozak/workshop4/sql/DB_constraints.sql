ALTER TABLE Purchased_items_list
ADD CONSTRAINT check_purchased_item_price
CHECK (item_price >= 0);

ALTER TABLE wish_items_list
ADD CONSTRAINT check_wish_item_price
CHECK (item_price >= 0);
