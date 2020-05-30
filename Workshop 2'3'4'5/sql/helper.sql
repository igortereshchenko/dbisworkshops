/* HELPER TABLES PACKAGE (DECLARATION) */
CREATE OR REPLACE type id_array IS varray(10000) OF NUMBER;

CREATE OR REPLACE PACKAGE helper_tables_p AS
    
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
