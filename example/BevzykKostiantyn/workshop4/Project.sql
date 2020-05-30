create table users(
  user_id Integer Primary key,
  user_name VARCHAR2(50) NOT NULL UNIQUE,
  user_date date NOT NULL,
  age Integer,
  CONSTRAINT age_check CHECK (age>14)
);

create table resources(
  user_id Integer Primary  key,
  location_ VARCHAR2(50) NOT NULL,
  category_ VARCHAR2(50) NOT NULL,
  Constraint check_3 foreign key (user_id) references users(user_id)
);


AlTER TABLE resources ADD CONSTRAINT loc_check CHECK (length(location_)>0);

AlTER TABLE resources ADD CONSTRAINT category_ CHECK (length(category_)>0);



CREATE or Replace Trigger check_user_name
BEFORE UPDATE of user_name ON users
FOR EACH ROW
DECLARE
strin VARCHAR(50);
BEGIN
select regexp_replace(:new.user_name, '[[:alpha:]]|_') into strin from dual;
IF strin is not null then
    raise_application_error(-20000, 'Wrong user name format in update!');
END IF;
END;

CREATE or Replace Trigger check_loc
BEFORE UPDATE of location_ ON resources
FOR EACH ROW
DECLARE
strin VARCHAR(50);
BEGIN
select regexp_replace(:new.location_, '[[:alpha:]]|_') into strin from dual;
IF strin is not null then
    raise_application_error(-20000, 'Wrong user name format in update!');
END IF;
END;

Create or Replace Trigger check_category
BEFORE UPDATE of category_ ON resources
FOR EACH ROW
DECLARE
strin VARCHAR(50);
BEGIN
select regexp_replace(:new.category_, '[[:alpha:]]|_') into strin from dual;
IF strin is not null then
    raise_application_error(-20000, 'Wrong user name format in update!');
END IF;
END;
