CREATE OR REPLACE PACKAGE lection_theme_package IS type rowlection_theme is RECORD( u_theme lection_theme.lection_name%TYPE);
    TYPE tbl_lection_theme IS
        TABLE OF rowlection_theme;
    FUNCTION get_lection_theme(theme IN lection_theme.lection_name%TYPE default null)
    RETURN tbl_lection_theme
        PIPELINED;

    FUNCTION add_theme (
        u_theme   IN lection_theme.lection_name%TYPE
    )return VARCHAR2;

    PROCEDURE del_theme (
        u_theme   IN lection_theme.lection_name%TYPE
    );

    FUNCTION update_theme (
        new_theme   IN lection_theme.lection_name%TYPE,
        old_theme   IN lection_theme.lection_name%TYPE
    )RETURN VARCHAR2;
end lection_theme_package;
/
    
CREATE OR REPLACE PACKAGE BODY lection_theme_package IS 
    
    FUNCTION get_lection_theme(theme IN lection_theme.lection_name%TYPE default null) 
    RETURN tbl_lection_theme
        PIPELINED
        is
        TYPE lection_cursor_type IS REF CURSOR;
        lection_cursor lection_cursor_type;
        cursor_data rowlection_theme;
        query_str VARCHAR2(1000);
        begin
        query_str := 'select * from LECTION_THEME';
    if theme IS NOT NULL then
    query_str := query_str
    || ' where TRIM(lection_theme.lection_name) = trim('''
    || theme
    || ''')';
    end if;
    OPEN lection_cursor FOR query_str;

    LOOP
        FETCH lection_cursor INTO cursor_data;
        EXIT WHEN ( lection_cursor%notfound );
        pipe      row(cursor_data);
        end       loop;

    end get_lection_theme;
    
    FUNCTION add_theme (
        u_theme   IN lection_theme.lection_name%TYPE
    )return VARCHAR2 is
    message VARCHAR2(30);
    theme_ex EXCEPTION;
    begin
        message:='ok';
        if not REGEXP_LIKE(u_theme,'^[A-Z][A-Za-z]*\s([A-Za-z]*\s?)+') then
            raise theme_ex;
        end if;
        INSERT INTO LECTION_THEME
        (LECTION_NAME) VALUES ( u_theme );
        COMMIT;
        return message;
    exception
        when DUP_VAL_ON_INDEX then
            message:='this theme already exist';
            return message;
        when theme_ex then
            message:='invalid theme!!!';
            return message;
    end add_theme;
    
    PROCEDURE del_theme (
        u_theme   IN lection_theme.lection_name%TYPE
    ) is
    begin
        delete from LECTION_THEME
        where LECTION_NAME = u_theme;
    COMMIT;
    end del_theme;

    FUNCTION update_theme (
        new_theme   IN lection_theme.lection_name%TYPE, 
        old_theme IN lection_theme.lection_name%TYPE
    )return VARCHAR2 IS 
    message VARCHAR2(30);
    theme_ex EXCEPTION;
    BEGIN
    message:='ok';
        if not REGEXP_LIKE(new_theme,'^[A-Z][A-Za-z]*\s([A-Za-z]*\s?)+') then
            raise theme_ex;
        end if;
    UPDATE lection_theme
        SET
            lection_name = new_theme
    WHERE
        lection_name = old_theme;
    COMMIT;
    return message;
    exception
        when DUP_VAL_ON_INDEX then
            message:='this theme already exist';
            return message;
        when theme_ex then
            message:='invalid new theme!!!';
            return message;
END update_theme; 
end lection_theme_package;
/