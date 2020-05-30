import cx_Oracle

from db import OracleDb as OD 

db_oracle = OD()

def newUser(student_name,student_abitur,student_sex):

    student_id = db_oracle.cursor.var(cx_Oracle.NATIVE_INT)
    status = db_oracle.cursor.var(cx_Oracle.STRING)

    db_oracle.cursor.callproc("student_auth.new_student", [student_id, status,student_name,student_abitur,student_sex])
    db_oracle.cursor.close()
    db_oracle.connection.close()

    return student_id.getvalue(), status.getvalue()


def newRecom(recom_specialty_id,
			recom_univer_id,recom_region_id,
			recom_priority, recom_student_id):

    recom_id = db_oracle.cursor.var(cx_Oracle.NATIVE_INT)
    status = db_oracle.cursor.var(cx_Oracle.STRING)

    db_oracle.cursor.callproc("recom_pkg.new_recom", [recom_id, status,recom_specialty_id,
				recom_univer_id,recom_region_id,
				recom_priority, recom_student_id])
    db_oracle.cursor.close()
    db_oracle.connection.close()

    return recom_id.getvalue(), status.getvalue()

   