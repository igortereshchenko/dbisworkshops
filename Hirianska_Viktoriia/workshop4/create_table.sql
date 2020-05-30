CREATE TABLE U_USER(
    id NUMBER(3) NOT NULL,
    user_username VARCHAR2(50) NOT NULL,
    CONSTRAINT pk_id_user PRIMARY KEY (id),
    CONSTRAINT username_unique UNIQUE (user_username)
);

CREATE TABLE SERIES( 
    id NUMBER(3) NOT NULL,
    series_title VARCHAR2(128) NOT NULL, 
    series_genre VARCHAR2(128) NOT NULL, 
    series_year NUMBER(4) NOT NULL, 
    series_country VARCHAR2(128) NOT NULL, 
    series_amountofseasons NUMBER(2) NOT NULL, 
    series_duration NUMBER(3) NOT NULL, 
    series_description VARCHAR2(512) NOT NULL,
    CONSTRAINT pk_id_series PRIMARY KEY (id),
    CONSTRAINT title_unique UNIQUE (series_title),
	CONSTRAINT check_series_year CHECK(series_year<=2020),
	CONSTRAINT check_series_years CHECK(series_year>=1985)
);

CREATE TABLE GRADE(
    id NUMBER(2) NOT NULL,
    grade_value NUMBER(2),
    user_id NUMBER(2) NOT NULL,
    series_id NUMBER(2) NOT NULL,
    reviw VARCHAR2(200) NOT NULL,
    CONSTRAINT pk_id_grade PRIMARY KEY (id),
    CONSTRAINT fk_id_user FOREIGN KEY(user_id) REFERENCES U_USER(id),
    CONSTRAINT fk_id_series FOREIGN KEY(series_id) REFERENCES SERIES(id),
    CONSTRAINT check_grade_value CHECK(grade_value<=10)
);