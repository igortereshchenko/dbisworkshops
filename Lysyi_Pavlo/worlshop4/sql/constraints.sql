
alter table user_database
add constraint user_check1 CHECK ((user_age >= 16));

alter table user_database
add constraint user_check2 CHECK (LENGTH(login) >= 5);

alter table user_database
add constraint user_check3 CHECK  (LENGTH(user_pass) >= 5);

alter table user_database
add constraint user_unique UNIQUE  (user_mail, login);

alter table todolist
add constraint todolist_fk foreign key (user_id) references user_database(id);

alter table todolist
add constraint todolist_check CHECK (status IN (0, 1));