import datetime
import time

from model import *
from OracleDb import OracleDb

db = OracleDb()

session = db.sqlalchemy_session
'''

new_group = groups.add_group(GroupName='EL-1',
                               level='Elementary',
                               timetable='Пн-Ср(18:40-20:00',)
                               teachers='Anna K, Kate L',
                               Price=1800)

new_group = groups.add_group(GroupName='EL-2',
                               level='Elementary',
                               timetable='Пн-Чт(16:00-17:40',)
                               teachers='lauren, Mary S',
                               Price=1900)
                               
new_group = groups.add_group(GroupName='EL-3',
                               level='Elementary',
                               timetable='Пн-Ср-Пт (18:00-19:10',)
                               teachers='Anna K, Kate L',
                               Price=2000)
new_group = groups.add_group(GroupName='PreInt-1',
                               level='Pre-Intermediate',
                               timetable='Пн-Ср(18:40-20:00',)
                               teachers='Anna K, Kate L',
                               Price=2000) 
                               
new_group = groups.add_group(GroupName='PreInt-2',
                               level='Pre-Intermediate',
                               timetable='Пн-Чт(19:35-21:15',)
                               teachers='Jony A, Peter K',
                               Price=2200) 

new_group = groups.add_group(GroupName='Int-1',
                               level='Intermediate',
                               timetable='Вт-Пт(18:40-20:00',)
                               teachers='Anna O, Lisa L',
                               Price=2000) 
                               
new_group = groups.add_group(GroupName='Int-2',
                               level='Intermediate',
                               timetable='Пн-Чт(19:25-21:15',)
                               teachers='Conor, Kate T',
                               Price=2200) 

new_group = groups.add_group(GroupName='UpInt-1',
                               level='Upper-Intermediate',
                               timetable='Пн-Чт(19:25-21:15',)
                               teachers='Lisa, Kate R',
                               Price=2300)      
                               
new_group = groups.add_group(GroupName='UpInt-2',
                               level='Upper-Intermediate',
                               timetable='Пн-Ср-Пт(17:00-18:20',)
                               teachers='Lisa, Kate R',
                               Price=2500) 
            
new_group = groups.add_group(GroupName='Adv-1',
                               level='Advanced',
                               timetable='Пн-Чт(19:25-21:15',)
                               teachers='Peter, Kate S',
                               Price=2400)     
                               
new_group = groups.add_group(GroupName='Adv-1',
                               level='Advanced',
                               timetable='Вт-Чт(18:40-20:10',)
                               teachers='Lauren, Peter',
                               Price=2600) 
                                                                                                                              
new_student = students.add_student(name ='Кузьменко Олексій Петрович',
                               age = 12,
                               phone = 0674758621,
                               Email = oleksiy@gmail.com,
                               level = Elementary)
 
new_student = students.add_student(name ='Зубик Назар Васильович',
                               age = 10,
                               phone = 0974758621,
                               Email = zubyk123@gmail.com,
                               level = Elementary)                              

new_student = students.add_student(name ='Калинушка Кристина Юріївна',
                               age = 15,
                               phone = 0684757821,
                               Email = kk2005@gmail.com,
                               level = Pre-Intermediate)

new_student = students.add_student(name ='Данілова Анастасія Валеріївна',
                               age = 11,
                               phone = 0964778621,
                               Email = danilova.1505@gmail.com,
                               level = Elementary)
 
new_student = students.add_student(name ='Музика Дмитро Васильович',
                               age = 16,
                               phone = 0684758771,
                               Email = dima777@gmail.com,
                               level = Intermediate)  
                               
new_student = students.add_student(name ='Штойко Людмила Григорівна',
                               age = 17,
                               phone = 0975558673,
                               Email = shtoiko717@gmail.com,
                               level = Intermediate)

new_student = students.add_student(name ='Дубовий Олександр Петрович',
                               age = 15,
                               phone = 0960058620,
                               Email = o@gmail.com,
                               level = Intermediate)
                                                                                                                        
new_student = students.add_student(name ='Дудник Данило Русланович',
                               age = 12,
                               phone = 0680457800,
                               Email = dd2007@gmail.com,
                               level = Elementary)
                               
new_student = students.add_student(name ='Сідельник Ольга Петрівна',
                               age = 18,
                               phone = 0965020378,
                               Email = kisssa45@gmail.com,
                               level = Upper-Intermediate)                               
'''
session.commit()