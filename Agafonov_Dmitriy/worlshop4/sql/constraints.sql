
alter table user_table_sql
add constraint user_check1 CHECK ((user_age >= 18));

alter table user_table_sql
add constraint user_check2 CHECK (LENGTH(edrpou) = 6);

alter table user_table_sql
add constraint user_check3 CHECK  (LENGTH(user_pass) >= 5);

alter table user_table_sql
add constraint user_unique UNIQUE  (user_mail, edrpou);

alter table question_table_sql
add constraint question_fk foreign key (user_id) references user_table_sql(id);

alter table question_table_sql
add constraint question_check CHECK (status IN (0, 1));