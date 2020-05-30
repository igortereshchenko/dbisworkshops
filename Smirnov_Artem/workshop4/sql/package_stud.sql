create or replace package student_auth is

	procedure new_student(
		stud_id out integer,
		status out varchar2,
		student_name in students.student_name%type,
		student_abitur in students.student_abitur%type,
		student_sex in students.student_sex%type
);

end student_auth;

create or replace package body student_auth is
    procedure new_student(
                stud_id out integer,
                status out varchar2,
                student_name in students.student_name%type,
                student_abitur in students.student_abitur%type,
                student_sex in students.student_sex%type
	) is
	begin
	BEGIN
	insert into students(student_id,student_name,
				student_abitur,student_sex) 
		values(seq_student.nextval,student_name,
			student_abitur,student_sex)
	returning student_id into stud_id;

	commit;
	status:='ok';
	exception
		when dup_val_on_index then
			status:='student already exist';
		when others then
			status:=sqlerrm;
	END;

	end new_student;


end student_auth;
