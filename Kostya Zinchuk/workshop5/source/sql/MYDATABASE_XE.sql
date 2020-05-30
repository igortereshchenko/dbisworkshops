CREATE TABLE book (
    book_id           NUMERIC(10) NOT NULL,
    book_name         VARCHAR2(50) NOT NULL,
    author_name       VARCHAR2(50) NOT NULL,
    author_lastname   VARCHAR2(50) NOT NULL,
    book_url          VARCHAR2(70) NOT NULL,
    CONSTRAINT book_pk PRIMARY KEY ( book_id ),
    CONSTRAINT check_id CHECK ( book_id > 0 )
);

CREATE TABLE l_user (
    user_name       VARCHAR2(50),
    user_lastname   VARCHAR2(50),
    email           VARCHAR2(50) NOT NULL PRIMARY KEY,
    registration    DATE NOT NULL,
    login           VARCHAR2(20) NOT NULL UNIQUE,
    password        VARCHAR2(30) NOT NULL,
    book_amount     NUMERIC,
    CONSTRAINT ba_ch CHECK ( book_amount >= 0 )
);

CREATE TABLE user_book (
    t_book_id    NUMERIC(10) NOT NULL,
    user_email   VARCHAR2(50) NOT NULL,
    CONSTRAINT ub_pk PRIMARY KEY ( t_book_id,
                                   user_email ),
    CONSTRAINT book_fk FOREIGN KEY ( t_book_id )
        REFERENCES book ( book_id ),
    CONSTRAINT user_fk FOREIGN KEY ( user_email )
        REFERENCES l_user ( email )
);

CREATE OR REPLACE TRIGGER check_author_name BEFORE
    UPDATE OF author_name ON book
    FOR EACH ROW
DECLARE
    tmp VARCHAR2(50);
BEGIN
    SELECT
        regexp_replace(:new.author_name, '[[:alpha:]]|_')
    INTO tmp
    FROM
        dual;

    IF tmp IS NOT NULL THEN
        raise_application_error(-20001, 'Author name cant be with digits');
    END IF;
END;
/

CREATE OR REPLACE TRIGGER check_author_name_insert BEFORE
    INSERT ON book
    FOR EACH ROW
DECLARE
    tmp VARCHAR2(50);
BEGIN
    SELECT
        regexp_replace(:new.author_name, '[[:alpha:]]|_')
    INTO tmp
    FROM
        dual;

    IF tmp IS NOT NULL THEN
        raise_application_error(-20002, 'Wrong Author name format. Can not be insert in book table');
    END IF;
END;
/

CREATE OR REPLACE TRIGGER check_author_lastname BEFORE
    UPDATE OF author_lastname ON book
    FOR EACH ROW
DECLARE
    tmp VARCHAR2(50);
BEGIN
    SELECT
        regexp_replace(:new.author_lastname, '[[:alpha:]]|_')
    INTO tmp
    FROM
        dual;

    IF tmp IS NOT NULL THEN
        raise_application_error(-20003, 'Author lastname cant be with digits');
    END IF;
END;
/

CREATE OR REPLACE TRIGGER check_author_lastname_insert BEFORE
    INSERT ON book
    FOR EACH ROW
DECLARE
    tmp VARCHAR2(50);
BEGIN
    SELECT
        regexp_replace(:new.author_lastname, '[[:alpha:]]|_')
    INTO tmp
    FROM
        dual;

    IF tmp IS NOT NULL THEN
        raise_application_error(-20004, 'Author lastname wrong format. Can not be insert');
    END IF;
END;
/

CREATE OR REPLACE TRIGGER check_user_name BEFORE
    UPDATE OF user_name ON l_user
    FOR EACH ROW
DECLARE
    tmp VARCHAR2(50);
BEGIN
    SELECT
        regexp_replace(:new.user_name, '[[:alpha:]]|_')
    INTO tmp
    FROM
        dual;

    IF tmp IS NOT NULL THEN
        raise_application_error(-20005, 'User name cant be with digits');
    END IF;
END;
/

CREATE OR REPLACE TRIGGER check_user_name_insert BEFORE
    INSERT ON l_user
    FOR EACH ROW
DECLARE
    tmp VARCHAR2(50);
BEGIN
    SELECT
        regexp_replace(:new.user_name, '[[:alpha:]]|_')
    INTO tmp
    FROM
        dual;

    IF tmp IS NOT NULL THEN
        raise_application_error(-20006, 'User name wrong format. Can not be insert');
    END IF;
END;
/

CREATE OR REPLACE TRIGGER check_user_lastname BEFORE
    UPDATE OF user_lastname ON l_user
    FOR EACH ROW
DECLARE
    tmp VARCHAR2(50);
BEGIN
    SELECT
        regexp_replace(:new.user_lastname, '[[:alpha:]]|_')
    INTO tmp
    FROM
        dual;

    IF tmp IS NOT NULL THEN
        raise_application_error(-20007, 'User name cant be with digits');
    END IF;
END;
/

CREATE OR REPLACE TRIGGER check_user_lastname_insert BEFORE
    INSERT ON l_user
    FOR EACH ROW
DECLARE
    tmp VARCHAR2(50);
BEGIN
    SELECT
        regexp_replace(:new.user_lastname, '[[:alpha:]]|_')
    INTO tmp
    FROM
        dual;

    IF tmp IS NOT NULL THEN
        raise_application_error(-20008, 'User lastname wrong format. Can not be insert');
    END IF;
END;
/

CREATE OR REPLACE TRIGGER check_email BEFORE
    UPDATE OF email ON l_user
    FOR EACH ROW
BEGIN
    IF :new.email NOT LIKE '%@%.%' THEN
        raise_application_error(-20009, 'Email format is invalid');
    END IF;
END;
/

CREATE OR REPLACE TRIGGER check_email_insert BEFORE
    INSERT ON l_user
    FOR EACH ROW
BEGIN
    IF :new.email NOT LIKE '%@%.%' THEN
        raise_application_error(-20009, 'Email format is invalid');
    END IF;
END;