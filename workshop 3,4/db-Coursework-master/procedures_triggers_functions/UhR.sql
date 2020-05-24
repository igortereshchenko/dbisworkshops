CREATE OR REPLACE PACKAGE uhr_package IS
    
    FUNCTION add_uhr (
        u_nick       IN user_has_resourses.author_nickname%TYPE,
        u_resourse   IN user_has_resourses.resource_name%TYPE
    ) RETURN VARCHAR2;

    PROCEDURE del_uhr (
        u_resourse   IN user_has_resourses.resource_name%TYPE,
        u_nick       IN user_has_resourses.author_nickname%TYPE
    );

    FUNCTION update_uhr (
        new_resourse   IN user_has_resourses.resource_name%TYPE,
        old_resourse   IN user_has_resourses.resource_name%TYPE
    ) RETURN VARCHAR2;

END uhr_package;
/

CREATE OR REPLACE PACKAGE BODY uhr_package IS

    FUNCTION add_uhr (
        u_nick       IN user_has_resourses.author_nickname%TYPE,
        u_resourse   IN user_has_resourses.resource_name%TYPE
    ) RETURN VARCHAR2 IS
        message   VARCHAR2(30);
    BEGIN
        message := 'ok';
        INSERT INTO user_has_resourses (
            user_resourse_id,
            author_nickname,
            resource_name,
            "Date"
        ) VALUES (
            uhr_id.NEXTVAL,
            u_nick,
            u_resourse,
            SYSDATE
        );

        COMMIT;
        RETURN message;
    EXCEPTION
        WHEN dup_val_on_index THEN
            message := 'this resourse already exist';
            RETURN message;
        WHEN OTHERS THEN
            message := 'you entered wrong data!!!';
            RETURN message;
    END add_uhr;

    PROCEDURE del_uhr (
        u_resourse   IN user_has_resourses.resource_name%TYPE,
        u_nick       IN user_has_resourses.author_nickname%TYPE
    )
        IS
    BEGIN
        DELETE FROM user_has_resourses WHERE
            resource_name = u_resourse
            and author_nickname=u_nick;

        COMMIT;
    END del_uhr;

    FUNCTION update_uhr (
        new_resourse   IN user_has_resourses.resource_name%TYPE,
        old_resourse   IN user_has_resourses.resource_name%TYPE
    ) RETURN VARCHAR2 IS
        message   VARCHAR2(30);
    BEGIN
        message := 'ok';
        UPDATE user_has_resourses
            SET
                resource_name = new_resourse
        WHERE
            resource_name = old_resourse;

        COMMIT;
        RETURN message;
    EXCEPTION
        WHEN dup_val_on_index THEN
            message := 'this resourse already exist';
            RETURN message;
        WHEN OTHERS THEN
            message := 'you entered wrong data!!!';
            RETURN message;
    END update_uhr;

END uhr_package;
/