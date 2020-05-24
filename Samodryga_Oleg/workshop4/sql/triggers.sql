CREATE OR REPLACE TRIGGER TRG_I_Note
BEFORE INSERT ON "Note"
FOR EACH ROW
DECLARE
counter INTEGER;
BEGIN
    SELECT COUNT(*) INTO counter
    FROM "Note"
    WHERE "user_id" = :new."user_id";
    IF counter>40
    THEN
        raise_application_error(-20011,'Notes will be less than 40. Please delete note');
    END IF;
END;
/
CREATE OR REPLACE TRIGGER TRG_I_Users
BEFORE INSERT ON "Users"
FOR EACH ROW
DECLARE
counter INTEGER;
BEGIN
    IF :new."username" IS NULL
    THEN 
        raise_application_error(-20011,'Username is empty');
    END IF;
    IF :new."password" IS NULL
    THEN 
        raise_application_error(-20011,'Password is empty');
    END IF;
    
    SELECT COUNT(*) INTO counter
    FROM "Users"
    WHERE "username" = :new."username";
    IF counter> 0
    THEN
        raise_application_error(-20011,'Username mast be unique');
    END IF;
END;
/
CREATE OR REPLACE TRIGGER TRG_I_Country
BEFORE INSERT ON "Country"
FOR EACH ROW
DECLARE
counter INTEGER;
BEGIN
    IF :new."name" IS NULL
    THEN 
        raise_application_error(-20011,'name is empty');
    END IF;
END;
/
CREATE OR REPLACE TRIGGER TRG_I_NumbersAid
BEFORE INSERT ON "NumbersAid"
FOR EACH ROW
DECLARE
counter INTEGER;
BEGIN
    IF :new."phone_number" IS NULL
    THEN 
        raise_application_error(-20011,'phone number is empty');
    END IF;
	IF :new."country_id" IS NULL
    THEN 
        raise_application_error(-20011,'country number is empty');
    END IF;
END;
/
CREATE OR REPLACE TRIGGER TRG_I_Hospital
BEFORE INSERT ON "Hospital"
FOR EACH ROW
DECLARE
counter INTEGER;
BEGIN
    IF :new."name" IS NULL
    THEN 
        raise_application_error(-20011,'name is empty');
    END IF;
	IF :new."country_id" IS NULL
    THEN 
        raise_application_error(-20011,'phone number is empty');
    END IF;
	IF :new."adress" IS NULL
    THEN 
        raise_application_error(-20011,'adress number is empty');
    END IF;
END;
/
CREATE OR REPLACE TRIGGER TRG_I_Symptom
BEFORE INSERT ON "Symptom"
FOR EACH ROW
DECLARE
counter INTEGER;
BEGIN
    IF :new."name" IS NULL
    THEN 
        raise_application_error(-20011,'name is empty');
    END IF;
	IF :new."Description" IS NULL
    THEN 
        raise_application_error(-20011,'Description is empty');
    END IF;
END;
/
CREATE OR REPLACE TRIGGER TRG_I_Note_IsNotNull
BEFORE INSERT ON "Note"
FOR EACH ROW
DECLARE
counter INTEGER;
BEGIN
    IF :new."name" IS NULL
    THEN 
        raise_application_error(-20011,'name is empty');
    END IF;
	IF :new."user_id" IS NULL
    THEN 
        raise_application_error(-20011,'user is empty');
    END IF;
END;