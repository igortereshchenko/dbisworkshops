CREATE OR REPLACE TRIGGER lection_theme_del BEFORE
    DELETE ON lection_theme
DECLARE
    x   NUMBER;
BEGIN
    SELECT
        COUNT(*)
    INTO
        x
    FROM
        lection_theme;
    IF
        x < 4
    THEN
        raise_application_error(-20000,'Theme less than 4');
    END IF;
END;



    


