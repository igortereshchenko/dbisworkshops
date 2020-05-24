CREATE OR REPLACE PACKAGE information_package IS
    TYPE row_info IS RECORD ( i_id information.info_id%TYPE,
    i_nickname information.nickname%TYPE,
    i_lec_name information.lection_name%TYPE,
    i_resourse information.resource_name%TYPE,
    i_link information.information_link%TYPE,
    i_date information."Date"%TYPE );
    TYPE tbl_information IS
        TABLE OF row_info;
    FUNCTION get_information (
        nick   IN information.nickname%TYPE default null,
        lec_name IN information.lection_name%TYPE
    ) RETURN tbl_information
        PIPELINED;

    FUNCTION add_info (
        i_nickname   IN information.nickname%TYPE,
        i_lec_name   IN information.lection_name%TYPE,
        i_resourse   IN information.resource_name%TYPE,
        i_link       IN information.information_link%TYPE
    )return VARCHAR2;

    PROCEDURE del_info (
        i_nickname   IN information.nickname%TYPE,
        i_id   IN information.INFO_ID%TYPE
    );

END information_package;
/

CREATE OR REPLACE PACKAGE BODY information_package IS

    FUNCTION get_information (
        nick   IN information.nickname%TYPE default null,
        lec_name IN information.lection_name%TYPE
    ) RETURN tbl_information
        PIPELINED
    IS
    TYPE information_cursor_type IS REF CURSOR;
        information_cursor information_cursor_type;
        cursor_data row_info;
        query_str VARCHAR2(1000);
    BEGIN
        query_str:= 'SELECT * FROM information';
            if nick is not NULL then
                query_str:= query_str||' where TRIM(information.nickname) = trim('''||nick||''')';
                if lec_name is not NULL THEN
                    query_str:= query_str||' AND TRIM(information.lection_name) = trim('''||lec_name||''')';
                end if;
            else 
                if lec_name is not NULL then
                    query_str:= query_str||' where TRIM(information.lection_name) = trim('''||lec_name||''')';
                end if;
            end if;
        OPEN information_cursor FOR query_str;
        LOOP
            FETCH information_cursor INTO cursor_data;
            EXIT WHEN ( information_cursor%notfound );
            PIPE ROW ( cursor_data );
        END LOOP;
    END get_information;

    FUNCTION add_info (
        i_nickname   IN information.nickname%TYPE,
        i_lec_name   IN information.lection_name%TYPE,
        i_resourse   IN information.resource_name%TYPE,
        i_link       IN information.information_link%TYPE
    )return VARCHAR2
        IS
        message VARCHAR2(30);
        nickname_ex EXCEPTION;
        theme_ex EXCEPTION;
        resourse_ex exception;
        link_ex EXCEPTION;
    BEGIN
        message:='ok';  
        if not REGEXP_LIKE(i_nickname,'^[A-Za-z].*') then
            raise nickname_ex;
        end if;
        if not REGEXP_LIKE(i_lec_name,'^[A-Z][A-Za-z]*\s([A-Za-z]*\s?)+') then
            raise theme_ex;
        end if;
        if not REGEXP_LIKE(i_resourse,'^www\.[a-z]*\.[0-9a-z\.\/\-]+') then
                raise resourse_ex;
        end if;
        if not REGEXP_LIKE(i_link,'^https:\/\/telegra\.ph\/[A-Za-z\-]+') then
                raise link_ex;
        end if;
        
        INSERT INTO information (
            info_id,
            nickname,
            lection_name,
            resource_name,
            information_link,
            "Date"
        ) VALUES (
            info_id.nextval,
            i_nickname,
            i_lec_name,
            i_resourse,
            i_link,
            SYSDATE
        );

        COMMIT;
        return message;
    exception
        when DUP_VAL_ON_INDEX then
            message:='this user already exist';
            return message;
        when theme_ex then
            message:='invalid theme!!!';
            return message;
        when resourse_ex then
            message:='invalid resourse!!!';
            return message;
        when nickname_ex then
            message:='invalid nickname';
            return message;
        when link_ex then
            message:='invalid link';
            return message;
        when OTHERS then
            message:='You Enter wrong information';
            return message;
    END add_info;

    PROCEDURE del_info (
        i_nickname   IN information.nickname%TYPE,
        i_id   IN information.INFO_ID%TYPE
    )
        IS
    BEGIN
        DELETE FROM information
        WHERE
            information.nickname = i_nickname
            and information.INFO_ID = i_id;
            
    COMMIT;

    END del_info;

END information_package;
/