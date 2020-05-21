-----------CONSTRAINTS------------

ALTER TABLE "UserProfile"
ADD CONSTRAINT name_length_check
CHECK (length(user_name) > 1);

ALTER TABLE "UserProfile"
ADD CONSTRAINT phone_check
CHECK (user_phone LIKE '+380_________' AND  REGEXP_LIKE(TRIM('+' from user_phone), '^[[:digit:]]+$'));

ALTER TABLE "UserProfile"
ADD CONSTRAINT email_check
CHECK (user_email LIKE '_%@_%._%');

-----------------------------------

ALTER TABLE "Card"
ADD CONSTRAINT card_number_check
CHECK (REGEXP_LIKE(card_number, '^[[:digit:]]+$') and length(card_number) = 16);

ALTER TABLE "Card"
ADD CONSTRAINT card_ccv_check
CHECK (REGEXP_LIKE(card_ccv, '^[[:digit:]]+$') and length(card_ccv) = 3);

-----------------------------------

ALTER TABLE "Supply"
ADD CONSTRAINT supply_ids_check
CHECK (water_supply_id > 0 AND power_supply_id > 0 AND gas_supply_id > 0);

-----------------------------------

ALTER TABLE "WaterSupply"
ADD CONSTRAINT water_fields_check
CHECK (water_hot_previous >= 0 AND water_hot_current >= 0 AND water_cold_previous >= 0 AND water_cold_current >= 0);

ALTER TABLE "WaterSupply"
ADD CONSTRAINT water_prev_check
CHECK (water_hot_current >= water_hot_previous AND water_cold_current >= water_cold_previous);

-----------------------------------

ALTER TABLE "PowerSupply"
ADD CONSTRAINT power_fields_check
CHECK (power_reading >= 0);

-----------------------------------

ALTER TABLE "GasSupply"
ADD CONSTRAINT gas_fields_check
CHECK (gas_reading >= 0);



------------TRIGGERS---------------

CREATE SEQUENCE sq_user_profile
START WITH 1 
INCREMENT BY 1 
NOMAXVALUE;

CREATE OR REPLACE TRIGGER tr_ai_user_profile before INSERT ON "UserProfile" FOR each row
BEGIN
    SELECT sq_user_profile.NEXTVAL
    INTO :new.user_id
    FROM dual;
END;
/
-----------------------------------

CREATE OR REPLACE TRIGGER card_date_check before INSERT ON "Card" FOR each row
BEGIN
    IF :new.card_date < current_date()
    THEN
        raise_application_error(-20001, 'Card expired');
    END IF;    
END;
/
CREATE OR REPLACE TRIGGER card_date_check_update before UPDATE ON "Card" FOR each row
BEGIN
    IF :new.card_date < current_date
    THEN
        raise_application_error(-20001, 'Card expired');
    END IF;    
END;
/
-----------------------------------

CREATE OR REPLACE TRIGGER water_auto_date before INSERT ON "WaterSupply" FOR each row
BEGIN
    SELECT current_date
    INTO :new.filling_date
    FROM dual;
END;
/
CREATE OR REPLACE TRIGGER water_save_date before UPDATE ON "WaterSupply" FOR each row
BEGIN
    SELECT :old.filling_date
    INTO :new.filling_date
    FROM dual;
END;
/
CREATE OR REPLACE TRIGGER water_all_null_check before INSERT ON "WaterSupply" FOR each row
BEGIN
    IF :new.water_hot_previous IS NULL AND :new.water_hot_current IS NULL
    AND :new.water_cold_previous IS NULL AND :new.water_cold_current IS NULL
    THEN
        raise_application_error(-20002, 'All fields are empty');
    END IF;    
END;
/
CREATE OR REPLACE TRIGGER water_nullifying_check before UPDATE ON "WaterSupply" FOR each row
BEGIN
    IF :new.water_hot_previous IS NULL AND :old.water_hot_previous IS NOT NULL
    OR :new.water_hot_current IS NULL AND :old.water_hot_current IS NOT NULL
    OR :new.water_cold_previous IS NULL AND :old.water_cold_previous IS NOT NULL
    OR :new.water_cold_current IS NULL AND :old.water_cold_current IS NOT NULL
    THEN
        raise_application_error(-20003, 'Can`t nullify existing data');
    END IF;
END;
/

-----------------------------------

CREATE OR REPLACE TRIGGER power_auto_date before INSERT ON "PowerSupply" FOR each row
BEGIN
    SELECT current_date
    INTO :new.filling_date
    FROM dual;
END;
/
CREATE OR REPLACE TRIGGER power_save_date before UPDATE ON "PowerSupply" FOR each row
BEGIN
    SELECT :old.filling_date
    INTO :new.filling_date
    FROM dual;
END;
/

-----------------------------------

CREATE OR REPLACE TRIGGER gas_auto_date before INSERT ON "GasSupply" FOR each row
BEGIN
    SELECT current_date
    INTO :new.filling_date
    FROM dual;
END;
/
CREATE OR REPLACE TRIGGER gas_save_date before UPDATE ON "GasSupply" FOR each row
BEGIN
    SELECT :old.filling_date
    INTO :new.filling_date
    FROM dual;
END;
/

-----------------------------------