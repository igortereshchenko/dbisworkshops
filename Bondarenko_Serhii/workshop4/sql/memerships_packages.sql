
CREATE OR REPLACE PACKAGE create_membership_p AS
    PROCEDURE create_membership (
        m_user_name       IN    memberships.user_name%TYPE,
        m_qr_code   IN    memberships.qr_code%TYPE,
        m_memb_rank   IN    memberships.memb_rank%TYPE,
        counter_unique    OUT   NUMBER,
        status            OUT   NVARCHAR2
    );

END create_membership_p;

CREATE OR REPLACE PACKAGE BODY create_membership_p AS

    PROCEDURE create_membership (
        m_user_name       IN    memberships.user_name%TYPE,
        m_qr_code   IN    memberships.qr_code%TYPE,
        m_memb_rank   IN    memberships.memb_rank%TYPE,
        counter_unique    OUT   NUMBER,
        status            OUT   NVARCHAR2
    ) IS
        unambigous_ex EXCEPTION;
        is_null_ex EXCEPTION;
    BEGIN
        counter_unique:= 0;
        SELECT
            COUNT(*)
        INTO counter_unique
        FROM
            memberships
        WHERE
            memberships.user_name = m_user_name;

        IF counter_unique = 0 THEN
            RAISE unambigous_ex;
        END IF;
        IF ( m_user_name IS NULL ) OR ( m_qr_code IS NULL ) OR ( m_memb_rank IS NULL ) THEN
            RAISE is_null_ex;
        END IF;
        
        INSERT INTO memberships(memberships.user_name,memberships.qr_code,memberships.memb_rank) VALUES (
            m_user_name,
            m_qr_code,
            m_memb_rank
        );
        status := 'Membership has been created';
        
        
    EXCEPTION
        WHEN unambigous_ex THEN
            status := 'Cant find user with this username';
        WHEN is_null_ex THEN
            status := 'Some data was not entered';
        WHEN value_error THEN
            status := 'Invalid data format';
        WHEN OTHERS THEN
            status := 'Some other problem';
    END create_membership;

END create_membership_p;

CREATE OR REPLACE PACKAGE membership_configurations_p AS


    FUNCTION get_membsh_id (
        m_user_name IN memberships.user_name%TYPE
    ) RETURN memberships.membsh_id%TYPE;

    PROCEDURE delete_membership (
        m_user_name   IN    memberships.user_name%TYPE,
        status      OUT   NVARCHAR2
    );
    
    PROCEDURE check_and_del (
        m_user_name   IN    memberships.user_name%TYPE,
        m_memb_rank   IN    memberships.memb_rank%TYPE,
        m_reg_date   IN    memberships.reg_date%TYPE,
        checked_date IN   NVARCHAR2,
        status      OUT   NVARCHAR2
    );



END membership_configurations_p;

CREATE OR REPLACE PACKAGE BODY membership_configurations_p AS
    
    FUNCTION get_membsh_id (
        m_user_name IN memberships.user_name%TYPE
    ) RETURN memberships.membsh_id%TYPE IS
        m_membsh_id memberships.membsh_id%TYPE;
    BEGIN
        SELECT
            memberships.membsh_id
        INTO m_membsh_id
        FROM
            memberships
        WHERE
            memberships.user_name = m_user_name;

        RETURN m_membsh_id;
    EXCEPTION
        WHEN OTHERS THEN
            m_membsh_id := -1;
            RETURN m_membsh_id;
    END get_membsh_id;

    PROCEDURE delete_membership (
        m_user_name   IN    memberships.user_name%TYPE,
        status      OUT   NVARCHAR2
    ) IS
    BEGIN
        DELETE FROM memberships
        WHERE
            memberships.user_name = m_user_name;

        status := 'Membership has been deleted';
    EXCEPTION
        WHEN OTHERS THEN
            status := 'Something happened and the Membership could not be deleted ';
    END delete_membership;
    
    PROCEDURE check_and_del (
        m_user_name   IN    memberships.user_name%TYPE,
        m_memb_rank   IN    memberships.memb_rank%TYPE,
        m_reg_date   IN    memberships.reg_date%TYPE,
        checked_date IN   NVARCHAR2,
        status      OUT   NVARCHAR2
    )IS
    BEGIN
        IF (m_memb_rank = '1') THEN
            IF ( ( to_number(TO_DATE(checked_date,'yyyy/mm/dd') - m_reg_date) ) > 30 ) THEN
                DELETE FROM memberships
                WHERE
                    memberships.user_name = m_user_name;
            END IF;
        END IF;
        IF (m_memb_rank = '2') THEN
            IF ( ( to_number(TO_DATE(checked_date,'yyyy/mm/dd') - m_reg_date) ) > 90 ) THEN
                DELETE FROM memberships
                WHERE
                    memberships.user_name = m_user_name;
            END IF;
        END IF;
        IF (m_memb_rank = '3') THEN
            IF ( ( to_number(TO_DATE(checked_date,'yyyy/mm/dd') - m_reg_date) ) > 365 ) THEN
                DELETE FROM memberships
                WHERE
                    memberships.user_name = m_user_name;
            END IF;
        END IF;
        status := 'Abonement is still active ';
    EXCEPTION
        WHEN OTHERS THEN
            status := 'Something happened and the checkig was crashed ';
    END check_and_del;
END membership_configurations_p;