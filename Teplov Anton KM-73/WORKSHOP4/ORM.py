#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from  database_connection import engine
from sqlalchemy.orm import sessionmaker
from DAO.models.models_create import Lessons,Groups, Student,Teacher, Audience, Schedule
from sqlalchemy import func

Session = sessionmaker(bind=engine)
session = Session()

group = Groups(
    name_g='KM-73',
    entrance_year=2017,
    grad_year=2021
)
session.add(group)
session.commit()



group_id = (session.query(Groups).filter(Groups.name_g == 'KM-73')[0]).Groups_id

student = Student(
    name='Anton',
    lastname='Teplov',
    group=group_id
)
session.add(student)
session.commit()


subject = session.query(Lessons).filter(Lessons.name_of_lesson == 'Math')
lessons = Lessons(
    name_of_lesson=subject
)
session.add(lessons)
session.commit()


teacher = Teacher(
    teacher_name='Elena',
    lastname='Temnikova'
)
session.add(teacher)
session.commit()

audience = Audience(
    building_num=15,
    audience_num=312,
    floor=3
)
session.add(audience)
session.commit()

lesson_id = (session.query(Lessons).filter(Lessons.name_of_lesson == 'Math')[0]).id_lesson
audience_id = (session.query(Audience).filter(Audience.audience_num == 312)[0]).Audience_id
group_id = (session.query(Groups).filter(Groups.name_g == 'KM-73')[0]).Groups_id
teacher_id = (session.query(Teacher).filter(Teacher.teacher_name == 'Elena').filter(Teacher.lastname == 'Temnikova')[0]).t_id

shedule = Schedule(
    lesson=lesson_id,
    audience=audience_id,
    term=1,
    group=group_id,
    teacher=teacher_id
)
session.add(shedule)
session.commit()

