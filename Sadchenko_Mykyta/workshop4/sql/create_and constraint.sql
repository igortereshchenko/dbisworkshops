CREATE TABLE USER (
    user_id NUMBER(10),
    username VARCHAR2(30),
    email VARCHAR2(50),
    password VARCHAR2(40)
);

CREATE TABLE NOTE (
    note_id NUMBER(20),
    url_id VARCHAR2(30),
    title VARCHAR2(50),
    text LONG,
    created DATE,
    updated DATE
);

CREATE TABLE USER_NOTE_PARAMS (
    params_id NUMBER(20),
    change_possibility CHAR(1),
    private_access CHAR(1),
    encryption CHAR(1),
    note_id NUMBER,
    user_id NUMBER
);

CREATE TABLE PRIVATE_ACCESS (
    access_id NUMBER(20),
    note_id NUMBER(20),
    user_id NUMBER(10)
);



ALTER TABLE USER
    ADD CONSTRAINT username_not_null CHECK(username is NOT NULL);
ALTER TABLE USER
    ADD CONSTRAINT password_not_null CHECK(password is NOT NULL);
ALTER TABLE NOTE
    ADD CONSTRAINT url_id_not_null CHECK(url_id is NOT NULL);
ALTER TABLE NOTE
    ADD CONSTRAINT created_not_null CHECK(created_id is NOT NULL);


ALTER TABLE USER
    ADD CONSTRAINT user_pk PRIMARY KEY (user_id);
ALTER TABLE NOTE
    ADD CONSTRAINT note_pk PRIMARY KEY (note_id);
ALTER TABLE USER_NOTE_PARAMS
    ADD CONSTRAINT params_pk PRIMARY KEY (params_id);
ALTER TABLE PRIVATE_ACCESS
    ADD CONSTRAINT access_pk PRIMARY KEY (access_id);


ALTER TABLE USER_NOTE_PARAMS
    ADD CONSTRAINT params_user_fk
        FOREIGN KEY (user_id) REFERENCES USER(user_id);
ALTER TABLE USER_NOTE_PARAMS
    ADD CONSTRAINT params_note_fk
        FOREIGN KEY (note_id) REFERENCES NOTE(note_id);
ALTER TABLE PRIVATE_ACCESS
    ADD CONSTRAINT access_user_fk
        FOREIGN KEY (user_id) REFERENCES USER(user_id);
ALTER TABLE PRIVATE_ACCESS
    ADD CONSTRAINT access_note_fk
        FOREIGN KEY (note_id) REFERENCES NOTE(note_id);

