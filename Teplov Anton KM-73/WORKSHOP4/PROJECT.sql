------------TRIGGERS---------------
/*DROP SEQUENCE sq_Lessons;
DROP SEQUENCE sq_Groups;
DROP SEQUENCE sq_Teacher;
DROP SEQUENCE sq_Audience;
DROP SEQUENCE sq_Schedule;
DROP SEQUENCE sq_Student;*/

�����. ����� �� �������

CREATE SEQUENCE sq_Lessons
START WITH 1 
INCREMENT BY 1 
NOMAXVALUE;
/
CREATE OR REPLACE TRIGGER tr_Lessons before INSERT ON "Lessons" FOR each row
BEGIN
  SELECT sq_Lessons.NEXTVAL
  INTO :new.id_lesson
  FROM dual;
END;
/
CREATE SEQUENCE sq_Groups
START WITH 1 
INCREMENT BY 1 
NOMAXVALUE;
/
CREATE OR REPLACE TRIGGER tr_Groups before INSERT ON "Groups" FOR each row
BEGIN
  SELECT sq_Groups.NEXTVAL
  INTO :new."Groups_id" 
  FROM dual;
END;
/
CREATE SEQUENCE sq_Teacher
START WITH 1 
INCREMENT BY 1 
NOMAXVALUE;
/
CREATE OR REPLACE TRIGGER tr_Teacher before INSERT ON "Teacher" FOR each row
BEGIN
  SELECT sq_Teacher.NEXTVAL
  INTO :new.t_id
  FROM dual;
END;
/
CREATE SEQUENCE sq_Audience
START WITH 1 
INCREMENT BY 1 
NOMAXVALUE;
/
CREATE OR REPLACE TRIGGER tr_Audience before INSERT ON "Audience" FOR each row
BEGIN
  SELECT sq_Audience.NEXTVAL
  INTO :new."Audience_id"
  FROM dual;
END;
/
CREATE SEQUENCE sq_Student
START WITH 1 
INCREMENT BY 1 
NOMAXVALUE;
/
CREATE OR REPLACE TRIGGER tr_Student before INSERT ON "Student" FOR each row
BEGIN
  SELECT sq_Student.NEXTVAL
  INTO :new.st_id 
  FROM dual;
END;
/
CREATE OR REPLACE TRIGGER TRG_I_Groups
BEFORE INSERT ON "Groups"
FOR EACH ROW
BEGIN
    IF :new.name_g IS NULL
    THEN 
        raise_application_error(-20011,'name is empty');
    END IF;
    IF :new.entrance_year IS NULL
    THEN 
        raise_application_error(-20011,'entrance year is empty');
    END IF;
    IF :new.grad_year IS NULL
    THEN 
        raise_application_error(-20011,'grad year is empty');
    END IF;
END;
/
CREATE OR REPLACE TRIGGER TRG_I_Student
BEFORE INSERT ON "Student"
FOR EACH ROW
BEGIN
    IF :new.name IS NULL
    THEN 
        raise_application_error(-20011,'name is empty');
    END IF;
        IF :new.lastname IS NULL
    THEN 
        raise_application_error(-20011,'lastname is empty');
    END IF;
END;
/
CREATE OR REPLACE TRIGGER TRG_I_Teacher
BEFORE INSERT ON "Teacher"
FOR EACH ROW
BEGIN
    IF :new.teacher_name IS NULL
    THEN 
        raise_application_error(-20011,'teacher name is empty');
    END IF;
        IF :new.lastname IS NULL
    THEN 
        raise_application_error(-20011,'lastname is empty');
    END IF;
END;
/
CREATE OR REPLACE TRIGGER TRG_I_Audience
BEFORE INSERT ON "Audience"
FOR EACH ROW
BEGIN
    IF :new.building_num IS NULL
    THEN 
        raise_application_error(-20011,'building num name is empty');
    END IF;
    IF :new.audience_num IS NULL
    THEN 
        raise_application_error(-20011,'audience num is empty');
    END IF;
END;
/
CREATE OR REPLACE TRIGGER TRG_I_Schedule
BEFORE INSERT ON "Schedule"
FOR EACH ROW
BEGIN
    IF :new.term IS NULL
    THEN 
        raise_application_error(-20011,'building num name is empty');
    END IF;
END;

��� ��������� ����������� ����� �������� � ���� �� ���� ok. ���������� c���� � � ���� �������� ��� ������ 3 ���� ��� ���??