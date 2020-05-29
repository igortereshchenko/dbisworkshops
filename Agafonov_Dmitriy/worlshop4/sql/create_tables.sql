create table user_table_sql (
    id INTEGER NOT NULL,
    user_name VARCHAR2(100) NOT NULL,
    user_mail VARCHAR2(100) NOT NULL,
    user_age INTEGER NOT NULL,
    edrpou VARCHAR2(100) NOT NULL,
    user_pass VARCHAR2(100) NOT NULL,
  constraint user_pk primary key (id)
);

create table  question_table_sql (
    question_id INTEGER NOT NULL,
    user_id INTEGER,
    question_reference VARCHAR2(20),
    question VARCHAR2(2000),
    time_creating TIMESTAMP(2) NOT NULL,
    status SMALLINT NOT NULL,
    constraint question_pk  PRIMARY KEY (question_id)
);