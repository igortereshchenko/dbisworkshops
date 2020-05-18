create table students(
	student_id integer not null,
	student_name varchar2(100) not null,
	student_abitur boolean not null,
	student_sex varchar2(6) not null,
	constraint student_pk primary key (student_id)
);

create table regions(
	region_id integer not null,
	region_name varchar2(200) not null,
	constraint region_pk primary key (region_id)
);

create table univers(
	univer_id integer not null,
	univer_name varchar2(200) not null,
	constraint univer_pk primary key (univer_id)
);

create table specialties(
	specialty_id integer not null,
	specialty_name varchar2(200) not null,
	constraint specialty_pk primary key (specialty_id)
);

create table zno_scores(
	zno_score_id integer not null,
	zno_score_name varchar2(100) not null,
	zno_score_value float not null,
	zno_score_student_id integer not null,
	constraint zno_score_pk primary key (zno_score_id)
);

create table recom_list(
	recom_id integer not null,
	recom_specialty_id integer not null,
	recom_univer_id integer not null,
	recom_region_id integer not null,
	recom_priority integer not null,
	recom_student_id integer not null,

	constraint recom_id _pk primary key (recom_id)
);
