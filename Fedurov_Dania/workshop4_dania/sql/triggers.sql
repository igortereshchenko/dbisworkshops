CREATE SEQUENCE user_seq START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER user_auto 
BEFORE INSERT or UPDATE ON user_database 
FOR EACH ROW
WHEN ( new.id_user IS NULL )
BEGIN
   :new.id_user := user_seq.nextval;
END;


CREATE SEQUENCE pred_seq START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER pred_auto 
BEFORE INSERT or UPDATE ON prediction_database 
FOR EACH ROW
WHEN ( new.id_pred IS NULL )
BEGIN
   :new.id_pred := pred_seq.nextval;
END;


CREATE SEQUENCE numer_seq START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER numer_auto 
BEFORE INSERT or UPDATE ON numerology_database 
FOR EACH ROW
WHEN ( new.id_nume IS NULL )
BEGIN
   :new.id_nume := numer_seq.nextval;
END;



CREATE OR REPLACE TRIGGER user_trigg 
BEFORE INSERT or UPDATE ON user_database
FOR EACH ROW
BEGIN
    IF :new.user_name is NULL
    THEN
        raise_application_error(-20004,'user_name is NULL');
    END IF;

    IF :new.user_surname is NULL
    THEN
        raise_application_error(-20004,'user_name is NULL');
    END IF;

    IF :new.user_age is NULL
    THEN
        raise_application_error(-20004,'user_age is NULL');
    END IF;
    
    IF :new.user_age < 18
    THEN
        raise_application_error(-20015,'User age is not valid!');
    END IF;

    IF :new.user_mail is NULL
    THEN
        raise_application_error(-20004,'user_mail is NULL');
    END IF;
    
    IF :new.user_mail NOT LIKE '%@%.%'
    THEN
        raise_application_error(-20001,'User mail is not valid!');
    END IF;
        
    IF :new.user_login is NULL
    THEN
        raise_application_error(-20004,'login is NULL');
    END IF;

    IF :new.user_pass is NULL
    THEN
        raise_application_error(-20004,'user_pass is NULL');
    END IF;
    
END;



CREATE OR REPLACE TRIGGER prediction_trigg 
BEFORE INSERT or UPDATE ON prediction_database
FOR EACH ROW
BEGIN
    IF :new.prediction_description is NULL
    THEN
        raise_application_error(-20004,'prediction_description is NULL');
    END IF;
   
END;


CREATE OR REPLACE TRIGGER numerology_trigg 
BEFORE INSERT or UPDATE ON numerology_database
FOR EACH ROW
BEGIN
    IF :new.numerology_date is NULL
    THEN
        raise_application_error(-20004,'numerology_date is NULL');
    END IF;
 
    IF :new.numerology_description is NULL
    THEN
        raise_application_error(-20004,'numerology_description is NULL');
    END IF;

END;



CREATE OR REPLACE TRIGGER time_trigger 
BEFORE INSERT OR UPDATE ON numerology_database
FOR EACH ROW
DECLARE
BEGIN
    if :NEW.numerology_date > SYSDATE
    THEN
        raise_application_error(-20004,'Data is bigger then today is');
    END IF;
END;