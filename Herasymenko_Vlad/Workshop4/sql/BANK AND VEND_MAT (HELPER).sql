/* HELPER TABLES PACKAGE (DECLARATION) */
CREATE OR REPLACE PACKAGE helper_tables_p AS
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
    counter_fk OUT NUMBER,
    user_message OUT NVARCHAR2);

  PROCEDURE update_vend_mat
    (
      new_mat_id_fk IN VEND_MAT_T.MATERIAL_ID_FK%TYPE,
      v_ed_fk       IN VEND_MAT_T.VEND_EDRPOU_FK%TYPE,
      counter_fk OUT NUMBER,
      user_message OUT NVARCHAR2
    ); 

PROCEDURE delete_vend_mat(
    v_ed_fk    IN VEND_MAT_T.VEND_EDRPOU_FK%TYPE,
    user_message OUT NVARCHAR2); 

END helper_tables_p;



/

/* HELPER TABLES PACKAGE (BODY) */
CREATE OR REPLACE PACKAGE BODY helper_tables_p
AS
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
    user_message := '����� ��� ���� ������ ������!';
  EXCEPTION
  WHEN non_existent_fk THEN
    user_message := '�� ���� ������������ � ����� ������!';
  WHEN ambigous_ex THEN
    user_message := '���������� ����� � ����� ������������� ������� ��� ����!';
  WHEN is_null_ex THEN
    user_message := '���� � ����`������� ���� �� ���������!';
  WHEN VALUE_ERROR THEN
    user_message := '������� ����� ���!';
  WHEN OTHERS THEN
    user_message := '������� ��������������� �������!';
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
  BEGIN
    SELECT COUNT(*)
    INTO counter_unique
    FROM BANK_T
    WHERE (BANK_T.ROZ_RAH = new_bank_rah);
    
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
    user_message               := '����� ������ ��������!';
  EXCEPTION
  WHEN non_existent_fk THEN
    user_message := '�� ���� ������������ � ����� ������!';
  WHEN ambigous_ex THEN
    user_message := '���������� ����� � ����� ������������� ������� ��� ����!';
  WHEN is_null_ex THEN
    user_message := '���� � ����`������� ���� �� ���������!';
  WHEN VALUE_ERROR THEN
    user_message := '������� ����� ���!';
  WHEN OTHERS THEN
    user_message := '������� ��������������� �������!';
  END update_bank;
  PROCEDURE delete_bank(
      v_ed_fk IN BANK_T.VEND_EDRPOU_FK%TYPE,
      user_message OUT NVARCHAR2)
  IS
  BEGIN
    DELETE FROM BANK_T WHERE BANK_T.VEND_EDRPOU_FK = v_ed_fk;
    user_message:='����� ��� ���� �������� ������!';
  EXCEPTION
  WHEN OTHERS THEN
    user_message:='������� ������� ��� �������. ������� �� ���������� �������� ��������� ����';
  END delete_bank;
  PROCEDURE add_vend_mat(
      mat_id_fk IN VEND_MAT_T.MATERIAL_ID_FK%TYPE,
      v_ed_fk   IN VEND_MAT_T.VEND_EDRPOU_FK%TYPE,
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
      (mat_id_fk,v_ed_fk
      );
    user_message := '����� ������ ������';
  EXCEPTION
  WHEN non_existent_fk THEN
    user_message := '�� ���� ������������ � ����� ������ ��� ��������� ����� ID!';
  WHEN is_null_ex THEN
    user_message := '���� � ����`������� ���� �� ���������!';
  WHEN VALUE_ERROR THEN
    user_message := '������� ����� ���!';
  WHEN OTHERS THEN
    user_message := '������� ��������������� �������!';
  END add_vend_mat;
  
  PROCEDURE update_vend_mat
    (
      new_mat_id_fk IN VEND_MAT_T.MATERIAL_ID_FK%TYPE,
      v_ed_fk       IN VEND_MAT_T.VEND_EDRPOU_FK%TYPE,
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
    SET VEND_MAT_T.MATERIAL_ID_FK   = new_mat_id_fk
    WHERE VEND_MAT_T.VEND_EDRPOU_FK = v_ed_fk;
    user_message                   := '����� ������ ������';
  EXCEPTION
  WHEN non_existent_fk THEN
    user_message := '�� ���� ������������ � ����� ������ ��� ��������� ����� ID!';
  WHEN is_null_ex THEN
    user_message := '���� � ����`������� ���� �� ���������!';
  WHEN VALUE_ERROR THEN
    user_message := '������� ����� ���!';
  WHEN OTHERS THEN
    user_message := '������� ��������������� �������!';
END update_vend_mat;

PROCEDURE delete_vend_mat(
    v_ed_fk IN VEND_MAT_T.VEND_EDRPOU_FK%TYPE,
    user_message OUT NVARCHAR2)
IS
BEGIN
  DELETE FROM VEND_MAT_T WHERE VEND_MAT_T.VEND_EDRPOU_FK = v_ed_fk;
  user_message := '����� �������� ������';
EXCEPTION
WHEN OTHERS THEN
  user_message := '������� ������� ��� �������';
END delete_vend_mat;
END helper_tables_p;
/

/**/
