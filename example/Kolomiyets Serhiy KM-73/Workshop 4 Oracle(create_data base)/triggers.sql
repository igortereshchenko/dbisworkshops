create or replace trigger order_trigger
BEFORE INSERT ON orders
FOR EACH ROW
declare
BEGIN
    if :new.surname is null
    then 
        raise_application_error(-20011,'Name is empty');
    end if;
    if :new.code is null
    then 
        raise_application_error(-20011,'Product code is empty');
    end if;
    if :new.phone is null
    then 
        raise_application_error(-20011,'Phone number is empty');
    end if;
    if :new.email is null
    then 
        raise_application_error(-20011,'Email is empty');
    end if;
    if :new.amount is null
    then 
        raise_application_error(-20011,'Amount is empty');
    end if;
    if :new.city is null
    then 
        raise_application_error(-20011,'City is empty');
    end if;
    if :new.street is null
    then 
        raise_application_error(-20011,'Street is empty');
    end if;
    if :new.order_date is null
    then 
        raise_application_error(-20011,'Date is empty');
    end if;
    
 
END;




create or replace trigger category_trigger
BEFORE INSERT ON categories
FOR EACH ROW
declare
BEGIN
    if :new.name is null
    then 
        raise_application_error(-20011,'Name is empty');
    end if;
    
    if :new.description is null
    then 
        raise_application_error(-20011,'Description is empty');
    end if;
END;  





create or replace trigger product_trigger
BEFORE INSERT ON products
FOR EACH ROW
declare
counter integer;
BEGIN
    if :new.name is null
    then 
        raise_application_error(-20011,'Name is empty');
    end if;
    
    if :new.code is null
    then 
        raise_application_error(-20011,'Code is empty');
    end if;
     
    select count(*) into counter from products where code = :new.code;
    if counter> 0
    then
        raise_application_error(-20011,'Code must be unique');
    end if;
    
    if :new.price is null
    then 
        raise_application_error(-20011,'Price is empty');
    end if;
    
    if :new.description is null
    then 
        raise_application_error(-20011,'Description is empty');
    end if;
    
    if :new.color is null
    then 
        raise_application_error(-20011,'Color is empty');
    end if;
    
    if :new.amount is null
    then 
        raise_application_error(-20011,'Amount is empty');
    end if;
    
     
    if :new.available is null
    then 
        raise_application_error(-20011,'Available is empty');
    end if;
    
    if :new.country is null
    then 
        raise_application_error(-20011,'Country is empty');
    end if;
    
    if :new.material is null
    then 
        raise_application_error(-20011,'Material is empty');
    end if;
    
    if :new.cat is null
    then 
        raise_application_error(-20011,'Category is empty');
    end if;
    
    if :new.model is null
    then 
        raise_application_error(-20011,'Model is empty');
    end if;

END; 