create table user_database (
    id INTEGER NOT NULL,
    user_name VARCHAR2(100) NOT NULL,
    user_mail VARCHAR2(100) NOT NULL,
    user_age INTEGER NOT NULL,
    login VARCHAR2(100) NOT NULL,
    user_pass VARCHAR2(100) NOT NULL,
  constraint user_pk primary key (id)
);

create table  todolist (
    user_id INTEGER NOT NULL,
    todolist_name VARCHAR2(100),
    description_of_todo VARCHAR2(200),
    time_creating TIMESTAMP(2) NOT NULL,
    status SMALLINT NOT NULL,
    constraint todolist_pk  PRIMARY KEY (user_id, time_creating)
);