/* Materials logic*/

/*CANNOT CONTAIN A NUMBER */
CREATE OR REPLACE TRIGGER check_material
BEFORE INSERT OR UPDATE
ON MATERIALS_T
FOR EACH ROW
BEGIN
IF (REGEXP_LIKE(:NEW.MATERIAL_NAME,'([0123456789])')) THEN
RAISE VALUE_ERROR;
END IF;
END;

/

/*TRIGGERS FOR DELETING AND UPDATING*/
CREATE OR REPLACE TRIGGER mat_delete_tr
AFTER DELETE
ON MATERIALS_T
FOR EACH ROW
BEGIN
DELETE FROM VEND_MAT_T
WHERE VEND_MAT_T.MATERIAL_ID_FK=:old.MATERIAL_ID;
END;

/

SET SERVEROUTPUT ON;
CREATE OR REPLACE TRIGGER mat_update_tr
AFTER UPDATE
ON MATERIALS_T
FOR EACH ROW
BEGIN
UPDATE VEND_MAT_T
SET VEND_MAT_T.MATERIAL_ID_FK = :new.MATERIAL_ID
WHERE VEND_MAT_T.MATERIAL_ID_FK = :old.MATERIAL_ID;
END;

/

/* Sorting options */
/*
SELECT VEND_MAT.MATERIAL_NAME_FK,
  VENDORS_T.VEND_NAME
FROM VEND_MAT
JOIN VENDORS_T
ON VEND_MAT.VEND_EDRPOU_FK = VENDORS_T.VEND_EDRPOU
ORDER BY VEND_MAT.MATERIAL_NAME_FK;

/

SELECT VEND_MAT.MATERIAL_NAME_FK,
  VENDORS_T.VEND_NAME
FROM VEND_MAT
JOIN VENDORS_T
ON VEND_MAT.VEND_EDRPOU_FK = VENDORS_T.VEND_EDRPOU
ORDER BY VENDORS_T.VEND_NAME;

*/


/*PACKAGE FOR MATERIALS (DECLARATION)*/
CREATE OR REPLACE PACKAGE materials_p
AS
  new_id MATERIALS_T.material_id%TYPE:=1;
  PROCEDURE add_material(
      mat_name IN MATERIALS_T.material_name%TYPE,
      counter_unique OUT NUMBER,
      user_message OUT NVARCHAR2);
      
  PROCEDURE delete_material(
      mat_id IN MATERIALS_T.material_id%TYPE,
      user_message OUT NVARCHAR2);
      
  PROCEDURE update_material(
      mat_id   IN MATERIALS_T.material_id%TYPE,
      new_name IN MATERIALS_T.material_name%TYPE,
      counter_unique OUT NUMBER,
      user_message OUT NVARCHAR2,
      counter_ids OUT NUMBER);
  /*FIND VENDORS` EDRPOU BY MATERIAL ID*/
  FUNCTION find_vend_edrpou(
      mat_id IN MATERIALS_T.material_id%TYPE)
    RETURN id_array;
  /* FIND MAT_ID BY PART OF THE NAME*/
  FUNCTION find_mat_id(
      name_pattern IN MATERIALS_T.material_name%TYPE)
    RETURN id_array;
END materials_p;


/


/*PACKAGE FOR MATERIALS (BODY)*/
CREATE OR REPLACE PACKAGE BODY materials_p
AS
  PROCEDURE add_material(
      mat_name IN MATERIALS_T.material_name%TYPE,
      counter_unique OUT NUMBER,
      user_message OUT NVARCHAR2)
  IS
    ambigous_ex EXCEPTION;
    is_null_ex  EXCEPTION;
  BEGIN
    SELECT COUNT(*)
    INTO counter_unique
    FROM MATERIALS_T
    WHERE MATERIALS_T.material_name = mat_name;
    
    IF counter_unique > 0 THEN
      RAISE ambigous_ex;
    END IF;
    
    IF (mat_name IS NULL) THEN
      RAISE is_null_ex;
    END IF;
    
    SELECT (MAX(MATERIALS_T.material_id)+1) INTO new_id FROM MATERIALS_T;
    INSERT INTO MATERIALS_T VALUES
      (mat_name,new_id);
    
    user_message := 'Матеріал успішно додано';
    
  EXCEPTION
  WHEN ambigous_ex THEN
    user_message := 'Такий матеріал вже існує!';
  WHEN is_null_ex THEN
    user_message := 'Одне з обов`язкових полів не заповнено!';
  WHEN VALUE_ERROR THEN
    user_message := 'Введено невірні дані!';  
  WHEN OTHERS THEN
    user_message := 'Сталася непередбачувана помилка!';
  END add_material;
  
  
  PROCEDURE delete_material
    (
      mat_id IN MATERIALS_T.material_id%TYPE,
      user_message OUT NVARCHAR2
    )
  IS
  BEGIN
    DELETE FROM MATERIALS_T WHERE MATERIALS_T.material_id = mat_id;
    user_message := 'Матеріал успішно видалено!';
  EXCEPTION
    WHEN others THEN
    user_message := 'Сталася помилка при видалені! Перевірте, чи існує такий матеріал.';  
  END delete_material;
  
  
  PROCEDURE update_material(
      mat_id   IN MATERIALS_T.material_id%TYPE,
      new_name IN MATERIALS_T.material_name%TYPE,
      counter_unique OUT NUMBER,
      user_message OUT NVARCHAR2,
      counter_ids OUT NUMBER)
  IS
    ambigous_ex EXCEPTION;
    is_null_ex  EXCEPTION;
    not_existent EXCEPTION;
  BEGIN
    SELECT COUNT(*)
    INTO counter_unique
    FROM MATERIALS_T
    WHERE MATERIALS_T.material_name = new_name;
    
    IF counter_unique               > 0 THEN
      RAISE ambigous_ex;
    END IF;
    
    IF (new_name IS NULL) OR (mat_id IS NULL) THEN
      RAISE is_null_ex;
    END IF;
    
    SELECT COUNT(*)
    INTO counter_ids
    FROM MATERIALS_T
    WHERE MATERIALS_T.material_id = mat_id;
    
    IF counter_ids = 0 THEN
      RAISE not_existent;
    END IF;
    
    UPDATE MATERIALS_T
    SET MATERIALS_T.material_name = new_name
    WHERE MATERIALS_T.material_id = mat_id;
    user_message := 'Матеріал оновлено успішно';
    
  EXCEPTION
  WHEN ambigous_ex THEN
    user_message := 'Матеріал з такою назвою вже існує!';
  WHEN is_null_ex THEN
    user_message := 'Одне з обов`язкових полів не заповнено!';
  WHEN VALUE_ERROR THEN
    user_message := 'Введено невірні дані!';
  WHEN not_existent THEN
    user_message := 'Матеріалу, назву якого Ви хочете змінити не існує!';
  WHEN OTHERS THEN
    user_message := 'Сталася непередбачувана помилка!';
  END update_material;
  
  
/*FIND VENDORS` EDRPOU BY MATERIAL ID*/
  FUNCTION find_vend_edrpou(
      mat_id IN MATERIALS_T.MATERIAL_ID%TYPE)
    RETURN id_array
  IS
    edrpous id_array;
  BEGIN
    SELECT VEND_MAT_T.VEND_EDRPOU_FK BULK COLLECT
    INTO edrpous
    FROM MATERIALS_T
    JOIN VEND_MAT_T
    ON VEND_MAT_T.MATERIAL_ID_FK  = MATERIALS_T.MATERIAL_ID
    WHERE MATERIALS_T.MATERIAL_ID = mat_id;
    RETURN edrpous;
  END find_vend_edrpou;
  
  
/* FIND MAT_ID BY PART OF THE NAME*/
  FUNCTION find_mat_id(
      name_pattern IN MATERIALS_T.MATERIAL_NAME%TYPE)
    RETURN id_array
  IS
    idents id_array;
  BEGIN
    SELECT MATERIALS_T.material_id BULK COLLECT
    INTO idents
    FROM MATERIALS_T
    WHERE LOWER(TRIM(MATERIALS_T.MATERIAL_NAME)) LIKE ('%'
      || LOWER(TRIM(name_pattern))
      || '%');
    RETURN idents;
  END find_mat_id;
END materials_p;

/