-- date format
ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY MM DD';

-- users autoincrement
CREATE SEQUENCE users_id START WITH 1;

CREATE OR REPLACE TRIGGER users_id_ai
BEFORE INSERT ON users
FOR EACH ROW

BEGIN
  SELECT users_id.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;

-- config autoincrement
CREATE SEQUENCE users_config_id START WITH 1;

CREATE OR REPLACE TRIGGER users_config_id_ai
BEFORE INSERT ON user_config
FOR EACH ROW

BEGIN
  SELECT users_config_id.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;

-- items autoincrement
CREATE SEQUENCE users_item_id START WITH 1;

CREATE OR REPLACE TRIGGER users_item_id_ai
BEFORE INSERT ON user_items
FOR EACH ROW

BEGIN
  SELECT users_item_id.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;


-- actions autoincrement
CREATE SEQUENCE users_action_id START WITH 1;

CREATE OR REPLACE TRIGGER users_actions_id_ai
BEFORE INSERT ON user_actions
FOR EACH ROW

BEGIN
  SELECT users_action_id.NEXTVAL
  INTO   :new.id
  FROM   dual;
END;