CREATE OR REPLACE PACKAGE uht_package IS

    FUNCTION add_uht (
        u_nick    IN user_has_theme.author_nickname%TYPE,
        u_theme   IN user_has_theme.lection_name%TYPE
    ) RETURN VARCHAR2;

    PROCEDURE del_uht (
        u_theme   IN user_has_theme.lection_name%TYPE,
        u_nick    IN user_has_theme.author_nickname%TYPE
    );

    FUNCTION update_uht (
        new_theme   IN user_has_theme.lection_name%TYPE,
        old_theme   IN user_has_theme.lection_name%TYPE
    ) RETURN VARCHAR2;

END uht_package;
/

CREATE OR REPLACE PACKAGE BODY uht_package IS

    FUNCTION add_uht (
        u_nick    IN user_has_theme.author_nickname%TYPE,
        u_theme   IN user_has_theme.lection_name%TYPE
    ) RETURN VARCHAR2 IS
        message   VARCHAR2(30);
    BEGIN
        message := 'ok';
        INSERT INTO USER_HAS_THEME (
            USER_THEME_ID,
            author_nickname,
            LECTION_NAME,
            "Date"
        ) VALUES (
            uht_id.NEXTVAL,
            u_nick,
            u_theme,
            SYSDATE
        );

        COMMIT;
        RETURN message;
    EXCEPTION
        WHEN dup_val_on_index THEN
            message := 'this theme already exist';
            RETURN message;
        WHEN OTHERS THEN
            message := 'you entered wrong data!!!';
            RETURN message;
    END add_uht;

    PROCEDURE del_uht (
        u_theme   IN user_has_theme.lection_name%TYPE,
        u_nick    IN user_has_theme.author_nickname%TYPE
    )
        IS
    BEGIN
        DELETE FROM user_has_theme WHERE
            lection_name = u_theme
            and author_nickname=u_nick;

        COMMIT;
    END del_uht;

    FUNCTION update_uht (
        new_theme   IN user_has_theme.lection_name%TYPE,
        old_theme   IN user_has_theme.lection_name%TYPE
    ) RETURN VARCHAR2 IS
        message   VARCHAR2(30);
    BEGIN
        message := 'ok';
        UPDATE user_has_theme
            SET
                lection_name = new_theme
        WHERE
            lection_name = old_theme;

        COMMIT;
        RETURN message;
    EXCEPTION
        WHEN dup_val_on_index THEN
            message := 'this theme already exist';
            RETURN message;
        WHEN OTHERS THEN
            message := 'you entered wrong data!!!';
            RETURN message;
    END update_uht;

END uht_package;
/