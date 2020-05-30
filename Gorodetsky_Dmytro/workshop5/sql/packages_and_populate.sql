INSERT INTO BOOKS VALUES(1, 'Harry Potter1', 'J.K Rowling', 10, 'Fantasy', 3, 'Nice book', 'Machaon', 233);
INSERT INTO BOOKS VALUES(2, 'Harry Potter2', 'J.K Rowling', 12, 'Scince', 2, 'Nice book', 'Rosman', 4234);
INSERT INTO BOOKS VALUES(3, 'Harry Potter3', 'J.K Rowling', 23, 'Horror', 13, 'Nice book', 'Rosman', 543);
INSERT INTO BOOKS VALUES(4, 'Harry Potter4', 'J.K Rowling', 42, 'Fantasy', 878, 'Nice book', 'Machaon', 346);
INSERT INTO BOOKS VALUES(5, 'Harry Potter5', 'J.K Rowling', 12, 'Horror', 45, 'Nice book', 'Machaon', 567);
INSERT INTO BOOKS VALUES(6, 'Harry Potter6', 'J.K Rowling', 32, 'Scince', 170, 'Nice book', 'Machaon', 57);
INSERT INTO BOOKS VALUES(7, 'Harry Potter7', 'J.K Rowling', 45, 'Fantasy', 89, 'Nice book', 'Rosman', 67);
INSERT INTO BOOKS VALUES(8, 'Harry Potter8', 'J.K Rowling', 65, 'Fantasy', 7, 'Nice book', 'Machaon', 789);
INSERT INTO BOOKS VALUES(9, 'Harry Potter9', 'J.K Rowling', 86, 'Horror', 56, 'Nice book', 'Rosman', 89);
INSERT INTO BOOKS VALUES(10, 'Harry Potter10', 'J.K Rowling', 22, 'Fantasy', 4, 'Nice book', 'Machaon', 45);
INSERT INTO BOOKS VALUES(11, 'Harry Potter11', 'J.K Rowling', 43, 'Horror', 23, 'Nice book', 'Machaon', 75);
INSERT INTO BOOKS VALUES(12, 'Harry Potter12', 'J.K Rowling', 12, 'Fantasy', 5, 'Nice book', 'Machaon', 678);
INSERT INTO BOOKS VALUES(13, 'Harry Potter13', 'J.K Rowling', 52, 'Scince', 23, 'Nice book', 'Rosman', 45);
INSERT INTO BOOKS VALUES(14, 'Harry Potter14', 'J.K Rowling', 4, 'Horror', 56, 'Nice book', 'Machaon', 34);
INSERT INTO BOOKS VALUES(15, 'Harry Potter15', 'J.K Rowling', 1, 'Fantasy', 96, 'Nice book', 'Machaon', 44);
INSERT INTO BOOKS VALUES(16, 'Harry Potter16', 'J.K Rowling', 23, 'Horror', 345, 'Nice book', 'Rosman', 234);
INSERT INTO BOOKS VALUES(17, 'Harry Potter17', 'J.K Rowling', 124, 'Scince', 87, 'Nice book', 'Rosman', 865);
INSERT INTO BOOKS VALUES(18, 'Harry Potter18', 'J.K Rowling', 24, 'Horror', 4, 'Nice book', 'Machaon', 456);
INSERT INTO BOOKS VALUES(19, 'Harry Potter19', 'J.K Rowling', 2, 'Fantasy', 23, 'Nice book', 'Machaon', 865);
INSERT INTO BOOKS VALUES(20, 'Harry Potter20', 'J.K Rowling', 3, 'Fantasy', 99, 'Nice book', 'Machaon', 567);


INSERT INTO CUSTOMERS VALUES(1, 'Bob', 'Bobovitch', 'bob228@gmail.com', 'sven', 'sven');
INSERT INTO CUSTOMERS VALUES(2, 'Boba', 'Bobenko', 'boba1488@gmail.com', 'lina', 'lina');
INSERT INTO CUSTOMERS VALUES(3, 'Boban', 'Bobengaven', 'boban228@gmail.com', 'spirit', 'spirit');
INSERT INTO CUSTOMERS VALUES(4, 'David', 'Muler', 'dave228@gmail.com', 'zeus', 'zeus');
INSERT INTO CUSTOMERS VALUES(5, 'Kostya', 'Bobs', 'kostya228@gmail.com', 'mirana', 'mirana');



/
CREATE OR REPLACE PACKAGE authorisation_p
AS
  FUNCTION get_username(
      ident IN customers.customer_id%TYPE)
    RETURN customers.user_login%TYPE;
    
  FUNCTION authorisation(
      user_login IN customers.user_login%TYPE,
      pass           IN customers.user_password%TYPE)
    RETURN customers.customer_id%TYPE;
  END authorisation_p;


/
CREATE OR REPLACE PACKAGE BODY authorisation_p
AS
  FUNCTION authorisation(
      user_login IN customers.user_login%TYPE,
      pass           IN customers.user_password%TYPE)
    RETURN customers.customer_id%TYPE
  IS
    ident customers.customer_id%TYPE;
  BEGIN
    SELECT customers.customer_id
    INTO ident
    FROM customers
    WHERE (customers.user_login = user_login
    OR customers.email     = user_login)
    AND customers.user_password     = pass;
    RETURN ident;
  EXCEPTION
  WHEN OTHERS THEN
    ident := -1;
    RETURN ident;
  END authorisation;

  /* SELECT USERNAME BY ID. USE WHEN AUTHORISATION COMPLETED AND ID IS RETURNED */
  FUNCTION get_username(
      ident IN customers.customer_id%TYPE)
    RETURN customers.user_login%TYPE
  IS
    login customers.user_login%TYPE;
  BEGIN
    IF(ident = -1) THEN
      RETURN 'Invalid login or password';
    END IF;
    SELECT customers.user_login
    INTO login
    FROM customers
    WHERE customers.customer_id = ident;
    RETURN login;
  END get_username;

  
END authorisation_p;

/
 
 
 /*PACKAGE FOR REGISTRATION (DECLARATION)*/
CREATE OR REPLACE PACKAGE registration_p
AS
  u_id customers.customer_id%TYPE;
  PROCEDURE register_user(
      first_name IN Customers.first_name%TYPE,
      second_name IN Customers.second_name%TYPE,
      login IN Customers.user_login%TYPE,
      email IN Customers.email%TYPE,
      pass1 IN Customers.user_password%TYPE,
      pass2 IN Customers.user_password%TYPE,
      counter_unique OUT NUMBER,
      user_message OUT NVARCHAR2);
END registration_p;
/

/*PACKAGE FOR REGISTRATION (BODY)*/
CREATE OR REPLACE PACKAGE BODY registration_p
AS
  PROCEDURE register_user(
      first_name IN Customers.first_name%TYPE,
      second_name IN Customers.second_name%TYPE,
      login IN customers.user_login%TYPE,
      email IN customers.email%TYPE,
      pass1 IN customers.user_password%TYPE,
      pass2 IN customers.user_password%TYPE,
      counter_unique OUT NUMBER,
      user_message OUT NVARCHAR2)
  IS
    ambigous_ex EXCEPTION;
    is_null_ex EXCEPTION;
    not_same_passes EXCEPTION;
  BEGIN
    SELECT COUNT(*)
    INTO counter_unique
    FROM customers
    WHERE customers.user_login = login;
    
    IF counter_unique        > 0 THEN
      RAISE ambigous_ex;
    END IF;
    
    IF (login is null) OR (email is null) OR (pass1 is null) OR (pass2 is null) THEN
      RAISE is_null_ex;
    END IF;    
    
    SELECT (MAX(customers.customer_id)+1) INTO u_id FROM customers ;
    IF (pass1 != pass2) THEN
      RAISE not_same_passes;
    END IF;
    INSERT INTO customers VALUES
      (u_id, first_name, second_name, login, email, pass1
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

commit;