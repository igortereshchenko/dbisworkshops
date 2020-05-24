CREATE OR REPLACE PACKAGE user_package IS
    TYPE rowuser IS RECORD ( u_nickname "User".nickname%TYPE,
    u_login "User".login%TYPE,
    u_pass "User".pass%TYPE,
    u_name "User".name%TYPE,
    u_surname "User".surname%TYPE,
    u_faculty "User".faculty_name%TYPE,
    u_course "User".course_number%TYPE );
    TYPE tbl_user IS
        TABLE OF rowuser;
    FUNCTION get_user (
        u_nickname   "User".nickname%TYPE DEFAULT NULL
    ) RETURN tbl_user
        PIPELINED;

    FUNCTION is_user (
        u_nickname   "User".nickname%TYPE,
        u_pass       "User".pass%TYPE
    ) RETURN INTEGER;

    FUNCTION add_user (
        u_nickname   IN "User".nickname%TYPE,
        u_login      IN "User".login%TYPE,
        u_pass       IN "User".pass%TYPE,
        u_name       IN "User".name%TYPE DEFAULT NULL,
        u_surname    IN "User".surname%TYPE DEFAULT NULL,
        u_faculty    IN "User".faculty_name%TYPE,
        u_course     IN "User".course_number%TYPE
    )return VARCHAR2;

    PROCEDURE deluser (
        u_nickname   IN "User".nickname%TYPE
    );

END user_package;
/

CREATE OR REPLACE PACKAGE BODY user_package 
IS
    FUNCTION get_user (
        u_nickname   "User".nickname%TYPE DEFAULT NULL
    ) RETURN tbl_user
        PIPELINED
    IS
        TYPE user_cursor_type IS REF CURSOR;
        user_cursor   user_cursor_type;
        cursor_data   rowuser;
        query_str     VARCHAR2(1000);
    BEGIN
        query_str := 'select * from "User"';
        IF
            u_nickname IS NOT NULL
        THEN
            query_str := query_str
            || ' where TRIM("User".nickname) = trim('''
            || u_nickname
            || ''')';
        END IF;

        OPEN user_cursor FOR query_str;

        LOOP
            FETCH user_cursor INTO cursor_data;
            EXIT WHEN ( user_cursor%notfound );
            PIPE ROW ( cursor_data );
        END LOOP;

    END get_user;

    FUNCTION is_user (
        u_nickname   "User".nickname%TYPE,
        u_pass       "User".pass%TYPE
    ) RETURN INTEGER IS
        counter   INTEGER;
    BEGIN
        SELECT
            COUNT(*)
        INTO
            counter
        FROM
            "User"
        WHERE
            TRIM("User".nickname) = TRIM(u_nickname)
            AND   TRIM("User".pass) = TRIM(u_pass);

        RETURN counter;
    END is_user;

    FUNCTION add_user (
        u_nickname   IN "User".nickname%TYPE,
        u_login      IN "User".login%TYPE,
        u_pass       IN "User".pass%TYPE,
        u_name       IN "User".name%TYPE DEFAULT NULL,
        u_surname    IN "User".surname%TYPE DEFAULT NULL,
        u_faculty    IN "User".faculty_name%TYPE,
        u_course     IN "User".course_number%TYPE
    )return VARCHAR2
        IS
        message VARCHAR2(30);
        pass_ex EXCEPTION;
        name_ex EXCEPTION;
        surname_ex EXCEPTION;
        nickname_ex EXCEPTION;
        facultyname_ex EXCEPTION;
        course_ex EXCEPTION;
    BEGIN
        message:='ok';
        if not REGEXP_LIKE(u_pass,'[A-Za-z0-9]{6,16}') then
            raise pass_ex;
        end if;
        
        if u_name is not NULL and not REGEXP_LIKE(u_name,'^[A-Z][A-Za-z]+') then
            raise name_ex;
        end if;
        
        if u_surname is not NULL and not REGEXP_LIKE(u_surname,'^[A-Z][A-Za-z]+') then
            raise surname_ex;
        end if;
        
        if not REGEXP_LIKE(u_nickname,'^[A-Za-z].*') then
            raise nickname_ex;
        end if;
        
        if u_course>6 and u_course<=0 then
            raise course_ex;
        end if;
        
        if not REGEXP_LIKE(u_faculty,'^[A-Z]{1}[A-Za-z]+(\s[A-Za-z]*)*') then
            raise facultyname_ex;
        end if;
        INSERT INTO "User" (
            login,
            pass,
            nickname,
            name,
            surname,
            faculty_name,
            course_number
        ) VALUES (
            u_login,
            u_pass,
            u_nickname,
            u_name,
            u_surname,
            u_faculty,
            u_course
        );
        COMMIT;
        return message;
    exception
        when DUP_VAL_ON_INDEX then
            message:='this user already exist';
            return message;
        when pass_ex then
            message:='invalid password';
            return message;
        when name_ex then
            message:='invalid name';
            return message;
        when surname_ex then
            message:='invalid surname';
            return message;
        when nickname_ex then
            message:='invalid nickname';
            return message;
        when facultyname_ex then
            message:='invalid faculty';
            return message;
        when course_ex then
            message:='invalid course number';
            return message;
    END add_user;

    PROCEDURE deluser (
        u_nickname   IN "User".nickname%TYPE
    )IS 
    BEGIN
        DELETE FROM "User"
        WHERE
            "User".nickname = u_nickname;
        COMMIT;    
    END deluser; 
END user_package;
/