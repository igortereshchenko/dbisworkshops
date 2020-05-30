alter table users
add constraint pk_user
primary key 
(id);


alter table events
add constraint pk_event
primary key 
(id);


alter table events
add constraint fk_repeatedly
foreign key 
(repeatedly_id)
references repeatedly(id);


alter table events
add constraint fk_st
foreign key 
(start_id)
references time_dim (id);


alter table events
add constraint fk_et
foreign key 
(end_id)
references time_dim (id);


alter table events
modify 
(repeatedly_id number default 1);


alter table user_event
add constraint pk_user_event
primary key 
(user_id, event_id);


alter table user_event
add constraint fk_user
foreign key 
(user_id)
references users(id);


alter table user_event
add constraint fk_event
foreign key 
(event_id)
references events (id);


alter table groups
add constraint pk_group
primary key 
(id);


alter table user_group
add constraint pk_user_group
primary key 
(user_id, group_id);


alter table user_group
add constraint fk_user_group
foreign key 
(user_id)
references users(id);


alter table user_group
add constraint fk_group
foreign key 
(group_id)
references groups (id);


alter table user_group
add constraint check_admin
check (is_admin='1' or is_admin='0');


alter table repeatedly
add constraint pk_repeatedly
primary key 
(id);





