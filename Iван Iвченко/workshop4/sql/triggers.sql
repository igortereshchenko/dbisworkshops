CREATE OR REPLACE TRIGGER TRG_I_Vendors
BEFORE INSERT ON "Users"
FOR EACH ROW
DECLARE
counter INTEGER;
BEGIN
    IF :new."vendor_name" IS NULL
    THEN 
        raise_application_error(-20011,'Vendor name is empty');
    END IF;
    IF :new."vendor_email" IS NULL
    THEN 
        raise_application_error(-20011,'Vendor email is empty');
    END IF;
    IF :new."vendor_email" IS NULL
    THEN 
        raise_application_error(-20011,'Number of tickets is empty');
    END IF;
    
    SELECT COUNT(*) INTO counter
    FROM "Vendors"
    WHERE "vendor_name" = :new."vendor_name";
    IF counter> 0
    THEN
        raise_application_error(-20011,'Vendor name mast be unique');
    END IF;
END;
/
CREATE OR REPLACE TRIGGER TRG_I_Vendors
BEFORE INSERT ON "Ivents"
FOR EACH ROW
DECLARE
counter INTEGER;
BEGIN
    IF :new."event_name" IS NULL
    THEN 
        raise_application_error(-20011,'Ivent name is empty');
    END IF;
    IF :new."event_category" IS NULL
    THEN 
        raise_application_error(-20011,'Ivent email is empty');
    END IF;
    IF :new."vendor_id" IS NULL
    THEN 
        raise_application_error(-20011,'Vendor id is empty');
    END IF;
    IF :new."ticket_number" IS NULL
    THEN 
        raise_application_error(-20011,'Number of tickets is empty');
    END IF;
    
    SELECT COUNT(*) INTO counter
    FROM "Ivents"
    WHERE "event_name" = :new."event_name";
    IF counter> 0
    THEN
        raise_application_error(-20011,'Vendor name mast be unique');
    END IF;
END;
/