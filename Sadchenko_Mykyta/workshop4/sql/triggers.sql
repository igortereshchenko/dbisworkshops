
/* User table validation */
CREATE SEQUENCE pk_user_seq
    MINVALUE 1
    START WITH 1
    INCREMENT BY 1
    CACHE 20;

CREATE OR REPLACE TRIGGER user_trigg 
BEFORE INSERT ON User
FOR EACH ROW
WHEN ( new.id IS NULL )
BEGIN
    :new.id := pk_user_seq.nextval;
    IF (LENGTH(:new.username) > 30)
    THEN 
        raise_application_error(-20001,'Username length must be less than 30');
    END IF;
    IF :new.email NOT LIKE '%@%.%'
    THEN
        raise_application_error(-20002,'Email is not valid');
    END IF;
    IF (LENGTH(:new.username) > 50)
    THEN 
        raise_application_error(-20003,'Password length must be less than 50');
    END IF;
END;
/

/* Note table validation */
CREATE SEQUENCE pk_note_seq
    MINVALUE 1
    START WITH 1
    INCREMENT BY 1
    CACHE 20;

CREATE OR REPLACE TRIGGER note_trigg
BEFORE INSERT ON Note
FOR EACH ROW
WHEN ( new.id IS NULL )
BEGIN
    :new.id := pk_note_seq.nextval;
    IF (:new.url_id NOT IN (SELECT url_id
                    FROM Note
                    WHERE url_id = :new.url_id))
    THEN 
        raise_application_error(-20005, 'url_id already exist');
    END IF;
    IF (LENGTH(:new.url_id) != 9)
    THEN 
        raise_application_error(-20006, 'url_id length must be equal to 9');
    END IF;
    IF (LENGTH(:new.title) > 100)
    THEN 
        raise_application_error(-20008, 'Title length must be less than 100');
    END IF;
END;
/

/* UserNoteParams table validation */
CREATE SEQUENCE pk_params_seq
    MINVALUE 1
    START WITH 1
    INCREMENT BY 1
    CACHE 20;

CREATE OR REPLACE TRIGGER params_trigg 
BEFORE INSERT ON UserNoteParams
FOR EACH ROW
WHEN ( new.id IS NULL )
BEGIN
    :new.id := pk_params_seq.nextval;
    IF (:new.note_id NOT IN (SELECT id
                            FROM Note
                            WHERE id = :new.note_id))
    THEN 
        raise_application_error(-20012, 'Note does not exist');
    END IF;
    IF (:new.user_id NOT IN (SELECT id
                            FROM User
                            WHERE id = :new.user_id))
    THEN 
        raise_application_error(-20013, 'User does not exist');
    END IF;
    IF (:new.change_possibility NOT IN ('T', 'F'))
    THEN 
        raise_application_error(-20009, 'change_possibility equal to "T" or "F"');
    END IF;
    IF (:new.private_access NOT IN ('T', 'F'))
    THEN 
        raise_application_error(-20010, 'private_access equal to "T" or "F"');
    END IF;
    IF (:new.encryption NOT IN ('T', 'F'))
    THEN 
        raise_application_error(-20011, 'encryption equal to "T" or "F"');
    END IF;
END;
/

/* PrivateAccess table validation */
CREATE SEQUENCE pk_access_seq
    MINVALUE 1
    START WITH 1
    INCREMENT BY 1
    CACHE 20;

CREATE OR REPLACE TRIGGER access_trigg 
BEFORE INSERT ON PrivateAccess
FOR EACH ROW
WHEN ( new.id IS NULL )
BEGIN
    :new.id := pk_params_seq.nextval;
    IF (:new.note_id NOT IN (SELECT id
                            FROM Note
                            WHERE id = :new.note_id))
    THEN 
        raise_application_error(-20012, 'Note does not exist');
    END IF;
    IF (:new.user_id NOT IN (SELECT id
                            FROM User
                            WHERE id = :new.user_id))
    THEN 
        raise_application_error(-20013, 'User does not exist');
    END IF;
END;
/

