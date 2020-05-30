from flask import Flask, render_template, request,flash, session
from flask_sqlalchemy import SQLAlchemy
import sys
import json
import plotly
import plotly.graph_objs as go
from orm.create_table import *


class Worker():
      def __init__(self,db):
            self.db = db

      def make_plot(self,results):
            # y = [self.]
            user_scores = [row['student_score'] for row in results]
            recom_scores = [row['average_score'] for row in results] 
            fig = go.Figure(data=[go.Bar(
                name="Student's score",
                y=user_scores
                
            ),go.Bar(
                name="Position score",
                y=recom_scores
                
            )])
            fig.update_layout(barmode='group',width=500,height=500,)

            graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            return graphJSON

      def register_student(self,form):
            
            try:
                  self.db.session.add(Students(student_name=form['student_name'],
                                          student_sex=form['student_sex'],
                                          student_abitur=bool(int(form['student_abitur']))))
                  self.db.session.commit()
                  print('New students added to db')
            except:
                  print("Unexpected error with added student:", sys.exc_info()[0])

     
      def get_last_student_id(self):
            try:
                  return self.db.session.query(Students).order_by(Students.student_id.desc()).first().student_id
            
            except:
                  print("Unexpected error:", sys.exc_info()[0])
                       
     
      def add_score(self,form,student_id):
            try:      
                  self.db.session.add(Zno_Scores(zno_score_name=form['score_name'],
                                                zno_score_value=form['score_value'],
                                                zno_score_student_id=student_id))
                  self.db.session.commit()
                  print('Add a new score')
            except:
                  print("Unexpected error:", sys.exc_info()[0])

     
      def get_scores(self,student_id):
       
            try:
                  return self.db.session.query(Zno_Scores).filter_by(zno_score_student_id=student_id).all() 
            except:
                  print("Unexpected error:", sys.exc_info()[0])

      def delete_scores(self):
            try:
                  self.db.session.query(Zno_Scores).delete()
                  self.db.session.commit()
                  print('Cleared scores')
            except:
                  print("Unexpected error:", sys.exc_info()[0])

      def delete_recoms(self):
            try:
                  self.db.session.query(Recom_List).delete()
                  self.db.session.commit()
                  print('Cleared recoms')
            except:
                  print("Unexpected error")

      def make_recomms(self,form,student_id):
            result_query = self.db.session.query(Zno_Scores).filter_by(zno_score_student_id = student_id).all()
            subjects = {}
            for row in result_query:
                  if row.zno_score_name=='Середній бал документа про освіту':
                        subjects[row.zno_score_name] = float(row.zno_score_value)*200/12
                  else:
                        subjects[row.zno_score_name] = float(row.zno_score_value)
           
            result_query = self.db.session.query(Recom_Base).filter_by(recom_specialty_id=int(form['search_specialty']),
                                                recom_region_id=int(form['search_region'])).all()
            if not result_query:
                  return False,"Didn't find any position"

            rows = self.valid_subjects(subjects,result_query)
            if not rows:
                  return False,"Failed search, check pls your subjects and values"

            means = self.calculate_mean(rows,subjects)
            sorted_means = sorted(means, key=lambda x: float(x[0].recom_average_score)-x[1])
            # print('mean',means)
            return True,means[:7]

      def calculate_mean(self,rows,subjects):
            rows_means = []
            for row in rows:
                  res = {}
                  mean = 0.0
                  keys = ['subject_name','koef','min_score']
                  for id_key in row.recom_subjects.keys():
                        #find min score specialty koef
                        if row.recom_subjects[id_key]['min_score']!='None':
                              min_score = float(row.recom_subjects[id_key]['min_score'].split(' ')[1])    
                        else:
                              min_score = 0.0 
                        #find koef
                        koef = float(row.recom_subjects[id_key]['koef'].split('=')[1])
                        #find subject_name
                        subject_name = row.recom_subjects[id_key]['subject_name'].replace(' (ЗНО)','')
                        res[subject_name]={'koef':koef,'min_score':min_score}
                  #get names of user's subjects 
                  user_subjects_keys = list(subjects.keys()) 
                  #get names of competion subjects
                  subj_keys = list(res.keys())
                  #get must have subjects and optional
                  must_subj,option_subj = self.get_must_option_subj(subj_keys)
                  # print('res',res)
                  # print('user_subjects_keys',user_subjects_keys)
                  # print('subj_keys',subj_keys)
                  # print('must_subj,option_subj',must_subj,option_subj)
                  for subj_name in must_subj:
                        if subjects[subj_name]<res[subj_name]['min_score']:
                              mean = 0.0
                              break
                        else:
                              mean += subjects[subj_name]*res[subj_name]['koef']
                              
                  if mean:
                        for subj_name in set(option_subj)&(set(user_subjects_keys)-set(must_subj)):

                              if subjects[subj_name]<res[subj_name]['min_score']:
                                    mean = 0.0
                                    break
                              else:
                                    mean += subjects[subj_name]*res[subj_name]['koef']
                              
                  rows_means.append((row,mean))
            return rows_means
     

      def valid_subjects(self, student_subjects, result_query):
            # result_query = self.valid_names_subjects(student_subjects,result_query)
            res = []
            for row in result_query:
                  
                  if self.valid_names_subjects(student_subjects, row):
                        # print('True valid_names_subjects')
                        res.append(row)    
                  else:
                        continue
            return res

      def valid_names_subjects(self,student_subjects, row):
            names = list(student_subjects.keys())
            subj_keys = [row.recom_subjects[key]['subject_name'].replace(' (ЗНО)','') for key in row.recom_subjects.keys()]
            # print(' names', names)
            # print('subject names', subj_keys)
            must, opti = self.get_must_option_subj(subj_keys)
            if set(must)&set(names)==set(must):
            
                  if set(opti)&(set(names)-set(must)):
                        return True

                  else:
                        return False
            else:
                  return False



      def get_must_option_subj(self,subj_keys):
            '''find must have subjects and optional subjects in specialty and return them'''
            must_have_subj = subj_keys[:2]
            subj_keys = subj_keys[2:]

            if 'Творчий конкурс' in subj_keys:
                  must_have_subj +=['Творчий конкурс']
                  subj_keys.remove('Творчий конкурс')
            
            if 'Середній бал документа про освіту' in subj_keys:
                  must_have_subj +=['Середній бал документа про освіту']
                  subj_keys.remove('Середній бал документа про освіту')

            optional_subj = list(set(subj_keys)-set(must_have_subj))

            return must_have_subj,optional_subj

      def add_recom_list(self,results,student_id):
            try:
                  for row in results:
                        self.db.session.add(Recom_List(recom_id=row[0].id,
                                                      recom_student_id=student_id,
                                                      student_score=row[1],
                                                      recom_crit=row[0].recom_average_score-row[1]))
                  self.db.session.commit()
            except Exception as e:
                  print('Error when add recom list: ',e)

      def get_recom_list(self,student_id):
            try:
                  res_query = self.db.session.query(Recom_List,Recom_Base,Regions,Univers,Specialties).\
                  filter(Recom_List.recom_student_id==student_id).\
                  filter(Recom_Base.id == Recom_List.recom_id).\
                  filter(Regions.region_id==Recom_Base.recom_region_id).\
                  filter(Univers.univer_id==Recom_Base.recom_univer_id).\
                  filter(Specialties.specialty_id==Recom_Base.recom_specialty_id).all()
                  # print(dir(res_query))
                  # print(dir(res_query[0]))
                  results = []
                  for row in res_query:
                        results.append({})
                        results[-1]['region_name'] = row.Regions.region_name
                        results[-1]['univer_name'] = row.Univers.univer_name
                        results[-1]['specialty_name'] = row.Specialties.specialty_name
                        results[-1]['faculty_name'] = row.Recom_Base.recom_faculty_name
                        results[-1]['average_score'] = row.Recom_Base.recom_average_score
                        results[-1]['student_score'] = row.Recom_List.student_score
                        # print(row.Recom_Base.recom_subjects)
                  results = sorted(results,key=lambda x: x['average_score']-x['student_score'])
                  for i,row in enumerate(results):
                        row['priority']=i+1
                  return results
            except Exception as e:
                  print('Error when get recom list:',e)