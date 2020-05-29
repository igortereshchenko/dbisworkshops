#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms.student import StudentForm
from forms.score import ScoreForm
from forms.search_params import SearchForm
from forms.atestat import AtestatForm
from flask_bootstrap import Bootstrap




from task import Worker

# from dao import db_api
from orm.database_connection import ENGINE_PATH_WIN_AUTH
from orm.create_table import *
import psycopg2 as ps
import csv




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ENGINE_PATH_WIN_AUTH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sausage'

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
ts = Worker(db)

ts.delete_scores()
ts.delete_recoms()

@app.route('/', methods=['GET', 'POST'])
def index():
    form_student = StudentForm(request.form)
    form_score = ScoreForm(request.form)
    form_search = SearchForm(request.form)
    form_atestat = AtestatForm(request.form)
    student_scores = []
    result_search = []
    
    # allUsers = getUsers()
    

    if request.method == 'POST':
        if request.form.get('submit_student')=='Register':
            if form_student.validate():
                ts.register_student(request.form)
                session['student_id'] = ts.get_last_student_id()
                status = "Register student"
                return redirect(url_for('index'))
            

        elif request.form.get('submit_score')=='Add score':
            if session['student_id']:
                if form_score.validate():
                    ts.add_score(request.form,int(session['student_id']))
                    status='Added score'
                    return redirect(url_for('index'))

        elif request.form.get('submit_atestat')=='Add score':
            if session['student_id']:
                if form_atestat.validate():
                    form = {'score_name': 'Середній бал документа про освіту','score_value': request.form['atestat_value']}
                    ts.add_score(form,int(session['student_id']))
                    return redirect(url_for('index'))

        elif request.form.get('submit_search')=='Search':
            # print('in')
            # print(form_search.validate())  
            # print(form_search.errors)  
            if form_search.validate():
                print(request.form['search_region'],type(request.form['search_region']))
                results = ts.make_recomms(request.form,session['student_id'])
                if not results[0]:
                    status = results[1]
                    return redirect(url_for('error',status=status))
                else:
                    results = results[1]

                ts.add_recom_list(results,session['student_id'])
                return redirect(url_for('index'))
            else:
                status = "fail search"
    

    bar_graph = None 
     
    if 'student_id' in session:
        print(session['student_id'])
        student_scores = ts.get_scores(session['student_id'])
        result_search = ts.get_recom_list(session['student_id'])
        if result_search:
            print('inbargraph')
            bar_graph = ts.make_plot(result_search) 


            

    

    print(bar_graph)
    return render_template('index.html', form_student=form_student, 
                                        form_score=form_score,
                                        result_search=result_search,
                                        student_scores=student_scores,
                                        form_search=form_search,
                                        form_atestat=form_atestat,
                                        plot=bar_graph)


if __name__ == '__main__':
    app.run(debug=True)