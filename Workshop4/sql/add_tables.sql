create table nutrition(
    nutr_title VARCHAR2(100),
    nutr_brand VARCHAR2(40),
    nutr_price NUMBER(8, 2),
    nutr_weight NUMBER(6, 2),
    nutr_ingredient VARCHAR2(30), 
    nutr_description VARCHAR2(500) NOT NULL,
    CONSTRAINT nutr_constraint PRIMARY KEY (nutr_title, nutr_brand, nutr_price, nutr_ingredient),
    CONSTRAINT check_nutr_price CHECK (nutr_price >= 0),
    CONSTRAINT check_nutr_weight CHECK (nutr_weight >= 0),
);

create table customer(
    cust_name VARCHAR2(80) NOT NULL, 
    cust_surname VARCHAR2(90),
    cust_login VARCHAR2(40) NOT NULL PRIMARY KEY,
    cust_password VARCHAR2(50) NOT NULL, 
    cust_email VARCHAR2(50) NOT NULL UNIQUE, 
    cust_adress VARCHAR2(300) NOT NULL
    CONSTRAINT cust_email_check CHECK (REGEXP_LIKE (cust_email, '^(\S+)\@(\S+)\.(\S+)$'))
);

create table review(
    nutr_title VARCHAR2(100) NOT NULL,
    nutr_brand VARCHAR2(40) NOT NULL,
    nutr_price_fk NUMBER(8, 2),
    nutr_ingredient_fk VARCHAR2(30),
    reviews VARCHAR2(600) NOT NULL,
    rating INTEGER NOT NULL,
    CONSTRAINT review_constraint PRIMARY KEY (nutr_title, nutr_brand),
    CONSTRAINT check_review_nutr_price CHECK (nutr_price_fk >= 0),
    CONSTRAINT rating CHECK (rating > 0 and rating <= 10)
);


create table cust_order(
    nutr_title VARCHAR2(100) NOT NULL,
    nutr_brand VARCHAR2(40) NOT NULL,
    nutr_price NUMBER(8, 2) NOT NULL,
    nutr_ingredient_fk VARCHAR2(30), 
    status VARCHAR2(25) NOT NULL,
    CONSTRAINT order_constraint PRIMARY KEY (nutr_title, nutr_brand),
    CONSTRAINT check_order_nutr_price CHECK (nutr_price >= 0)
);


