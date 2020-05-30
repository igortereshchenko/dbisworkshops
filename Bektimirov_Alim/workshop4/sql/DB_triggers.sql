

create or replace function date_to_unix_ts( PDate in date ) return number is

   l_unix_ts number;

begin

   l_unix_ts := ( PDate - date '1970-01-01' ) * 60 * 60 * 24;
   return l_unix_ts;

end;


CREATE OR REPLACE TRIGGER film_date
BEFORE INSERT ON expected_film_list
FOR EACH ROW
DECLARE
    cur_date date;
    cur_date_unix integer;
    new_date integer := :new.release_date;
BEGIN
    SELECT CURRENT_DATE INTO cur_date FROM DUAL;
    cur_date_unix := DATE_TO_UNIX_TS(cur_date);
    IF new_date < cur_date_unix THEN
        raise_application_error(-20000,'The expected film cannot be already released.');
    END IF;
END;


CREATE OR REPLACE TRIGGER film_quantity
BEFORE INSERT ON expected_film_list
FOR EACH ROW
DECLARE
    film_quan integer;
    new_film_id expected_film_list.FILM_ID%TYPE := :new.FILM_ID;
BEGIN
    SELECT count(FILM_ID) INTO film_quan FROM expected_film_list WHERE FILM_ID = new_film_id;
    IF film_quan > 1000 THEN
        raise_application_error(-20001,'User can not add more then 1000 films.');
    END IF;
END;


CREATE OR REPLACE TRIGGER film_year
BEFORE INSERT ON expected_film_list
FOR EACH ROW
DECLARE
    new_date integer := :new.release_date;
BEGIN
    IF new_date < -315619200 THEN
        raise_application_error(-20002,'The year of release of the film cannot be earlier than 1960.');
    END IF;
END;



CREATE OR REPLACE TRIGGER film_quantity1
BEFORE INSERT ON liked_film_list
FOR EACH ROW
DECLARE
    film_quan integer;
    new_film_id expected_film_list.FILM_ID%TYPE := :new.FILM_ID;
BEGIN
    SELECT count(FILM_ID) INTO film_quan FROM expected_film_list WHERE FILM_ID = new_film_id;
    IF film_quan > 1000 THEN
        raise_application_error(-20001,'User can not add more then 1000 films.');
    END IF;
END;


CREATE OR REPLACE TRIGGER film_year1
BEFORE INSERT ON liked_film_list
FOR EACH ROW
DECLARE
    new_date integer := :new.release_date;
BEGIN
    IF new_date < -315619200 THEN
        raise_application_error(-20002,'The year of release of the film cannot be earlier than 1960.');
    END IF;
END;

CREATE OR REPLACE TRIGGER round_rating
BEFORE INSERT ON liked_film_list
FOR EACH ROW
DECLARE
    new integer := :new.rating;
BEGIN
    :new.rating := round(new,2);
END;

CREATE OR REPLACE TRIGGER round_rating1
BEFORE INSERT ON expected_film_list
FOR EACH ROW
DECLARE
    new integer := :new.rating;
BEGIN
    :new.rating := round(new,2);
END;