CREATE SEQUENCE comments_sequence START WITH 1;

CREATE OR REPLACE TRIGGER comments_on_insert
      BEFORE INSERT ON comments
      FOR EACH ROW
BEGIN
      SELECT comments_sequence.nextval
      INTO :new.comment_id
      FROM dual;
END;

CREATE SEQUENCE portfolios_sequence START WITH 1;

CREATE OR REPLACE TRIGGER portfolios_on_insert
      BEFORE INSERT ON portfolios
      FOR EACH ROW
BEGIN
      SELECT portfolios_sequence.nextval
      INTO :new.portfolio_id
      FROM dual;
END;

CREATE SEQUENCE history_sequence START WITH 1;

CREATE OR REPLACE TRIGGER history_on_insert
      BEFORE INSERT ON history
      FOR EACH ROW
BEGIN
      SELECT history_sequence.nextval
      INTO :new.history_id
      FROM dual;
END;