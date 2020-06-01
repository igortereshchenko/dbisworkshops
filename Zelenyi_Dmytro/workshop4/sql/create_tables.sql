CREATE TABLE photographers(
    email VARCHAR2(30) NOT NULL,
    user_password VARCHAR2(30) NOT NULL,
    photographer_name VARCHAR2(30) NOT NULL,
    photographer_surname VARCHAR2(30),
    gender VARCHAR2(20) NOT NULL,
    about_photographer LONG NOT NULL,
    birthday DATE,
    experience INTEGER NOT NULL,
    region VARCHAR2(30) NOT NULL,
    city VARCHAR2(30) NOT NULL,
    is_premium CHAR(1) CHECK (is_premium IN ('N','Y')),
    
    CONSTRAINT photographer_pk PRIMARY KEY(email)
);

CREATE TABLE contacts(
    email VARCHAR2(30) NOT NULL,
    phone_number VARCHAR2(20),
    instagram VARCHAR2(50),
    facebook VARCHAR2(50),
    skype VARCHAR2(50),
    telegram VARCHAR2(50)
);

CREATE TABLE services(
    email VARCHAR2(30) NOT NULL,
    object_shooting FLOAT,
    portrait_shooting FLOAT,
    wedding_photo_shoot FLOAT,
    family_photo_shot FLOAT,
    event_photography FLOAT,
    reportage_shooting FLOAT,
    childrens_photo_shoot FLOAT,
    interior_shooting FLOAT,
    photosession_love_story FLOAT,
    pregnant_photoshoot FLOAT,
    neither FLOAT
);

CREATE TABLE comments(
    comment_id INTEGER NOT NULL,
    email_customer VARCHAR2(30) NOT NULL,
    email_photographer VARCHAR2(30) NOT NULL,
    comment_text LONG NOT NULL,
    
    CONSTRAINT comment_pk PRIMARY KEY(comment_id)
);

CREATE TABLE portfolios(
    portfolio_id INTEGER NOT NULL,
    author_email VARCHAR2(30) NOT NULL,
    img_src VARCHAR2(50) NOT NULL,
    
    CONSTRAINT portfolio_pk PRIMARY KEY(portfolio_id)
);

CREATE TABLE customers(
    email VARCHAR2(30) NOT NULL,
    user_password VARCHAR2(30) NOT NULL,
    customer_name VARCHAR2(30) NOT NULL,
    customer_surname VARCHAR2(30),
    
    CONSTRAINT customer_pk PRIMARY KEY(email)
);

CREATE TABLE history(
    history_id INTEGER NOT NULL,
    customer VARCHAR2(30) NOT NULL,
    photographer VARCHAR2(30) NOT NULL,
    
    CONSTRAINT history_pk PRIMARY KEY(history_id)
);

--DROP TABLE contacts;
--DROP TABLE services;
--DROP TABLE comments;
--DROP TABLE portfolios;
--DROP TABLE customers;
--DROP TABLE history;