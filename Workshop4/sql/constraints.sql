ALTER TABLE review
ADD CONSTRAINT review_fk_constraint
   FOREIGN KEY (nutrition_title, nutr_brand, nutr_price_fk, nutr_ingredient_fk)
   REFERENCES nutrition (nutr_title, nutr_brand, nutr_price, nutr_ingredient);
   
ALTER TABLE nutrition_order
ADD CONSTRAINT order_fk_constraint
   FOREIGN KEY (nutrition_title, nutr_brand, nutr_price, nutr_ingredient_fk)
   REFERENCES nutrition (nutr_title, nutr_brand, nutr_price, nutr_ingredient);
   
CREATE OR REPLACE TRIGGER check_nutr_ingredient
BEFORE UPDATE OF nutr_ingredient ON nutrition
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN

select regexp_replace(:new.nutr_ingredient, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong ingredient format for update!');
END IF;
END;
/

CREATE OR REPLACE TRIGGER check_nutr_ingredient_insert
BEFORE INSERT ON nutrition
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN
select regexp_replace(:new.nutr_ingredient, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong ingredient format for insert!');
END IF;
END;
/

CREATE OR REPLACE TRIGGER check_cust_name_update
BEFORE UPDATE of cust_name ON customer
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN
select regexp_replace(:new.cust_name, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong name format for update!');
END IF;
END;
/

CREATE OR REPLACE TRIGGER check_cust_name_insert
BEFORE Insert ON customer
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN
select regexp_replace(:new.cust_name, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong name format for insert!');
END IF;
END;
/

CREATE OR REPLACE TRIGGER check_cust_surname_update
BEFORE UPDATE of cust_surname ON customer
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN
select regexp_replace(:new.cust_surname, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong surname format for update!');
END IF;
END;
/

CREATE OR REPLACE TRIGGER check_cust_surname_insert
BEFORE Insert ON customer
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN
select regexp_replace(:new.cust_surname, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong surname format for insert!');
END IF;
END;
/