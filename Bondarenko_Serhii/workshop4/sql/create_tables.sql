CREATE TABLE users_t (
    user_id          INTEGER
        GENERATED ALWAYS AS IDENTITY ( START WITH 1 INCREMENT BY 1 ),
    user_name        VARCHAR2(100) NOT NULL,
    full_name        VARCHAR2(250) NOT NULL,
    sex              CHAR(1) NOT NULL CHECK ( sex IN (
        'M',
        'F'
    ) ),
    birthday         DATE NOT NULL,
    profile_photo    VARCHAR2(255) NOT NULL,
    profile_status   CHAR(1) DEFAULT 'N' NOT NULL CHECK ( profile_status IN (
        'N',
        'A',
        'B'
    ) ),
    friendly         CHAR(1) DEFAULT 'N' NOT NULL CHECK ( friendly IN (
        'Y',
        'N'
    ) ),
    reg_date         DATE DEFAULT current_date,
    CONSTRAINT ak_1 UNIQUE ( user_name ),
    CONSTRAINT users_pk PRIMARY KEY ( user_id ),
    CONSTRAINT check_age CHECK ( ( to_number(reg_date - birthday) ) >= 18 )
);

CREATE TABLE memberships (
    membsh_id   INTEGER
        GENERATED ALWAYS AS IDENTITY ( START WITH 1 INCREMENT BY 1 ),
    user_name   VARCHAR2(100) NOT NULL,
    reg_date    DATE DEFAULT current_date,
    qr_code     VARCHAR2(255) NOT NULL,
    memb_rank VARCHAR(1) NOT NULL CHECK ( memb_rank IN (
        '1',
        '2',
        '3'
    ) ),
    CONSTRAINT memberships_ak_1 UNIQUE ( user_name ),
    CONSTRAINT memberships_pk PRIMARY KEY ( membsh_id )
);

INSERT INTO users_t (
    user_name,
    full_name,
    sex,
    birthday,
    profile_photo
) VALUES (
    'user1',
    'fulluser1',
    'M',
    TO_DATE('2000/07/09', 'yyyy/mm/dd'),
    'dads'
);

INSERT INTO users_t (
    user_name,
    full_name,
    sex,
    birthday,
    profile_photo
) VALUES (
    'user2',
    'fulluser1',
    'M',
    TO_DATE('2000/07/09', 'yyyy/mm/dd'),
    'dads'
);

INSERT INTO users_t (
    user_name,
    full_name,
    sex,
    birthday,
    profile_photo
) VALUES (
    'user3',
    'fulluser1',
    'M',
    TO_DATE('2000/07/09', 'yyyy/mm/dd'),
    'dads'
);

INSERT INTO memberships (
    user_name,
    qr_code,
    memb_rank
) VALUES (
    'user2',
    'fulluser1',
    '1'
);

-- foreign keys
-- Reference: Memberships_fk0 (table: Memberships)

ALTER TABLE memberships
    ADD CONSTRAINT memberships_fk0 FOREIGN KEY ( user_name )
        REFERENCES users_t ( user_name );

-- Reference: Users_fk0 (table: Users)

ALTER TABLE users_t
    ADD CONSTRAINT users_t_fk0 FOREIGN KEY ( user_name )
        REFERENCES memberships ( user_name )DISABLE;