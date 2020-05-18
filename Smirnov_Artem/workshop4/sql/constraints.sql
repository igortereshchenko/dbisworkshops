alter table zno_scores
add constraint zno_scores_fk foreign key (zno_score_student_id)
				references students(student_id);

alter table  recom_list
add constraint recom_list_spec_fk foreign key (recom_specialty_id)
				references specialties(specialty_id);

alter table recom_list
add constraint recom_list_uni_fk foreign key (recom_univer_id)
				references univers(univer_id);

alter table recom_list
add constraint recom_list_reg_fk foreign key (recom_region_id)
				references regions(region_id);

alter table recom_list
add constraint recom_student_id_fk foreign key (recom_student_id)
				references students(student_id);
