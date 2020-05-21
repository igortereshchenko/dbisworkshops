create or replace trigger user_trigg
BEFORE INSERT ON users
FOR EACH ROW
declare
counter integer;
BEGIN
    if :new.name is null
    then 
        raise_application_error(-20011,'Name is empty');
    end if;
    if :new.username is null
    then 
        raise_application_error(-20011,'Username is empty');
    end if;
    if :new.password is null
    then 
        raise_application_error(-20011,'Password is empty');
    end if;
    
   select count(*) into counter from users where username = :new.username;
   if counter> 0
   then
        raise_application_error(-20011,'Username mast be unique');
    end if;
END;