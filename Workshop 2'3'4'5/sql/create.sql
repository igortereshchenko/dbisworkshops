SET TRANSACTION ISOLATION LEVEL READ COMMITTED;


CREATE OR REPLACE type id_array IS varray(10000) OF NUMBER;
/*CREATING TABLES*/

CREATE OR REPLACE type str_array IS varray(10000) OF NVARCHAR2(1000);


CREATE TABLE VENDORS_T(
vend_name nvarchar2(150) NOT NULL,
vend_edrpou NUMBER(8) NOT NULL,/*PK*/
vend_adress nvarchar2(200),
vend_city nvarchar2(100) NOT NULL,
telephone nvarchar2(20),
manager_name nvarchar2(100),
email nvarchar2(320)
);  

CREATE TABLE MATERIALS_T(
material_name nvarchar2(150) NOT NULL,
material_id number(8) NOT NULL/*PK*/
description nvarchar2(1000)
);


/

CREATE TABLE VEND_MAT_T( /*Допоміжна таблиця між вендорами та інформацією*/
material_id_fk number(8) NOT NULL,/*PK*/ /*FK*/
vend_edrpou_fk NUMBER(8) NOT NULL /*PK*/ /*FK*/
price NUMBER(8,2)
);



/

CREATE TABLE USERS_T(
user_id NUMBER(8) NOT NULL,/*PK*/
user_login nvarchar2(100) NOT NULL,
user_email nvarchar2(100) NOT NULL,
user_pass nvarchar2(100) NOT NULL
);
/

/*ADDING MAIN CONSTRAINTS*/

/
ALTER TABLE VENDORS_T
ADD CONSTRAINT primary_vend PRIMARY KEY(vend_edrpou);
/
ALTER TABLE VENDORS_T
ADD CONSTRAINT unique_name UNIQUE(vend_name);
/
ALTER TABLE VENDORS_T
ADD CONSTRAINT check_vendor CHECK(LENGTH(VEND_EDRPOU) = 8);
/
ALTER TABLE VENDORS_T
ADD CONSTRAINT check_vendor_ed_gr0 CHECK(VEND_EDRPOU > 0);
/
ALTER TABLE VENDORS_T
ADD CONSTRAINT name_not_semi_null CHECK(VEND_NAME != '');
/
ALTER TABLE VENDORS_T
ADD CONSTRAINT city_not_semi_null CHECK(VEND_CITY != '');
/
ALTER TABLE MATERIALS_T
ADD CONSTRAINT primary_material PRIMARY KEY(material_name);
/
ALTER TABLE MATERIALS_T
ADD CONSTRAINT unique_id_mat UNIQUE(material_id);
/
ALTER TABLE MATERIALS_T
ADD CONSTRAINT check_materials_name CHECK(material_name != '');
/
ALTER TABLE MATERIALS_T
ADD CONSTRAINT id_greater0 CHECK(material_id>0);
/
ALTER TABLE VEND_MAT_T
ADD CONSTRAINT primary_help PRIMARY KEY(material_id_fk,vend_edrpou_fk);
/
ALTER TABLE VEND_MAT_T
ADD CONSTRAINT vend_fk FOREIGN KEY(vend_edrpou_fk) REFERENCES VENDORS_T(vend_edrpou);
/
ALTER TABLE VEND_MAT_T
ADD CONSTRAINT mater_fk FOREIGN KEY(material_id_fk) REFERENCES MATERIALS_T(material_id);
/
ALTER TABLE USERS_T 
ADD CONSTRAINT primary_user PRIMARY KEY(user_id);
/
ALTER TABLE USERS_T 
ADD CONSTRAINT check_id_positive CHECK (user_id>0);
/
ALTER TABLE USERS_T 
ADD CONSTRAINT user_email_unique UNIQUE(user_email);
/
ALTER TABLE USERS_T 
ADD CONSTRAINT user_login_unique UNIQUE(user_login);

/