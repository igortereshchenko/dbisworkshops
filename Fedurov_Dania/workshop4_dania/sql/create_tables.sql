create table user_database (
    id_user INTEGER NOT NULL,
    user_name VARCHAR2(100) NOT NULL,
    user_surname VARCHAR2(100) NOT NULL, 
    user_age INTEGER NOT NULL,
    user_mail VARCHAR2(100) NOT NULL,
    user_login VARCHAR2(100) NOT NULL,
    user_pass VARCHAR2(100) NOT NULL,
  constraint user_database_pk primary key (id_user)
);

create table  prediction_database (
    id_pred INTEGER NOT NULL,
    prediction_description VARCHAR2(500) NOT NULL,
    constraint prediction_database_pk  PRIMARY KEY (id_pred)
);

create table  numerology_database (
    id_nume INTEGER NOT NULL,
    numerology_date DATE NOT NULL,
    numerology_description VARCHAR2(500) NOT NULL,
    constraint numerology_database_pk  PRIMARY KEY (id_nume)
);