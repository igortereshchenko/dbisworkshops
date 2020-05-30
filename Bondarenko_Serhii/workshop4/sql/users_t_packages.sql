CREATE OR REPLACE TRIGGER check_user BEFORE
    INSERT OR UPDATE ON users_t
    FOR EACH ROW
BEGIN
    IF ( ( to_number(:new.reg_date - TO_DATE(:new.birthday,'yyyy/mm/dd')) ) < 18 ) THEN
        RAISE value_error;
    END IF;
END;

CREATE OR REPLACE PACKAGE registration_p AS
    PROCEDURE register_user (
        u_user_name       IN    users_t.user_name%TYPE,
        u_full_name       IN    users_t.full_name%TYPE,
        u_sex             IN    users_t.sex%TYPE,
        u_birthday        IN    users_t.full_name%TYPE,
        u_profile_photo   IN    users_t.profile_photo%TYPE,
        u_friend_name     IN    users_t.user_name%TYPE,
        u_friendly        OUT   users_t.friendly%TYPE,
        counter_unique    OUT   NUMBER,
        status            OUT   NVARCHAR2
    );

END registration_p;

CREATE OR REPLACE PACKAGE BODY registration_p AS

    PROCEDURE register_user (
        u_user_name       IN    users_t.user_name%TYPE,
        u_full_name       IN    users_t.full_name%TYPE,
        u_sex             IN    users_t.sex%TYPE,
        u_birthday        IN    users_t.full_name%TYPE,
        u_profile_photo   IN    users_t.profile_photo%TYPE,
        u_friend_name     IN    users_t.user_name%TYPE,
        u_friendly        OUT   users_t.friendly%TYPE,
        counter_unique    OUT   NUMBER,
        status            OUT   NVARCHAR2
    ) IS
        ambigous_ex EXCEPTION;
        is_null_ex EXCEPTION;
    BEGIN
        SELECT
            COUNT(*)
        INTO counter_unique
        FROM
            users_t
        WHERE
            users_t.user_name = u_user_name;

        IF counter_unique > 0 THEN
            RAISE ambigous_ex;
        END IF;
        IF ( u_user_name IS NULL ) OR ( u_full_name IS NULL ) OR ( u_sex IS NULL ) OR ( u_birthday IS NULL ) OR ( u_profile_photo
        IS NULL ) THEN
            RAISE is_null_ex;
        END IF;

        INSERT INTO users_t(users_t.user_name,users_t.full_name,users_t.sex,users_t.birthday,users_t.profile_photo) VALUES (
            u_user_name,
            u_full_name,
            u_sex,
            TO_DATE(u_birthday,'yyyy/mm/dd'),
            u_profile_photo
        );

        status := 'User has been added';
        IF ( u_friend_name IS NOT NULL ) THEN
            counter_unique := 0;
            SELECT
                COUNT(*)
            INTO counter_unique
            FROM
                users_t
            WHERE
                users_t.user_name = u_friend_name;

            IF counter_unique > 0 THEN
                UPDATE users_t
                SET
                    users_t.friendly = 'Y'
                WHERE
                    users_t.user_name = u_friend_name;

            END IF;

        END IF;

    EXCEPTION
        WHEN ambigous_ex THEN
            status := 'This username is already taken,so user with this name is already added';
        WHEN is_null_ex THEN
            status := 'Some data was not entered';
        WHEN value_error THEN
            status := 'Invalid data format, or user age less than 18';
        WHEN OTHERS THEN
            status := 'Some other problem';
    END register_user;

END registration_p;

CREATE OR REPLACE PACKAGE user_configurations_p AS

    FUNCTION get_user_id (
        u_user_name IN users_t.user_name%TYPE
    ) RETURN users_t.user_id%TYPE;

    PROCEDURE delete_user (
        u_user_name         IN    users_t.user_name%TYPE,
        status      OUT   NVARCHAR2
    );

    PROCEDURE edit_user (
        u_user_name         IN    users_t.user_name%TYPE,
        new_full_name       IN    users_t.full_name%TYPE,
        new_profile_photo   IN    users_t.profile_photo%TYPE,
        status              OUT   NVARCHAR2
    );

    PROCEDURE change_profile_status (
        u_user_name         IN    users_t.user_name%TYPE,
        new_profile_status   IN    users_t.profile_status%TYPE,
        status               OUT   NVARCHAR2
    );

END user_configurations_p;

CREATE OR REPLACE PACKAGE BODY user_configurations_p AS

    FUNCTION get_user_id (
        u_user_name IN users_t.user_name%TYPE
    ) RETURN users_t.user_id%TYPE IS
        u_user_id users_t.user_id%TYPE;
    BEGIN
        SELECT
            users_t.user_id
        INTO u_user_id
        FROM
            users_t
        WHERE
            users_t.user_name = u_user_name;

        RETURN u_user_id;
    EXCEPTION
        WHEN OTHERS THEN
            u_user_id := -1;
            RETURN u_user_id;
    END get_user_id;



    PROCEDURE delete_user (
        u_user_name   IN    users_t.user_name%TYPE,
        status      OUT   NVARCHAR2
    ) IS
    BEGIN
        DELETE FROM memberships
        WHERE
            memberships.user_name = u_user_name;
        DELETE FROM users_t
        WHERE
            users_t.user_name = u_user_name;

        status := 'User has been deleted';
    EXCEPTION
        WHEN OTHERS THEN
            status := 'Something happened and the user could not be deleted ';
    END delete_user;

    PROCEDURE edit_user (
        u_user_name         IN    users_t.user_name%TYPE,
        new_full_name       IN    users_t.full_name%TYPE,
        new_profile_photo   IN    users_t.profile_photo%TYPE,
        status              OUT   NVARCHAR2
    ) IS
        is_null_ex EXCEPTION;
    BEGIN
        IF ( new_full_name IS NULL ) OR ( new_profile_photo IS NULL ) THEN
            RAISE is_null_ex;
        END IF;

        UPDATE users_t
        SET
            users_t.full_name = new_full_name,
            users_t.profile_photo = new_profile_photo
        WHERE
             users_t.user_name = u_user_name ;

        status := 'Users data updated';
    EXCEPTION
        WHEN is_null_ex THEN
            status := 'Some data was not entered';
        WHEN value_error THEN
            status := 'Invalid data format';
        WHEN OTHERS THEN
            status := 'Some other problem';
    END edit_user;

    PROCEDURE change_profile_status (
        u_user_name            IN    users_t.user_name%TYPE,
        new_profile_status   IN    users_t.profile_status%TYPE,
        status               OUT   NVARCHAR2
    ) IS
    BEGIN
        UPDATE users_t
        SET
            users_t.profile_status = new_profile_status
        WHERE
            users_t.user_name = u_user_name;

        status := 'Status has been changed';
    EXCEPTION
        WHEN value_error THEN
            status := 'Invalid data format';
        WHEN OTHERS THEN
            status := 'Some other problem';
    END change_profile_status;

END user_configurations_p;