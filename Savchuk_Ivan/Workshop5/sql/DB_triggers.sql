/*
    This block dedicated to triggers
*/
/*
    This sub-block contains group of triggers
    that auto-generate ids for whole group of tables
*/
/*Comment table validation*/

CREATE SEQUENCE pk1_seq
    MINVALUE 1
    START WITH 1
    INCREMENT BY 1
    CACHE 20;

CREATE OR REPLACE TRIGGER pk_comment_id 
BEFORE INSERT ON comments
FOR EACH ROW
WHEN ( new.comment_id IS NULL )
BEGIN
   :new.comment_id := pk1_seq.nextval;
END;
/
/*App_user table validation*/

CREATE SEQUENCE pk2_seq
    MINVALUE 1
    START WITH 1
    INCREMENT BY 1
    CACHE 20;

CREATE OR REPLACE TRIGGER user_id_trigg 
BEFORE INSERT ON app_user
FOR EACH ROW
WHEN ( new.user_id IS NULL )
BEGIN
    :new.user_id := pk2_seq.nextval;
    IF :new.user_age < 0
    THEN
        raise_application_error(-20015,'User age is not valid!');
    END IF;
    IF :new.user_mail NOT LIKE '%@%.%'
    THEN
        raise_application_error(-20001,'User mail is not valid!');
    END IF;
    IF :new.user_phone NOT LIKE '+%'
    THEN 
        raise_application_error(-20003,'User phone number is not valid!');
    END IF;
    IF (LENGTH(TRIM(:new.user_bank)) > 19 OR LENGTH(TRIM(:new.user_bank)) < 13)
    THEN 
        raise_application_error(-20004,'User bank number is not valid!');
    END IF;
END;
/
/*Cinema table validation*/
CREATE SEQUENCE pk5_seq
    MINVALUE 1
    START WITH 1
    INCREMENT BY 1
    CACHE 20;

CREATE OR REPLACE TRIGGER pk_cinema_id 
BEFORE INSERT ON cinema
FOR EACH ROW
WHEN ( new.cinema_id IS NULL )
BEGIN
   :new.cinema_id := pk5_seq.nextval;
END;
/

/*Films table validation*/
CREATE SEQUENCE pk6_seq
    MINVALUE 1
    START WITH 1
    INCREMENT BY 1
    CACHE 20;

CREATE OR REPLACE TRIGGER pk_film_id 
BEFORE INSERT ON films
FOR EACH ROW
WHEN ( new.film_id IS NULL )
BEGIN
   :new.film_id := pk6_seq.nextval;
END;
/

/*Snack table validation*/
CREATE SEQUENCE pk7_seq
    MINVALUE 1
    START WITH 1
    INCREMENT BY 1
    CACHE 20;

CREATE OR REPLACE TRIGGER pk_snack_id 
BEFORE INSERT ON snack
FOR EACH ROW
WHEN ( new.snack_id IS NULL )
BEGIN
   :new.snack_id := pk7_seq.nextval;
END;
/
/*Orders table validation*/

CREATE SEQUENCE pk3_seq
    MINVALUE 1
    START WITH 1
    INCREMENT BY 1
    CACHE 20;

CREATE OR REPLACE TRIGGER order_id_tr 
BEFORE INSERT ON orders
FOR EACH ROW
WHEN ( new.order_id IS NULL )
BEGIN
   :new.order_id := pk3_seq.nextval;
END;
/

CREATE OR REPLACE TRIGGER order_trigge 
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    /*Updating number of orders while insert*/
    UPDATE cinema
    SET orders_num = (SELECT orders_num FROM cinema WHERE cinema_id = :new.cinema_id) + 1
    WHERE cinema_id = :new.cinema_id;
    
    IF :new.snack IS NOT NULL
    THEN
        UPDATE snack
        SET orders_num = (SELECT orders_num
                          FROM snack
                          WHERE snack_name = :new.snack) + 1
        WHERE snack_name = :new.snack;
    END IF;
END;
/


CREATE OR REPLACE TRIGGER us_age 
BEFORE INSERT ON orders
FOR EACH ROW
DECLARE
    us_ag NUMBER(38,0);
    v_age NUMBER(38,0);
BEGIN
    SELECT user_age INTO us_ag FROM app_user WHERE user_id = :new.user_id;
    SELECT age_limit INTO v_age FROM films WHERE film_name = :new.movie;
    IF (us_ag < v_age)
    THEN raise_application_error(-20010,'User age is not valid');
    END IF;
END;
/

CREATE OR REPLACE TRIGGER user_age_apdate
BEFORE UPDATE ON app_user
FOR EACH ROW
BEGIN
    IF :old.user_age < :new.user_age
    THEN 
        raise_application_error(-20011,'User age cant be changed');
    END IF;
END;
/
/* 
    END SUB-BLOCK
*/

/*
    ANOUTHER SUB-BLOCKS IN PROGRESS
*/
/*
    ENDBLOCK
*/