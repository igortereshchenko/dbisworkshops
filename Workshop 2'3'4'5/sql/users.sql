
/* Authorisation logic + DELETE AND UPDATE*/
CREATE OR REPLACE type id_array IS varray(10000) OF NUMBER;

CREATE OR REPLACE TRIGGER check_user
BEFORE INSERT OR UPDATE
ON USERS_T
FOR EACH ROW
BEGIN
IF (LENGTH(:NEW.user_pass) <4) THEN
RAISE VALUE_ERROR;
END IF;
IF (:NEW.user_email NOT LIKE '%@%') THEN
RAISE VALUE_ERROR;
END IF;
END;

/
/*PACKAGE FOR AUTHORISATION (DECLARATION)*/
CREATE OR REPLACE PACKAGE authorisation_p
AS
  FUNCTION get_username(
      ident IN USERS_T.user_id%TYPE)
    RETURN USERS_T.user_login%TYPE;
    
  FUNCTION authorisation(
      email_or_login IN USERS_T.user_login%TYPE,
      pass           IN USERS_T.user_pass%TYPE)
    RETURN USERS_T.user_id%TYPE;
    
  PROCEDURE delete_user(
      ident IN USERS_T.user_id%TYPE,
      user_message OUT NVARCHAR2);
      
  PROCEDURE change_pass(
      ident    IN USERS_T.user_id%TYPE,
      new_pass1 IN USERS_T.user_pass%TYPE,
      new_pass2 IN USERS_T.user_pass%TYPE,
      user_message OUT NVARCHAR2);
      
  PROCEDURE change_email(
      ident     IN USERS_T.user_id%TYPE,
      new_email IN USERS_T.user_email%TYPE,
      user_message OUT NVARCHAR2);
  END authorisation_p;


/
/*PACKAGE FOR AUTHORISATION (BODY)*/
CREATE OR REPLACE PACKAGE BODY authorisation_p
AS
/* GET USERID BY EMAIL OR LOGIN AND PASS */
  FUNCTION authorisation(
      email_or_login IN USERS_T.user_login%TYPE,
      pass           IN USERS_T.user_pass%TYPE)
    RETURN USERS_T.user_id%TYPE
  IS
    ident USERS_T.user_id%TYPE;
  BEGIN
    SELECT USERS_T.user_id
    INTO ident
    FROM USERS_T
    WHERE (USERS_T.user_login = email_or_login
    OR USERS_T.user_email     = email_or_login)
    AND USERS_T.user_pass     = pass;
    RETURN ident;
  EXCEPTION
  WHEN OTHERS THEN
    ident := -1;
    RETURN ident;
  END authorisation;

  /* SELECT USERNAME BY ID. USE WHEN AUTHORISATION COMPLETED AND ID IS RETURNED */
  FUNCTION get_username(
      ident IN USERS_T.user_id%TYPE)
    RETURN USERS_T.user_login%TYPE
  IS
    login USERS_T.user_login%TYPE;
  BEGIN
    IF(ident = -1) THEN
      RETURN 'Invalid login or password';
    END IF;
    SELECT USERS_T.user_login
    INTO login
    FROM USERS_T
    WHERE USERS_T.user_id = ident;
    RETURN login;
  END get_username;
  
  
  PROCEDURE delete_user(
      ident IN USERS_T.user_id%TYPE,
      user_message OUT NVARCHAR2)
  IS
  BEGIN
    DELETE FROM USERS_T WHERE USERS_T.user_id = ident;
    user_message := 'Обліковий запис успішно видалено';
  EXCEPTION
  WHEN others THEN
    user_message := 'Сталася помилка при видалені. Перевірте чи існує користувач';
  END delete_user;
  
  
PROCEDURE change_pass(
    ident     IN USERS_T.user_id%TYPE,
    new_pass1 IN USERS_T.user_pass%TYPE,
    new_pass2 IN USERS_T.user_pass%TYPE,
    user_message OUT NVARCHAR2)
IS
  different_passes_ex EXCEPTION;
  no_user_ex EXCEPTION;
BEGIN

  IF ident = -1 THEN
  RAISE no_user_ex;
  END IF;

  IF new_pass1 != new_pass2 THEN
    RAISE different_passes_ex;
  END IF;
  UPDATE USERS_T SET USERS_T.USER_PASS= new_pass1 WHERE USERS_T.user_id = ident;
  user_message := 'Пароль змінено успішно';

EXCEPTION
WHEN no_user_ex THEN
  user_message := 'Такого користувача не існує!';
WHEN different_passes_ex THEN
  user_message := 'Паролі не співпадають!';
WHEN VALUE_ERROR THEN
  user_message := 'Введено неправильні дані! Перевірте довжину паролю.';
WHEN others THEN
  user_message := 'Сталася непередбачувана помилка!';
END change_pass; 
  
  
PROCEDURE change_email(
    ident     IN USERS_T.user_id%TYPE,
    new_email IN USERS_T.user_email%TYPE,
    user_message OUT NVARCHAR2)
IS
no_user_ex EXCEPTION;
BEGIN
  IF ident = -1 THEN
  RAISE no_user_ex;
  END IF;
  
  UPDATE USERS_T
  SET USERS_T.user_email= new_email
  WHERE USERS_T.user_id = ident;
  user_message := 'E-mail успішно змінено';
EXCEPTION
WHEN no_user_ex THEN
  user_message := 'Такого користувача не існує!';
WHEN VALUE_ERROR THEN
  user_message := 'Введено неправильні дані! Перевірте коректність пошти.';
WHEN others THEN
  user_message := 'Сталася непередбачувана помилка!';
END change_email;
  
END authorisation_p;

/
/*REGISTRATION logic*/

/* AUTHORISATION AND REGISTRATION TRIGER. PASS MUST BE 4+ characters long and email must contain @ */
CREATE OR REPLACE TRIGGER check_user
BEFORE INSERT OR UPDATE
ON USERS_T
FOR EACH ROW
BEGIN
IF (LENGTH(:NEW.user_pass) <4) THEN
RAISE VALUE_ERROR;
END IF;
IF (:NEW.user_email NOT LIKE '%@%') THEN
RAISE VALUE_ERROR;
END IF;
END;

/

/* Actual registration */

/*PACKAGE FOR REGISTRATION (DECLARATION)*/
CREATE OR REPLACE PACKAGE registration_p
AS
  u_id USERS_T.user_id%TYPE;
  PROCEDURE register_user(
      u_login IN USERS_T.user_login%TYPE,
      u_email IN USERS_T.user_email%TYPE,
      u_pass1 IN USERS_T.user_pass%TYPE,
      u_pass2 IN USERS_T.user_pass%TYPE,
      counter_unique OUT NUMBER,
      user_message OUT NVARCHAR2);
END registration_p;
/

/*PACKAGE FOR REGISTRATION (BODY)*/
CREATE OR REPLACE PACKAGE BODY registration_p
AS
  PROCEDURE register_user(
      u_login IN USERS_T.user_login%TYPE,
      u_email IN USERS_T.user_email%TYPE,
      u_pass1 IN USERS_T.user_pass%TYPE,
      u_pass2 IN USERS_T.user_pass%TYPE,
      counter_unique OUT NUMBER,
      user_message OUT NVARCHAR2)
  IS
    ambigous_ex EXCEPTION;
    is_null_ex EXCEPTION;
    not_same_passes EXCEPTION;
  BEGIN
    SELECT COUNT(*)
    INTO counter_unique
    FROM USERS_T
    WHERE USERS_T.user_login = u_login
    OR USERS_T.user_email    = u_email;
    
    IF counter_unique        > 0 THEN
      RAISE ambigous_ex;
    END IF;
    
    IF (u_login is null) OR (u_email is null) OR (u_pass1 is null) OR (u_pass2 is null) THEN
      RAISE is_null_ex;
    END IF;    
    
    SELECT (MAX(USERS_T.user_id)+1) INTO u_id FROM USERS_T ;
    IF (u_pass1 != u_pass2) THEN
      RAISE not_same_passes;
    END IF;
    INSERT INTO USERS_T VALUES
      (u_id,u_login,u_email,u_pass1
      );
    user_message := 'Користувач усішно зареєстрований';
  EXCEPTION
  WHEN ambigous_ex THEN
    user_message := 'Користувач з таким логіном чи e-mail вже зареєстрований!';
  WHEN is_null_ex THEN
    user_message := 'Одне з обов`язкових полів не заповнено!';
  WHEN VALUE_ERROR THEN
    user_message := 'Введено невірні дані. Перевірте довжину паролю та коректність e-mail';
  WHEN not_same_passes THEN
    user_message := 'Паролі не співпадають!';  
  WHEN others THEN
    user_message := 'Сталася непередбачувана помилка!';
  END register_user;
  
END registration_p;


/