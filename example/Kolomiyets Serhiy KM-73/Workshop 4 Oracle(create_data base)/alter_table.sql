alter table categories
add constraint pk_cat
primary key 
(id);

alter table products
add constraint pk_product
primary key 
(id);

alter table orders
add constraint pk_order
primary key 
(id);

alter table products
add constraint fk_category
foreign key 
(cat)
references categories(id);

alter table orders
add constraint fk_product
foreign key 
(code)
references products(id);

alter table products
add constraint check_available
check (available='y' or available='n');

ALTER TABLE products
ADD CONSTRAINT check_price
CHECK (price > 0);

ALTER TABLE orders
ADD CONSTRAINT check_amount
CHECK (amount > 0 and amount < 11 );