create table users
(
id number GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
name varchar2(100) not null,
username varchar2(20) UNIQUE not null,
password varchar2(100) not null
);


create table events
(
id number GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
name varchar2(50) not null,
event_date date not null,
start_id number not null,
end_id number not null,
repeatedly_id number
);


create table user_event
(
user_id number not null,
event_id number not null
);


create table groups
(
id number GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
name varchar2(100) not null
);



create table user_group
(
user_id number not null,
group_id number not null,
is_admin char(1)
);


create table repeatedly
(
id number GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
monday char(1) check (monday in ('0','1')),
tuesday char(1) check (tuesday in ('0','1')),
wednesday char(1) check (wednesday in ('0','1')),
thursday char(1) check (thursday in ('0','1')),
friday char(1) check (friday in ('0','1')),
saturday char(1) check (saturday in ('0','1')),
sunday char(1) check (sunday in ('0','1'))
);


create table time_dim
(
id integer GENERATED ALWAYS as IDENTITY(START with 1 INCREMENT by 1),
time varchar(20),
hour number not null,
minutes number not null
);


create view list_events
as
select 
    ue.user_id user_id,  e.name event_name, to_char(e.event_date, 'DD/MM/YYYY') event_date, st.time start_time, et.time end_time
from user_event ue
join events e
    on e.id = ue.event_id
join time_dim st
    on e.start_id = st.id
join time_dim et
    on e.end_id = et.id;


