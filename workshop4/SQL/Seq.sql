DROP SEQUENCE DBPROJECT.HIKES_SEQ;

CREATE SEQUENCE DBPROJECT.HIKES_SEQ
  START WITH 21
  MAXVALUE 999999999999999999999999999
  MINVALUE 1
  NOCYCLE
  CACHE 20
  NOORDER;

DROP SEQUENCE DBPROJECT.ORDERS_SEQ;

CREATE SEQUENCE DBPROJECT.ORDERS_SEQ
  START WITH 25
  MAXVALUE 999999999999999999999999999
  MINVALUE 1
  NOCYCLE
  CACHE 20
  NOORDER;

DROP SEQUENCE DBPROJECT.SENTENCES_SEQ;

CREATE SEQUENCE DBPROJECT.SENTENCES_SEQ
  START WITH 45
  MAXVALUE 999999999999999999999999999
  MINVALUE 1
  NOCYCLE
  CACHE 20
  NOORDER;

DROP SEQUENCE DBPROJECT.USERS_SEQ;

CREATE SEQUENCE DBPROJECT.USERS_SEQ
  START WITH 47
  MAXVALUE 9999999999999999999999999999
  MINVALUE 5
  NOCYCLE
  NOCACHE
  NOORDER;