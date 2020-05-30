create table categories
(
id number GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
name varchar2(128) unique not null,
description varchar2(512) not null
);

create table products
(
id number GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
name varchar2(128) not null,
code number(8) unique not null,
price number(5) not null,
description varchar2(512) not null,
color varchar2(16) not null,
amount number(3) not null,
available varchar2(1) not null,
country varchar2(32) not null,
material varchar2(32) not null,
cat number(2) not null,
model varchar2(64) not null
);

create table orders
(
id number GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
surname varchar2(64) not null,
code number(8) not null,
phone varchar2(13) not null,
email varchar2(64) not null, 
amount number(2) not null,
city varchar2(16) not null,
street varchar2(128) not null,
order_date date not null
);