create table services(
    service_name VARCHAR2(100) NOT NULL,
    price NUMBER(8,2) NOT NULL,  
    CONSTRAINT service_constraint PRIMARY KEY (service_name, price),
    CONSTRAINT check_price CHECK (price >= 0)
);

create table driver(
    driver_id INTEGER NOT NULL PRIMARY KEY,
    email VARCHAR2(50) NOT NULL UNIQUE,
    first_name VARCHAR2(100) NOT NULL, 
    second_name VARCHAR2(100),  
    user_login VARCHAR2(40) NOT NULL UNIQUE,
    user_password VARCHAR2(50) NOT NULL,
    birthday DATE,
    telephone VARCHAR2(30) NOT NULL UNIQUE,
    CONSTRAINT email_check CHECK (REGEXP_LIKE (email, '^(\S+)\@(\S+)\.(\S+)$')),
    CONSTRAINT valid_phone_number CHECK (REGEXP_LIKE(telephone, '^0\d{9}|\d{10}$'))
);


create table car(
    driver_id INTEGER,
    car_license_plate VARCHAR2(30),
    car_name VARCHAR2(100) NOT NULL, 
    car_type VARCHAR2(40) NOT NULL,
    car_color VARCHAR2(20),
    CONSTRAINT dr_car_constraint FOREIGN KEY(driver_id) REFERENCES driver(driver_id),
    CONSTRAINT car_constraint PRIMARY KEY (driver_id, car_license_plate)
);

create table wish(
    service_name VARCHAR2(100) NOT NULL,
    price NUMBER(8,2) NOT NULL,
    when_date TIMESTAMP(0) NOT NULL, 
    type_of_car VARCHAR2(100) NOT NULL,
    driver_id INTEGER NOT NULL,
    CONSTRAINT wish_constraint PRIMARY KEY (when_date),
    CONSTRAINT check_price_2 CHECK (price >= 70)
);

ALTER TABLE wish ADD CONSTRAINT wish_fk_constraint1 FOREIGN KEY (driver_id) REFERENCES driver (driver_id);
ALTER TABLE car ADD CONSTRAINT car_fk_constraint FOREIGN KEY (driver_id) REFERENCES driver(driver_id);

CREATE OR REPLACE TRIGGER check_service_name
BEFORE UPDATE OF service_name ON services
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN

select regexp_replace(:new.service_name, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong service_name format in update!'); -- if new service_name value contains numbers, we don't update it
END IF;
END;
/

CREATE OR REPLACE TRIGGER check_service_name_insert
BEFORE INSERT ON services
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN
select regexp_replace(:new.service_name, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong service name format in insert!');
END IF;
END;
/

CREATE OR REPLACE TRIGGER check_first_name_update
BEFORE UPDATE of first_name ON driver
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN
select regexp_replace(:new.first_name, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong first name format in update!');
END IF;
END;
/

CREATE OR REPLACE TRIGGER check_first_name_insert
BEFORE INSERT ON driver
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN
select regexp_replace(:new.first_name, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong first name format in insert!');
END IF;
END;
/

-----------------------------
CREATE OR REPLACE TRIGGER check_second_name_update
BEFORE UPDATE of second_name ON driver
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN
select regexp_replace(:new.second_name, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong second name format in update!');
END IF;
END;
/

CREATE OR REPLACE TRIGGER check_second_name_insert
BEFORE INSERT ON driver
FOR EACH ROW
DECLARE
str VARCHAR2(20);
BEGIN
select regexp_replace(:new.second_name, '[[:alpha:]]|_') into str from dual;
IF str is not null then
    raise_application_error(-20000, 'Wrong second name format in insert!');
END IF;
END;
/

CREATE OR REPLACE TRIGGER price_for_different_type
    BEFORE INSERT
    ON wish
    FOR EACH ROW
BEGIN
    IF :new.type_of_car = 'crossover'
    THEN
        :new.price := :new.price + 50;
    ELSIF :new.type_of_car = 'truck'
    THEN 
        :new.price := :new.price + 100;
    END IF;
END;
--INSERT INTO services (service_name, price) VALUES ('Interior Vacuum', 100);
--INSERT INTO driver (driver_id, email, first_name, second_name, user_login, USER_PASSWORD, BIRTDAY, TELEPHONE) VALUES (1, 'boroznuk@gmail.com', 'Dmytro', 'Borozniuk', 'admin', 'admin123', SYSDATE, '0638785961');
--INSERT INTO car (DRIVER_ID, CAR_LICENSE_PLATE, car_name, car_type, car_color) VALUES (2, 'AI3697AI', 'Subaru Forester', 'crossover', 'silver');
--ALTER TABLE driver RENAME COLUMN birtday TO birthday;

create or replace package user_auth is
    
    function get_driver_id(login driver.user_login%type, pass driver.user_password%type)
    return integer;
    
    function is_user(login driver.user_login%type, pass driver.user_password%type)
    return integer;
    function get_driver_username(idd driver.driver_id%type)
    return varchar2;
   
end user_auth;
/

create or replace package body user_auth is
    
    function is_user(login  driver.user_login%type, pass driver.user_password%type)
    return integer
    is
        counter INTEGER;
    begin
        select count(*) into counter from driver
            where 
                trim(driver.user_login)=trim(login)
                and
                trim(driver.user_password)=trim(pass);
        return counter;        
    end is_user;
    
    function get_driver_id(login driver.user_login%type, pass driver.user_password%type)
    return integer
    is
        user_id  integer;
    begin
        if is_user(login, pass)>0 then
            
            select driver.driver_id into user_id from driver
            where 
                trim(driver.user_login)=trim(login)
                and
                trim(driver.user_password)=trim(pass);
                
            return user_id;
        end if;
        return 0;
    end get_driver_id;
        
    function get_driver_username(idd driver.driver_id%type)
    return varchar2
    is
        user_name  varchar2(30);
    begin  
            select driver.user_login into user_name from driver
            where 
                trim(driver.driver_id)=trim(idd);
                
            return user_name;
    end get_driver_username;
    
    
end user_auth;
/
create or replace function date_is_taken_by_someone(datee WISH.WHEN_DATE%type)
return number
is
    countt  number;
begin  
        select count(wish.when_date) into countt from wish
        where 
            trim(wish.when_date)=TO_TIMESTAMP(datee);        
        return countt;
end date_is_taken_by_someone;
/ 



create or replace function get_service_price(nameee services.service_name%type)
return number
is
    pricee  number;
begin  
        select services.price into pricee from services
        where 
            trim(services.service_name)=trim(nameee);        
        return pricee;
end get_service_price;
/ 


create or replace function give_sale(idd WISH.DRIVER_ID%type)
return integer
is
    countt  integer;
begin  
        select count(WISH.DRIVER_ID) into countt from wish
        where 
            WISH.DRIVER_ID=idd;        
        return countt;
end give_sale;

CREATE OR REPLACE FUNCTION find_service_name(
      name_pattern IN services.service_name%TYPE)
    RETURN VARCHAR2
  IS
    idents VARCHAR2(100);
  BEGIN
    SELECT services.service_name INTO idents
    FROM services
    WHERE LOWER(TRIM(services.service_name)) LIKE ('%'
      || LOWER(TRIM(name_pattern))
      || '%');
    RETURN idents;
END find_service_name;
/

create or replace FUNCTION difference_between_dates(
      dateee IN wish.when_date%TYPE)
    RETURN VARCHAR2
  IS
    date_diff VARCHAR2(100);
  BEGIN
    date_diff:= SUBSTR((dateee - CURRENT_DATE),1,30);
    
    RETURN date_diff;
END difference_between_dates;


INSERT INTO services (service_name, price) VALUES ('Interior Vacuum', 400);
INSERT INTO services (service_name, price) VALUES ('Windows Cleaned', 180);
INSERT INTO services (service_name, price) VALUES ('Wet cleaning of panels', 300);
INSERT INTO services (service_name, price) VALUES ('Mat washing and drying', 140);
INSERT INTO services (service_name, price) VALUES ('Body protection', 600);
INSERT INTO services (service_name, price) VALUES ('Quick washing', 200);
INSERT INTO services (service_name, price) VALUES ('Undercarriage wash', 500);
INSERT INTO services (service_name, price) VALUES ('Perfect gloss inside and outside', 800);
INSERT INTO services (service_name, price) VALUES ('Protector wax', 550);
INSERT INTO services (service_name, price) VALUES ('Discs washing ', 200);

INSERT INTO driver (driver_id, email, first_name, second_name, user_login, USER_PASSWORD, BIRTDAY, TELEPHONE) VALUES (4, 'grigorova2000@gmail.com', 'Dasha', 'Grigorova', 'grigorovadasha20', 'dashadasha', '04-MAR-00', '0992342345');
INSERT INTO driver (driver_id, email, first_name, second_name, user_login, USER_PASSWORD, BIRTDAY, TELEPHONE) VALUES (3, 'artemb@gmail.com', 'Artem', 'Boyko', 'artemb5454', 'artemartem54', '29-OCT-99', '0634567732');
INSERT INTO driver (driver_id, email, first_name, second_name, user_login, USER_PASSWORD, BIRTDAY, TELEPHONE) VALUES (2, 'pasha123@gmail.com', 'Pasha', 'Boyko', 'pasha123', 'pashapasha123', '06-AUG-99', '0668912266');
INSERT INTO driver (driver_id, email, first_name, second_name, user_login, USER_PASSWORD, BIRTDAY, TELEPHONE) VALUES (1, 'boroznuk@gmail.com', 'Dmytro', 'Borozniuk', 'admin', 'admin123', '20-AUG-99', '0638785961');

INSERT INTO car (DRIVER_ID, CAR_LICENSE_PLATE, car_name, car_type, car_color) VALUES (2, 'AI3697AI', 'Subaru Forester', 'crossover', 'silver');
INSERT INTO car (DRIVER_ID, CAR_LICENSE_PLATE, car_name, car_type, car_color) VALUES (1, 'AA7766AA', 'BMW X5', 'crossover', 'black');
INSERT INTO car (DRIVER_ID, CAR_LICENSE_PLATE, car_name, car_type, car_color) VALUES (3, 'AC2233AI', 'Toyota Camry', 'sedan', 'black');
INSERT INTO car (DRIVER_ID, CAR_LICENSE_PLATE, car_name, car_type, car_color) VALUES (4, 'AA3459CC', 'Mazda 3', 'sedan', 'white');

insert into wish (service_name, price, when_date, type_of_car,  driver_id) values ('Interior Vacuum', 450, '29-MAY-20 07.20.00.000000000 PM', 'crossover', 1);


SET TRANSACTION ISOLATION LEVEL READ COMMITTED;


--alter table wish
--add (driver_id integer not null);

--alter table
-- wish
--modify
--(
--   when_date    Timestamp(0)
--);
--insert into wish (service_name, price, when_date, type_of_car,  driver_id) values ('Interior Vacuum', 100, SYSDATE, 'crossover', 1);