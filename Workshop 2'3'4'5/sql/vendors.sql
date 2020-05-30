/* VENDORS LOGIC */

CREATE OR REPLACE type id_array IS varray(10000) OF NUMBER;

CREATE OR REPLACE TRIGGER tr_delete
AFTER DELETE
ON VENDORS_T
FOR EACH ROW
BEGIN
DELETE FROM VEND_MAT_T
WHERE VEND_MAT_T.vend_edrpou_fk=:old.vend_edrpou;
END;
/

CREATE OR REPLACE TRIGGER tr_update
AFTER UPDATE
ON VENDORS_T
FOR EACH ROW
BEGIN
UPDATE VEND_MAT_T
SET VEND_MAT_T.vend_edrpou_fk = :new.vend_edrpou
WHERE VEND_MAT_T.vend_edrpou_fk = :old.vend_edrpou;
END;

/
CREATE OR REPLACE TRIGGER check_vendor_email
BEFORE INSERT OR UPDATE
ON VENDORS_T
FOR EACH ROW
BEGIN
IF (:NEW.email NOT LIKE '%@%') AND (:NEW.email IS NOT NULL)  THEN
RAISE VALUE_ERROR;
END IF;
END;

/

CREATE OR REPLACE TRIGGER check_vendor_city
BEFORE INSERT OR UPDATE
ON VENDORS_T
FOR EACH ROW
BEGIN
IF (LOWER(:NEW.vend_city) NOT LIKE '%київ%') THEN
RAISE VALUE_ERROR;
END IF;
END;



/

/*VENDORS PACKAGE (DECLARATION)*/
CREATE OR REPLACE PACKAGE vendors_p AS 

   PROCEDURE add_vendor(
    v_name      IN VENDORS_T.vend_name%TYPE,
    v_edrpou    IN VENDORS_T.VEND_EDRPOU%TYPE,
    v_adress  IN VENDORS_T.VEND_ADRESS%TYPE,
    v_city    IN VENDORS_T.VEND_CITY%TYPE,
    v_tel     IN VENDORS_T.TELEPHONE%TYPE,
    v_manager IN VENDORS_T.MANAGER_NAME%TYPE,
    v_email   IN VENDORS_T.EMAIL%TYPE,
    counter_unique OUT NUMBER,
    user_message OUT NVARCHAR2);
    
    
PROCEDURE delete_vendor(v_edrpou IN VENDORS_T.VEND_EDRPOU%TYPE,
                        user_message OUT NVARCHAR2);
   
   /*UPDATES ALL COLUMNS, BECAUSE VENDOR_T WILL STAY UNCHANGED*/
PROCEDURE update_vendor(
    v_edrpou    IN VENDORS_T.VEND_EDRPOU%TYPE,
    new_name    IN VENDORS_T.vend_name%TYPE,
    new_adress  IN VENDORS_T.VEND_ADRESS%TYPE,
    new_city    IN VENDORS_T.VEND_CITY%TYPE,
    new_tel     IN VENDORS_T.TELEPHONE%TYPE,
    new_manager IN VENDORS_T.MANAGER_NAME%TYPE,
    new_email   IN VENDORS_T.EMAIL%TYPE,
    counter_unique OUT NUMBER,
    user_message OUT NVARCHAR2,
    counter_ids OUT NUMBER);
      
   
   FUNCTION get_vend_name(
   v_edrpou IN VENDORS_T.VEND_EDRPOU%TYPE)
   RETURN VENDORS_T.VEND_NAME%TYPE;
   
    FUNCTION get_vend_city(
      v_ed IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN VENDORS_T.VEND_CITY%TYPE;
    
  FUNCTION get_vend_adress(
      v_ed IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN VENDORS_T.VEND_ADRESS%TYPE;

  FUNCTION get_vend_tel(
      v_ed IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN VENDORS_T.TELEPHONE%TYPE;
    
  FUNCTION get_vend_email(
      v_ed IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN VENDORS_T.EMAIL%TYPE;
    
  FUNCTION get_vend_m_name(
      v_ed IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN VENDORS_T.MANAGER_NAME%TYPE;

END vendors_p;


/


/*VENDORS PACKAGE (BODY)*/
CREATE OR REPLACE PACKAGE BODY vendors_p
AS
  PROCEDURE add_vendor(
      v_name    IN VENDORS_T.vend_name%TYPE,
      v_edrpou  IN VENDORS_T.VEND_EDRPOU%TYPE,
      v_adress  IN VENDORS_T.VEND_ADRESS%TYPE,
      v_city    IN VENDORS_T.VEND_CITY%TYPE,
      v_tel     IN VENDORS_T.TELEPHONE%TYPE,
      v_manager IN VENDORS_T.MANAGER_NAME%TYPE,
      v_email   IN VENDORS_T.EMAIL%TYPE,
      counter_unique OUT NUMBER,
      user_message OUT NVARCHAR2)
  IS
    ambigous_ex EXCEPTION;
    is_null_ex  EXCEPTION;
    not_kyiv EXCEPTION;
  BEGIN
    SELECT COUNT(*)
    INTO counter_unique
    FROM VENDORS_T
    WHERE (VENDORS_T.vend_name = v_name) OR (VENDORS_T.VEND_EDRPOU = v_edrpou);
    IF counter_unique               > 0 THEN
      RAISE ambigous_ex;
    END IF;
    
    IF (v_name IS NULL) OR (v_edrpou IS NULL) OR (v_city IS NULL) THEN
      RAISE is_null_ex;
    END IF;
    
    IF LENGTH(v_edrpou) != 8 THEN
      RAISE VALUE_ERROR;
    END IF;
    
    IF (LOWER(v_city) NOT LIKE '%київ%') THEN
      RAISE not_kyiv;
    END IF;
    
    INSERT    
    INTO VENDORS_T VALUES
      (
        v_name,
        v_edrpou,
        v_adress,
        v_city,
        v_tel,
        v_manager,
        v_email
      );
      user_message := 'Постачальника додано успішно!';
  EXCEPTION
  WHEN ambigous_ex THEN
    user_message := 'Такий постачальник вже існує!';
  WHEN is_null_ex THEN
    user_message := 'Одне з обов`язкових полів не заповнено!';
  WHEN not_kyiv THEN
    user_message := 'Міста роботи повинні включати Київ!';  
  WHEN VALUE_ERROR THEN
    user_message := 'Введено невірні дані!';
  WHEN OTHERS THEN
    user_message := 'Сталася непередбачувана помилка!';
  END add_vendor;
  
  PROCEDURE delete_vendor
    (
      v_edrpou IN VENDORS_T.VEND_EDRPOU%TYPE,
      user_message OUT NVARCHAR2
    )
  IS
  BEGIN
    DELETE FROM VENDORS_T WHERE VENDORS_T.VEND_EDRPOU = v_edrpou;
    user_message := 'Постачальника видалено успішно!';
  EXCEPTION
  WHEN others THEN
    user_message := 'Сталася помилка при видалені постачальника!';
  END delete_vendor;
  
  PROCEDURE update_vendor(
      v_edrpou    IN VENDORS_T.VEND_EDRPOU%TYPE,
      new_name    IN VENDORS_T.vend_name%TYPE,
      new_adress  IN VENDORS_T.VEND_ADRESS%TYPE,
      new_city    IN VENDORS_T.VEND_CITY%TYPE,
      new_tel     IN VENDORS_T.TELEPHONE%TYPE,
      new_manager IN VENDORS_T.MANAGER_NAME%TYPE,
      new_email   IN VENDORS_T.EMAIL%TYPE,
      counter_unique OUT NUMBER,
      user_message OUT NVARCHAR2,
      counter_ids OUT NUMBER)
  IS
    ambigous_ex EXCEPTION;
    is_null_ex  EXCEPTION;
    not_existent EXCEPTION;
    not_kyiv EXCEPTION;
  BEGIN
    SELECT COUNT(*)
    INTO counter_unique
    FROM VENDORS_T
    WHERE (VENDORS_T.vend_name = new_name);
    
    IF counter_unique               > 0 THEN
      RAISE ambigous_ex;
    END IF;
    
    IF (new_name IS NULL) OR (v_edrpou IS NULL) OR (new_city IS NULL) THEN
      RAISE is_null_ex;
    END IF;
    
    IF LENGTH(v_edrpou) != 8 THEN
      RAISE VALUE_ERROR;
    END IF;
    
    IF (LOWER(new_city) NOT LIKE '%київ%') THEN
      RAISE not_kyiv;
    END IF;
    
    SELECT COUNT(*)
    INTO counter_ids
    FROM VENDORS_T
    WHERE VENDORS_T.VEND_EDRPOU = v_edrpou;
    
    IF counter_ids = 0 THEN
      RAISE not_existent;
    END IF;
  
    UPDATE VENDORS_T
    SET VENDORS_T.vend_name     =new_name,
      VENDORS_T.VEND_ADRESS     = new_adress,
      VENDORS_T.VEND_CITY       = new_city,
      VENDORS_T.TELEPHONE       = new_tel,
      VENDORS_T.MANAGER_NAME    = new_manager,
      VENDORS_T.EMAIL           = new_emai
  EXCEPTION
  WHEN is_null_ex THEN
    user_message := 'Одне з обов`язкових полів не заповнено!';
  WHEN not_kyiv THEN
    user_message := 'Міста роботи повинні включати Київ!';
  WHEN VALUE_ERROR THEN
    user_message := 'Введено невірні дані!';
  WHEN OTHERS THEN
    user_message := 'Сталася непередбачувана помилка!';
  END update_vendor;
  
  FUNCTION get_edrpou(
      name_pattern IN VENDORS_T.vend_name%TYPE)
    RETURN id_array
  IS
    edrpous_array id_array;
  BEGIN
    SELECT VENDORS_T.VEND_EDRPOU BULK COLLECT
    INTO edrpous_array
    FROM VENDORS_T
    WHERE LOWER(TRIM(VENDORS_T.VEND_NAME)) LIKE ('%'
      || LOWER(TRIM(name_pattern))
      || '%');
    RETURN edrpous_array;
  END get_edrpou;
  
  FUNCTION get_products(
      v_edrpou IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN id_array
  IS
    prod_ids_array id_array;
  BEGIN
    SELECT VEND_MAT_T.MATERIAL_ID_FK BULK COLLECT
    INTO prod_ids_array
    FROM VEND_MAT_T
    WHERE VEND_MAT_T.VEND_EDRPOU_FK = v_edrpou;
    RETURN prod_ids_array;
  END get_products;
  
  FUNCTION get_vend_name(
      v_edrpou IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN VENDORS_T.VEND_NAME%TYPE
  IS
    v_name VENDORS_T.VEND_NAME%TYPE;
  BEGIN
    SELECT VENDORS_T.VEND_NAME
    INTO v_name
    FROM VENDORS_T
    WHERE VENDORS_T.VEND_EDRPOU = v_edrpou;
    
    RETURN v_name;
  END get_vend_name;
  
  
  
  FUNCTION get_vend_city(
      v_ed IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN VENDORS_T.VEND_CITY%TYPE
  IS
    v_city VENDORS_T.VEND_CITY%TYPE;
  BEGIN
    SELECT VENDORS_T.VEND_CITY
    INTO v_city
    FROM VENDORS_T
    WHERE VENDORS_T.VEND_EDRPOU = v_ed;
    RETURN v_city;
    
    IF v_city IS NULL THEN
      RETURN 'Місто не вказано';
    END IF;
    
  END get_vend_city;
  
  FUNCTION get_vend_adress(
      v_ed IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN VENDORS_T.VEND_ADRESS%TYPE
  IS
    v_adr VENDORS_T.VEND_ADRESS%TYPE;
  BEGIN
    SELECT VENDORS_T.VEND_ADRESS
    INTO v_adr
    FROM VENDORS_T
    WHERE VENDORS_T.VEND_EDRPOU = v_ed;

    IF v_adr IS NULL THEN
      RETURN 'Адресу не вказано';
    END IF;  
  
    RETURN v_adr;
  END get_vend_adress;
  
  
  FUNCTION get_vend_tel(
      v_ed IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN VENDORS_T.TELEPHONE%TYPE
  IS
    v_tel VENDORS_T.TELEPHONE%TYPE;
  BEGIN
    SELECT VENDORS_T.TELEPHONE
    INTO v_tel
    FROM VENDORS_T
    WHERE VENDORS_T.VEND_EDRPOU = v_ed;
    
    IF v_tel IS NULL THEN
      RETURN 'Телефон не вказано';
    END IF;
    
    RETURN v_tel;
  END get_vend_tel;
  
  
  FUNCTION get_vend_email(
      v_ed IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN VENDORS_T.EMAIL%TYPE
  IS
    v_email VENDORS_T.EMAIL%TYPE;
  BEGIN
    SELECT VENDORS_T.EMAIL
    INTO v_email
    FROM VENDORS_T
    WHERE VENDORS_T.VEND_EDRPOU = v_ed;
    
    IF v_email IS NULL THEN
      RETURN 'E-mail не вказано';
    END IF;
    
    RETURN v_email;
  END get_vend_email;
  

  FUNCTION get_vend_m_name(
      v_ed IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN VENDORS_T.MANAGER_NAME%TYPE
  IS
    m_name VENDORS_T.MANAGER_NAME%TYPE;
  BEGIN
    SELECT VENDORS_T.MANAGER_NAME
    INTO m_name
    FROM VENDORS_T
    WHERE VENDORS_T.VEND_EDRPOU = v_ed;
    
    IF m_name IS NULL THEN
      RETURN 'Імені менеджера не вказано';
    END IF;
    
    RETURN m_name;
  END get_vend_m_name;
   
END vendors_p;

/
