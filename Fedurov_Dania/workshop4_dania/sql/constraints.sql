
alter table user_database
add constraint user_check1 CHECK ((user_age >= 18));

alter table user_database
add constraint user_unique UNIQUE  (user_mail, user_login);

alter table prediction_database
add constraint prediction_database_check UNIQUE  (prediction_description);

alter table numerology_database
add constraint numerology_database_check UNIQUE  (numerology_description);