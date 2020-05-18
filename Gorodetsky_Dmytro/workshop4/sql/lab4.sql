create table book(
    book_name VARCHAR2(200),
    author VARCHAR2(80),
    price NUMBER(8, 2),
    genre VARCHAR2(50), 
    on_storage NUMBER(7), 
    book_description VARCHAR2(500) NOT NULL,
    book_edition VARCHAR2(50) NOT NULL,
    number_of_purchases NUMBER NOT NULL, 
    CONSTRAINT book_constraint PRIMARY KEY (book_name, author, price, genre),
    CONSTRAINT check_price CHECK (price >= 0),
    CONSTRAINT check_number_of_purchases CHECK (number_of_purchases >= 0)
    CONSTRAINT check_on_storage CHECK (on_storage >= 0)
);

create table customer(
    first_name VARCHAR2(100) NOT NULL, 
    second_name VARCHAR2(100), 
    email VARCHAR2(50) NOT NULL PRIMARY KEY, 
    user_login VARCHAR2(40) NOT NULL UNIQUE,
    user_password VARCHAR2(50) NOT NULL,
    CONSTRAINT email_check CHECK (REGEXP_LIKE (email, '^(\S+)\@(\S+)\.(\S+)$'))
);

create table discount(
    book_name VARCHAR2(200) NOT NULL,
    author VARCHAR2(80) NOT NULL,
    book_price_fk NUMBER(8, 2),
    book_genre_fk VARCHAR2(50), 
    discounts NUMBER(2) NOT NULL,
    discount_time TIMESTAMP NOT NULL,
    CONSTRAINT discount_constraint PRIMARY KEY (book_name, author),
    CONSTRAINT check_discount_price CHECK (book_price_fk >= 0),
    CONSTRAINT check_discounts CHECK (discounts >= 0 and discounts < 100)
);

create table book_notification(
    book_name VARCHAR2(200) NOT NULL,
    author VARCHAR2(80) NOT NULL,
    book_price_fk NUMBER(8, 2),
    book_genre_fk VARCHAR2(50),
    notification_text VARCHAR2(500) NOT NULL,
    notification_time TIMESTAMP NOT NULL PRIMARY KEY,
    CONSTRAINT check_notification_price CHECK (book_price_fk >= 0)
);

create table recomendation(
    book_name VARCHAR2(200) NOT NULL,
    author VARCHAR2(80) NOT NULL,
    price NUMBER(8, 2) NOT NULL,
    genre VARCHAR2(50) NOT NULL, 
    CONSTRAINT recomendation_constraint PRIMARY KEY (book_name, author),
    CONSTRAINT check_recomendation_price CHECK (price >= 0)
);

create table review(
    book_name VARCHAR2(200) NOT NULL,
    author VARCHAR2(80) NOT NULL,
    book_price_fk NUMBER(8, 2),
    book_genre_fk VARCHAR2(50),
    book_mark INTEGER NOT NULL,
    reviews VARCHAR2(500) NOT NULL,
    rating INTEGER NOT NULL,
    CONSTRAINT review_constraint PRIMARY KEY (book_name, author),
    CONSTRAINT check_review_price CHECK (book_price_fk >= 0),
    CONSTRAINT check_book_mark CHECK (book_mark > 0 and book_mark <= 5),
    CONSTRAINT rating CHECK (rating > 0 and rating <= 5)
);

create table desired(
    book_name VARCHAR2(200) NOT NULL,
    author VARCHAR2(80) NOT NULL,
    price NUMBER(8, 2) NOT NULL,
    genre VARCHAR2(50) NOT NULL, 
    CONSTRAINT desired_constraint PRIMARY KEY (book_name, author, price, genre),
    CONSTRAINT check_desired_price CHECK (price >= 0)
);

create table book_order(
    book_name VARCHAR2(200) NOT NULL,
    author VARCHAR2(80) NOT NULL,
    book_genre_fk VARCHAR2(50), 
    price NUMBER(8, 2) NOT NULL,
    status VARCHAR2(20) NOT NULL,
    CONSTRAINT order_constraint PRIMARY KEY (book_name, author),
    CONSTRAINT check_order_price CHECK (price >= 0)
);

ALTER TABLE discount
ADD CONSTRAINT discount_fk_constraint
   FOREIGN KEY (book_name, author, book_price_fk, book_genre_fk)
   REFERENCES book (book_name, author, price, genre);
   
ALTER TABLE book_notification
ADD CONSTRAINT notification_fk_constraint
   FOREIGN KEY (book_name, author, book_price_fk, book_genre_fk)
   REFERENCES book (book_name, author, price, genre);
   
ALTER TABLE recomendation
ADD CONSTRAINT recomendation_fk_constraint
   FOREIGN KEY (book_name, author, price, genre)
   REFERENCES book (book_name, author, price, genre);
   
ALTER TABLE review
ADD CONSTRAINT review_fk_constraint
   FOREIGN KEY (book_name, author, book_price_fk, book_genre_fk)
   REFERENCES book (book_name, author, price, genre);
   
ALTER TABLE desired
ADD CONSTRAINT desired_fk_constraint
   FOREIGN KEY (book_name, author, price, genre)
   REFERENCES book (book_name, author, price, genre);
   
ALTER TABLE book_order
ADD CONSTRAINT order_fk_constraint
   FOREIGN KEY (book_name, author, price, book_genre_fk)
   REFERENCES book (book_name, author, price, genre);
   
CREATE OR REPLACE TRIGGER check_genre
BEFORE UPDATE OF genre ON book
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN

select regexp_replace(:new.genre, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong genre format in update!'); -- if new genre value contains numbers, we don't update it
END IF;
END;
/

CREATE OR REPLACE TRIGGER check_genre_insert
BEFORE INSERT ON book
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN
select regexp_replace(:new.genre, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong genre format in insert!');
END IF;
END;
/

CREATE OR REPLACE TRIGGER check_first_name_update
BEFORE UPDATE of first_name ON customer
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN
select regexp_replace(:new.first_name, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong first name format in update!');
END IF;
END;
/

CREATE OR REPLACE TRIGGER check_first_name_insert
BEFORE Insert ON customer
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN
select regexp_replace(:new.first_name, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong first name format in insert!');
END IF;
END;
/

CREATE OR REPLACE TRIGGER check_second_name_update
BEFORE UPDATE of second_name ON customer
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN
select regexp_replace(:new.second_name, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong second name format in update!');
END IF;
END;
/

CREATE OR REPLACE TRIGGER check_second_name_insert
BEFORE Insert ON customer
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN
select regexp_replace(:new.second_name, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong second name format in insert!');
END IF;
END;
/
