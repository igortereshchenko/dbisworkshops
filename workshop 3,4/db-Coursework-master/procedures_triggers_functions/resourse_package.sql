CREATE OR REPLACE PACKAGE resourse_package IS type rowresourse is RECORD( u_resourse resourse.resource_name%TYPE);
    TYPE tbl_resourse IS
        TABLE OF rowresourse;
    FUNCTION get_resourse (u_resourse IN resourse.resource_name%TYPE default null)
    RETURN tbl_resourse
        PIPELINED;

    FUNCTION add_resourse (
        u_resourse in RESOURSE.RESOURCE_NAME%TYPE
    )RETURN VARCHAR2;

    PROCEDURE del_resourse (
        u_resourse in RESOURSE.RESOURCE_NAME%TYPE
    );

    FUNCTION update_resourse (
        new_resourse in RESOURSE.RESOURCE_NAME%TYPE,
        old_resourse in RESOURSE.RESOURCE_NAME%TYPE
    )RETURN VARCHAR2;
end resourse_package;
/
    
CREATE OR REPLACE PACKAGE BODY resourse_package IS 
    
    FUNCTION get_resourse (u_resourse IN resourse.resource_name%TYPE default null)
    RETURN tbl_resourse
        PIPELINED
        is
        TYPE resourse_cursor_type IS REF CURSOR;
        resourse_cursor resourse_cursor_type;
        cursor_data rowresourse;
        query_str VARCHAR2(1000);
        begin
            query_str:= 'SELECT * FROM RESOURSE';
            if u_resourse is not NULL then
                query_str:= query_str||' where TRIM(resourse.resource_name) = trim('''||u_resourse||''')';
            end if;
        OPEN resourse_cursor FOR query_str;
        loop
            FETCH resourse_cursor INTO cursor_data;
            EXIT WHEN ( resourse_cursor%notfound );
            pipe row(cursor_data);
        end loop;
    end get_resourse;
    
    FUNCTION add_resourse (
        u_resourse in RESOURSE.RESOURCE_NAME%TYPE
    )RETURN VARCHAR2 is
    message VARCHAR2(30);
    resourse_ex exception;
    begin
        message:='ok';
            if not REGEXP_LIKE(u_resourse,'^www\.[a-z]*\.[0-9a-z\.\/\-]+') then
                raise resourse_ex;
            end if;
        INSERT INTO RESOURSE
        (RESOURCE_NAME) VALUES ( u_resourse );
        COMMIT;
        return message;
    exception
        when DUP_VAL_ON_INDEX then
            message:='this resourse already exist';
            return message;
        when resourse_ex then
            message:='invalid resourse!!!';
            return message;
    end add_resourse;
    
    PROCEDURE del_resourse (
        u_resourse in RESOURSE.RESOURCE_NAME%TYPE
    ) is
    begin
        delete from RESOURSE
        where RESOURCE_NAME = u_resourse;
    COMMIT;
    end del_resourse;

    FUNCTION update_resourse (
        new_resourse in RESOURSE.RESOURCE_NAME%TYPE,
        old_resourse in RESOURSE.RESOURCE_NAME%TYPE
    )RETURN VARCHAR2 is
    message VARCHAR2(30);
    resourse_ex exception;
    BEGIN
        message:='ok';
            if not REGEXP_LIKE(new_resourse,'^www\.[a-z]*\.[0-9a-z\.\/\-]+') then
                raise resourse_ex;
            end if;
        UPDATE RESOURSE
            SET
                RESOURCE_NAME = new_resourse
        WHERE
            RESOURCE_NAME = old_resourse;
        COMMIT;
        return message;
    exception
        when DUP_VAL_ON_INDEX then
            message:='this resourse already exist';
            return message;
        when resourse_ex then
            message:='invalid new resourse!!!';
            return message;
    END update_resourse;
    
end resourse_package;
/