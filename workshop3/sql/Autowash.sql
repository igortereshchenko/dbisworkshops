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
    when_date DATE NOT NULL UNIQUE, 
    type_of_car VARCHAR2(100) NOT NULL,
    CONSTRAINT wish_constraint PRIMARY KEY (service_name, price),
    CONSTRAINT check_price_2 CHECK (price >= 70)  
);

ALTER TABLE wish ADD CONSTRAINT wish_fk_constraint FOREIGN KEY (service_name, price) REFERENCES services (service_name, price);
   
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
SELECT CURRENT_DATE FROM dual;
INSERT INTO services (service_name, price) VALUES ('Windowwash', 70);
INSERT INTO services (service_name, price) VALUES ('Interior Vacuum', 100);
INSERT INTO wish (service_name, price, when_date, type_of_car) VALUES ('Windowwash', 70, SYSDATE, 'truck');
INSERT INTO driver (driver_id, email, first_name, second_name, user_login, USER_PASSWORD, BIRTDAY, TELEPHONE) VALUES (1, 'boroznuk@gmail.com', 'Dmytro', 'Borozniuk', 'admin', 'admin123', SYSDATE, '0638785961');
INSERT INTO car (DRIVER_ID, CAR_LICENSE_PLATE, car_name, car_type, car_color) VALUES (2, 'AI3697AI', 'Subaru Forester', 'crossover', 'silver');
ALTER TABLE driver RENAME COLUMN birtday TO birthday;
