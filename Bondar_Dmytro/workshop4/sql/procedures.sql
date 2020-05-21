create or replace procedure add_event
    (user_id in number,
    event_name in varchar2,
    event_date in varchar2,
    start_time in varchar2,
    end_time in varchar2,
    mon in char,
    tue in char,
    wed in char,
    thu in char,
    fri in char,
    sat in char,
    sun in char)
is
    rep_id number;
    s_id number;
    e_id number;
    ev_date date;
    ev_collision integer;
    ev_id number;
begin

    if (user_id is null)
        then 
            raise_application_error(-20011,'user_id is empty');
        end if;
    if (event_name is null)
        then 
            raise_application_error(-20011,'event_name is empty');
        end if;
    if (event_date is null)
        then 
            raise_application_error(-20011,'event_date is empty');
        end if;
    if (start_time is null)
        then 
            raise_application_error(-20011,'start_time is empty');
        end if;
    if (end_time is null)
        then 
            raise_application_error(-20011,'end_time is empty');
        end if;

    ev_date := to_date(event_date, 'dd/mm/yyyy');

    select id
        into s_id  
    from time_dim
        where time = start_time;


    select id
        into e_id
    from time_dim
        where time = end_time;

    if (e_id < s_id)
        then 
        raise_application_error(-20001,'Incorrect event time');
    else if ( (ev_date < current_date) or (ev_date = current_date and to_char(current_timestamp, 'hh24:MM') > start_time) )
        then
        raise_application_error(-20001,'Incorrect event time');   
        end if;
    end if;

    select count(*)
        into ev_collision
    from events e
        join user_event ue
        on ue.event_id = e.id
    where 
        e.event_date = ev_date and
        ue.user_id= user_id and (
        (e.start_id >= s_id and e.start_id < e_id ) or 
        (e.end_id > s_id and e.end_id <= e_id )  or
        (e.start_id > s_id and e.end_id < e_id) );

    if (ev_collision > 0)
        then
        raise_application_error(-20001,'Event collision');
    end if;

    select id 
        into rep_id
    from repeatedly
        where 
        monday = mon and
        tuesday = tue and
        wednesday = wed and
        thursday = thu and
        friday = fri and
        saturday = sat and
        sunday = sun ;

    insert into events
        (name, event_date, start_id, end_id, repeatedly_id )
    values
        (event_name,
        ev_date,
        s_id,
        e_id,
        rep_id);

    select max(id)
        into ev_id
    from events;

    insert into user_event
        (user_id, event_id)
    values
        (user_id,
        ev_id);
    COMMIT;
EXCEPTION
WHEN OTHERS THEN
   raise_application_error(-20001,'An error was encountered - '||SQLCODE||' -ERROR- '||SQLERRM);
end add_event;


create or replace NONEDITIONABLE procedure add_group
(user_id in number,
g_name in varchar2)
is
g_id number;
begin

if (g_name is null)
    then 
    raise_application_error(-20011,'group_name is empty');
end if;

insert into 
groups (name)
values (g_name);

select max(id)
into g_id
from groups;

insert into 
user_group (user_id , group_id , is_admin )
values (user_id, g_id, '0');

COMMIT;
EXCEPTION
WHEN OTHERS THEN
   raise_application_error(-20001,'An error was encountered - '||SQLCODE||' -ERROR- '||SQLERRM);
end add_group;



