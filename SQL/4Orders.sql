ALTER TABLE DBPROJECT.ORDERS
 DROP PRIMARY KEY CASCADE;

DROP TABLE DBPROJECT.ORDERS CASCADE CONSTRAINTS;

CREATE TABLE DBPROJECT.ORDERS
(
  ORDER_ID        INTEGER,
  FK_USER_ID      INTEGER,
  FK_SENTENCE_ID  INTEGER,
  FK_HIKE_ID      INTEGER,
  GRADE           INTEGER,
  FK_FEATURE_ID   INTEGER
)
TABLESPACE USERS
RESULT_CACHE (MODE DEFAULT)
PCTUSED    0
PCTFREE    10
INITRANS   1
MAXTRANS   255
STORAGE    (
            INITIAL          64K
            NEXT             1M
            MAXSIZE          UNLIMITED
            MINEXTENTS       1
            MAXEXTENTS       UNLIMITED
            PCTINCREASE      0
            BUFFER_POOL      DEFAULT
            FLASH_CACHE      DEFAULT
            CELL_FLASH_CACHE DEFAULT
           )
LOGGING 
NOCOMPRESS 
NOCACHE
NOPARALLEL
MONITORING;


CREATE UNIQUE INDEX DBPROJECT.ORDERS_PK ON DBPROJECT.ORDERS
(ORDER_ID)
LOGGING
TABLESPACE USERS
PCTFREE    10
INITRANS   2
MAXTRANS   255
STORAGE    (
            INITIAL          64K
            NEXT             1M
            MAXSIZE          UNLIMITED
            MINEXTENTS       1
            MAXEXTENTS       UNLIMITED
            PCTINCREASE      0
            BUFFER_POOL      DEFAULT
            FLASH_CACHE      DEFAULT
            CELL_FLASH_CACHE DEFAULT
           )
NOPARALLEL;


CREATE OR REPLACE TRIGGER DBPROJECT.ORDERSSEQ
BEFORE INSERT
ON DBPROJECT.ORDERS
REFERENCING NEW AS New OLD AS Old
FOR EACH ROW
BEGIN
-- For Toad:  Highlight column ORDER_ID
  :new.ORDER_ID := ORDERS_SEQ.nextval;
END ORDERSSEQ;
/


ALTER TABLE DBPROJECT.ORDERS ADD (
  CONSTRAINT ORDERS_PK
  PRIMARY KEY
  (ORDER_ID)
  USING INDEX DBPROJECT.ORDERS_PK
  ENABLE VALIDATE);

ALTER TABLE DBPROJECT.ORDERS ADD (
  CONSTRAINT ORDER_USER_FK 
  FOREIGN KEY (FK_USER_ID) 
  REFERENCES DBPROJECT.USERS (USER_ID)
  ON DELETE SET NULL
  ENABLE VALIDATE,
  CONSTRAINT SENTENCES_FK 
  FOREIGN KEY (FK_SENTENCE_ID) 
  REFERENCES DBPROJECT.SENTENCES (SENTENCE_ID)
  ENABLE VALIDATE);
