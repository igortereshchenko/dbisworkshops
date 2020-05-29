
drop SEQUENCE dept_seq;

CREATE SEQUENCE dept_seq START WITH 1 INCREMENT BY 1;

CREATE OR REPLACE TRIGGER dept_bir 
BEFORE INSERT or UPDATE ON user_table_sql 
FOR EACH ROW
WHEN ( new.id IS NULL )
BEGIN
   :new.id := dept_seq.nextval;
END;

CREATE OR REPLACE TRIGGER user_trigg 
BEFORE INSERT or UPDATE ON user_table_sql
FOR EACH ROW
BEGIN
    IF :new.user_name is NULL
    THEN
        raise_application_error(-20004,'user_name is NULL');
    END IF;

    IF :new.user_mail is NULL
    THEN
        raise_application_error(-20004,'user_mail is NULL');
    END IF;
    
    IF :new.user_mail NOT LIKE '%@%.%'
    THEN
        raise_application_error(-20001,'User mail is not valid!');
    END IF;
    
    IF :new.user_age is NULL
    THEN
        raise_application_error(-20004,'user_age is NULL');
    END IF;
    
    IF :new.user_age < 18
    THEN
        raise_application_error(-20015,'User age is not valid!');
    END IF;
    
    IF :new.edrpou is NULL
    THEN
        raise_application_error(-20004,'login is NULL');
    END IF;

    IF :new.user_pass is NULL
    THEN
        raise_application_error(-20004,'user_pass is NULL');
    END IF;
    
    IF LENGTH(:new.edrpou) != 6
    THEN
        raise_application_error(-20004,'Invalid EDRPOU code');
    END IF;
    
    IF LENGTH(:new.user_pass) < 5
    THEN
        raise_application_error(-20004,'length of passsword < 5');
    END IF;
END;


CREATE OR REPLACE TRIGGER question_trigger 
BEFORE INSERT OR UPDATE ON question_table_sql
FOR EACH ROW
DECLARE
BEGIN
    if :NEW.time_creating < SYSDATE
    THEN
        raise_application_error(-20004,'error with time');
    END IF;
    
    IF LENGTH(:new.question) < 5
    THEN
        raise_application_error(-20004,'Question is too short');
    END IF;
END;