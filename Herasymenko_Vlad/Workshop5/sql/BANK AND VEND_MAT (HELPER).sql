/* HELPER TABLES PACKAGE (DECLARATION) */
CREATE OR REPLACE type id_array IS varray(10000) OF NUMBER;

CREATE OR REPLACE PACKAGE helper_tables_p AS

    FUNCTION get_bank_name(
      v_ed IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN BANK_T.VEND_BANK_NAME%TYPE;
    
   FUNCTION get_bank_mfo(
      v_ed IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN BANK_T.MFO%TYPE;   

  FUNCTION get_bank_roz_rah(
      v_ed IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN BANK_T.ROZ_RAH%TYPE;

PROCEDURE add_bank(
    bank_name    IN BANK_T.VEND_BANK_NAME%TYPE,
    bank_rah    IN BANK_T.ROZ_RAH%TYPE,
    bank_mfo  IN BANK_T.MFO%TYPE,
    v_ed_fk    IN BANK_T.VEND_EDRPOU_FK%TYPE,
    counter_fk OUT NUMBER,
    counter_unique OUT NUMBER,
    user_message OUT NVARCHAR2);

PROCEDURE update_bank(
    new_bank_name    IN BANK_T.VEND_BANK_NAME%TYPE,
    new_bank_rah    IN BANK_T.ROZ_RAH%TYPE,
    new_bank_mfo  IN BANK_T.MFO%TYPE,
    v_ed_fk    IN BANK_T.VEND_EDRPOU_FK%TYPE,
    counter_fk OUT NUMBER,
    counter_unique OUT NUMBER,
    user_message OUT NVARCHAR2);  

PROCEDURE delete_bank(
    v_ed_fk    IN BANK_T.VEND_EDRPOU_FK%TYPE,
    user_message OUT NVARCHAR2); 
    
    
    
    
PROCEDURE add_vend_mat(
    mat_id_fk    IN VEND_MAT_T.MATERIAL_ID_FK%TYPE,
    v_ed_fk    IN VEND_MAT_T.VEND_EDRPOU_FK%TYPE,
    price IN VEND_MAT_T.PRICE%TYPE,
    counter_fk OUT NUMBER,
    user_message OUT NVARCHAR2);

  PROCEDURE update_vend_mat
    (
      new_mat_id_fk IN VEND_MAT_T.MATERIAL_ID_FK%TYPE,
      v_ed_fk       IN VEND_MAT_T.VEND_EDRPOU_FK%TYPE,
      new_price IN VEND_MAT_T.PRICE%TYPE,
      counter_fk OUT NUMBER,
      user_message OUT NVARCHAR2
    ); 

PROCEDURE delete_vend_mat(
    mat_id    IN VEND_MAT_T.MATERIAL_ID_FK%TYPE,
    v_ed_fk IN VEND_MAT_T.VEND_EDRPOU_FK%TYPE,
    user_message OUT NVARCHAR2); 

END helper_tables_p;



/

/* HELPER TABLES PACKAGE (BODY) */
CREATE OR REPLACE PACKAGE BODY helper_tables_p
AS

  FUNCTION get_bank_name(
      v_ed IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN BANK_T.VEND_BANK_NAME%TYPE
  IS
    b_name BANK_T.VEND_BANK_NAME%TYPE;
  BEGIN
    SELECT BANK_T.VEND_BANK_NAME
    INTO b_name
    FROM BANK_T
    WHERE BANK_T.VEND_EDRPOU_FK = v_ed;
    
    IF b_name IS NULL THEN
      RETURN 'Назви банку не вказано';
    END IF;
    
    RETURN b_name;
    EXCEPTION
    WHEN OTHERS THEN
    RETURN 'Назви банку не вказано';
  END get_bank_name;
  


  FUNCTION get_bank_mfo(
      v_ed IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN BANK_T.MFO%TYPE
  IS
    mfo BANK_T.MFO%TYPE;
  BEGIN
    SELECT BANK_T.MFO
    INTO mfo
    FROM BANK_T
    WHERE BANK_T.VEND_EDRPOU_FK = v_ed;
    
    IF mfo IS NULL THEN
      RETURN 'МФО банку не вказано';
    END IF;
    
    RETURN mfo;
    EXCEPTION
    WHEN OTHERS THEN
    RETURN 'МФО банку не вказано';
  END get_bank_mfo;



  FUNCTION get_bank_roz_rah(
      v_ed IN VENDORS_T.VEND_EDRPOU%TYPE)
    RETURN BANK_T.ROZ_RAH%TYPE
  IS
    bank_rr BANK_T.ROZ_RAH%TYPE;
  BEGIN
    SELECT BANK_T.ROZ_RAH
    INTO bank_rr
    FROM BANK_T
    WHERE BANK_T.VEND_EDRPOU_FK = v_ed;
    
    IF bank_rr IS NULL THEN
      RETURN 'Не задано рахунку';
    END IF;
    
    RETURN bank_rr;
  END get_bank_roz_rah;

  PROCEDURE add_bank(
      bank_name IN BANK_T.VEND_BANK_NAME%TYPE,
      bank_rah  IN BANK_T.ROZ_RAH%TYPE,
      bank_mfo  IN BANK_T.MFO%TYPE,
      v_ed_fk   IN BANK_T.VEND_EDRPOU_FK%TYPE,
      counter_fk OUT NUMBER,
      counter_unique OUT NUMBER,
      user_message OUT NVARCHAR2)
  IS
    is_null_ex      EXCEPTION;
    ambigous_ex     EXCEPTION;
    non_existent_fk EXCEPTION;
  BEGIN
    SELECT COUNT(*)
    INTO counter_unique
    FROM BANK_T
    WHERE (BANK_T.ROZ_RAH = bank_rah);
    IF counter_unique     > 0 THEN
      RAISE ambigous_ex;
    END IF;
    SELECT COUNT(*) INTO counter_fk FROM VENDORS_T WHERE (VEND_EDRPOU = v_ed_fk);
    IF counter_fk = 0 THEN
      RAISE non_existent_fk;
    END IF;
    IF (bank_name IS NULL) OR (bank_rah IS NULL) OR (bank_mfo IS NULL) OR (v_ed_fk IS NULL) THEN
      RAISE is_null_ex;
    END IF;
    IF LENGTH(bank_mfo) != 6 THEN
      RAISE VALUE_ERROR;
    END IF;
    INSERT INTO BANK_T VALUES
      (bank_name,bank_rah,bank_mfo,v_ed_fk
      );
    user_message := 'Запис про банк додано успішно!';
  EXCEPTION
  WHEN non_existent_fk THEN
    user_message := 'Не існує постачальнка з таким ЄДРПОУ!';
  WHEN ambigous_ex THEN
    user_message := 'Банківський запис з таким розрахунковим номером вже існує!';
  WHEN is_null_ex THEN
    user_message := 'Одне з обов`язкових полів не заповнено!';
  WHEN VALUE_ERROR THEN
    user_message := 'Введено невірні дані!';
  WHEN OTHERS THEN
    user_message := 'Сталася непередбачувана помилка!';
  END add_bank;
  
  PROCEDURE update_bank
    (
      new_bank_name IN BANK_T.VEND_BANK_NAME%TYPE,
      new_bank_rah  IN BANK_T.ROZ_RAH%TYPE,
      new_bank_mfo  IN BANK_T.MFO%TYPE,
      v_ed_fk       IN BANK_T.VEND_EDRPOU_FK%TYPE,
      counter_fk OUT NUMBER,
      counter_unique OUT NUMBER,
      user_message OUT NVARCHAR2
    )
  IS
    is_null_ex      EXCEPTION;
    ambigous_ex     EXCEPTION;
    non_existent_fk EXCEPTION;
    current_rr BANK_T.ROZ_RAH%TYPE;
  BEGIN
    
    SELECT BANK_T.ROZ_RAH
    INTO current_rr
    FROM BANK_T
    WHERE BANK_T.VEND_EDRPOU_FK = v_ed_fk;
  
    SELECT COUNT(*)
    INTO counter_unique
    FROM BANK_T
    WHERE (BANK_T.ROZ_RAH = new_bank_rah) AND ( BANK_T.ROZ_RAH !=  current_rr);
    
    IF counter_unique     > 0 THEN
      RAISE ambigous_ex;
    END IF;
    
    SELECT COUNT(*) INTO counter_fk FROM VENDORS_T WHERE (VEND_EDRPOU = v_ed_fk);
    IF counter_fk = 0 THEN
      RAISE non_existent_fk;
    END IF;
    IF (new_bank_name IS NULL) OR (new_bank_rah IS NULL) OR (new_bank_mfo IS NULL) OR (v_ed_fk IS NULL) THEN
      RAISE is_null_ex;
    END IF;
    IF LENGTH(new_bank_mfo) != 6 THEN
      RAISE VALUE_ERROR;
    END IF;
    UPDATE BANK_T
    SET BANK_T.VEND_BANK_NAME   = new_bank_name,
      BANK_T.ROZ_RAH            =new_bank_rah,
      BANK_T.MFO                =new_bank_mfo
    WHERE BANK_T.VEND_EDRPOU_FK = v_ed_fk;
    user_message               := 'Запис успішно оновлено!';
  EXCEPTION
  WHEN non_existent_fk THEN
    user_message := 'Не існує постачальнка з таким ЄДРПОУ!';
  WHEN ambigous_ex THEN
    user_message := 'Банківський запис з таким розрахунковим номером вже існує!';
  WHEN is_null_ex THEN
    user_message := 'Одне з обов`язкових полів не заповнено!';
  WHEN VALUE_ERROR THEN
    user_message := 'Введено невірні дані!';
  WHEN OTHERS THEN
    user_message := 'Сталася непередбачувана помилка!';
  END update_bank;
  PROCEDURE delete_bank(
      v_ed_fk IN BANK_T.VEND_EDRPOU_FK%TYPE,
      user_message OUT NVARCHAR2)
  IS
  BEGIN
    DELETE FROM BANK_T WHERE BANK_T.VEND_EDRPOU_FK = v_ed_fk;
    user_message:='Запис про банк видалено успішно!';
  EXCEPTION
  WHEN OTHERS THEN
    user_message:='Сталася помилка при видалені. Можливо Ви намагалися видалити неіснуючий банк';
  END delete_bank;
  PROCEDURE add_vend_mat(
      mat_id_fk IN VEND_MAT_T.MATERIAL_ID_FK%TYPE,
      v_ed_fk   IN VEND_MAT_T.VEND_EDRPOU_FK%TYPE,
      price IN VEND_MAT_T.PRICE%TYPE,
      counter_fk OUT NUMBER,
      user_message OUT NVARCHAR2)
  IS
    is_null_ex      EXCEPTION;
    non_existent_fk EXCEPTION;
  BEGIN
    SELECT COUNT(*) INTO counter_fk FROM VENDORS_T WHERE (VEND_EDRPOU = v_ed_fk);
    IF counter_fk = 0 THEN
      RAISE non_existent_fk;
    END IF;
    SELECT COUNT(*)
    INTO counter_fk
    FROM MATERIALS_T
    WHERE (MATERIAL_ID = mat_id_fk);
    IF counter_fk      = 0 THEN
      RAISE non_existent_fk;
    END IF;
    IF (mat_id_fk IS NULL) OR (v_ed_fk IS NULL) THEN
      RAISE is_null_ex;
    END IF;
    INSERT INTO VEND_MAT_T VALUES
      (mat_id_fk,v_ed_fk,price
      );
    user_message := 'Запис додано успішно';
  EXCEPTION
  WHEN non_existent_fk THEN
    user_message := 'Не існує постачальнка з таким ЄДРПОУ або матеріалуз таким ID!';
  WHEN is_null_ex THEN
    user_message := 'Одне з обов`язкових полів не заповнено!';
  WHEN VALUE_ERROR THEN
    user_message := 'Введено невірні дані!';
  WHEN OTHERS THEN
    user_message := 'Сталася непередбачувана помилка!';
  END add_vend_mat;
  
  PROCEDURE update_vend_mat
    (
      new_mat_id_fk IN VEND_MAT_T.MATERIAL_ID_FK%TYPE,
      v_ed_fk       IN VEND_MAT_T.VEND_EDRPOU_FK%TYPE,
      new_price IN VEND_MAT_T.PRICE%TYPE,
      counter_fk OUT NUMBER,
      user_message OUT NVARCHAR2
    )
  IS
    is_null_ex      EXCEPTION;
    non_existent_fk EXCEPTION;
  BEGIN
    SELECT COUNT(*) INTO counter_fk FROM VENDORS_T WHERE (VEND_EDRPOU = v_ed_fk);
    IF counter_fk = 0 THEN
      RAISE non_existent_fk;
    END IF;
    SELECT COUNT(*)
    INTO counter_fk
    FROM MATERIALS_T
    WHERE (MATERIAL_ID = new_mat_id_fk);
    IF counter_fk      = 0 THEN
      RAISE non_existent_fk;
    END IF;
    IF (new_mat_id_fk IS NULL) OR (v_ed_fk IS NULL) THEN
      RAISE is_null_ex;
    END IF;
    UPDATE VEND_MAT_T
    SET VEND_MAT_T.MATERIAL_ID_FK = new_mat_id_fk,VEND_MAT_T.PRICE = new_price
    WHERE VEND_MAT_T.VEND_EDRPOU_FK = v_ed_fk;
    user_message                   := 'Запис змінено успішно';
  EXCEPTION
  WHEN non_existent_fk THEN
    user_message := 'Не існує постачальнка з таким ЄДРПОУ або матеріалуз таким ID!';
  WHEN is_null_ex THEN
    user_message := 'Одне з обов`язкових полів не заповнено!';
  WHEN VALUE_ERROR THEN
    user_message := 'Введено невірні дані!';
  WHEN OTHERS THEN
    user_message := 'Сталася непередбачувана помилка!';
END update_vend_mat;

PROCEDURE delete_vend_mat(
    mat_id IN VEND_MAT_T.MATERIAL_ID_FK%TYPE,
    v_ed_fk IN VEND_MAT_T.VEND_EDRPOU_FK%TYPE,
    user_message OUT NVARCHAR2)
IS
BEGIN
  DELETE FROM VEND_MAT_T WHERE VEND_MAT_T.MATERIAL_ID_FK = mat_id AND VEND_MAT_T.VEND_EDRPOU_FK = v_ed_fk;
  user_message := 'Запис видалено успішно';
EXCEPTION
WHEN OTHERS THEN
  user_message := 'Сталася помилка при видалені';
END delete_vend_mat;


END helper_tables_p;
/

/**/
