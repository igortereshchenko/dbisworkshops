create or replace package recom_pkg is

	procedure new_recom(
		recom_id out integer,
		status out varchar2,
		recom_specialty_id in specialties.specialty_id%type,
		recom_univer_id in univers.univer_id%type,
		recom_region_id in regions.region_id%type,
		recom_priority in integer,
		recom_student_id in students.student_id%type

);

end recom_pkg;

create or replace package body recom_pkg is
    procedure new_recom(
        rec_id out integer,
		status out varchar2,
		recom_specialty_id in specialties.specialty_id%type,
		recom_univer_id in univers.univer_id%type,
		recom_region_id in regions.region_id%type,
		recom_priority in integer,
		recom_student_id in students.student_id%type
	) is
	begin
	BEGIN
	insert into recom_list(recom_id,recom_specialty_id,
				recom_univer_id,recom_region_id,
				recom_priority, recom_student_id) 
		values(seq_recom.nextval,recom_specialty_id,
				recom_univer_id,recom_region_id,
				recom_priority, recom_student_id)
	returning recom_id into rec_id;

	commit;
	status:='ok';
	exception
		when dup_val_on_index then
			status:='recom already exist';
		when others then
			status:=sqlerrm;
	END;

	end new_recom;


end recom_pkg;
