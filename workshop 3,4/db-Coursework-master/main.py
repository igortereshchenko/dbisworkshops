from flask import Flask, render_template, request, make_response, session, url_for, redirect
from wtf.form.login import LoginForm
from wtf.form.Init_form import first_page
from wtf.form.user import UserForm
from datetime import datetime, timedelta
from wtf.form.Show_user import UserShow
from wtf.form.ShowTheme import ThemeShow
from wtf.form.ShowResourse import ResourseShow
from wtf.form.ShowInfo import InfoShow
from functions import *
import plotly
import plotly.graph_objs as go
import json


app = Flask(__name__)
app.secret_key = 'My_key'



@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    first_form = first_page()
    # global form
    if request.method == 'GET':
        if 'username' in session:
            username = session['username']
            return render_template("Index.html", form=first_form, nickname=username)
        else:
            username = request.cookies.get('login_cook')
            if username is None:
                return render_template("Index.html", form=first_form, nickname=username)
            return render_template("Index.html", form=first_form, nickname=username)
    if request.method == 'POST':
        is_exist = is_user(request.form['username'], request.form['password'])
        if is_exist == 0:
            result = 'This user doesn`t exist'
            return render_template('login.html', myform=form, result=result)
        if 'username' in session:
            username = session['username']
            return render_template("Index.html", form=first_form, nickname=username)
        else:
            username = request.cookies.get('login_cook')
            session['username'] = request.form['username']
            if username is None:
                if form.validate() == False:
                    return render_template('login.html', myform=form)
                else:
                    response = make_response(redirect(url_for('index')))
                    expires = datetime.now()
                    expires += timedelta(days=60)
                    response.set_cookie('login_cook', request.form['username'], expires=expires)
                    return response

            return render_template("Index.html", form=first_form, nickname=username)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', myform=form)


@app.route('/logout')
def logout():
    session.pop('username', None)

    response = make_response(redirect(url_for('index')))
    response.set_cookie('login_cook', '', expires=0)
    return response

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form_reg = UserForm()
    if request.method == 'POST':
        session['username'] = request.form['username']
        if form_reg.validate() == False:
            return render_template('user.html', myform=form_reg)
        else:
            result = add_user(
                u_nickname=request.form["username"],
                u_login=request.form["login"],
                u_pass=request.form["password"],
                u_name=request.form["name"],
                u_surname=request.form["surname"],
                u_faculty=request.form["faculty"],
                u_course=request.form["course"]
            )
            if result != 'ok':
                return render_template('user.html', myform=form_reg, result=result)
            response = make_response(redirect(url_for('registration')))
            expires = datetime.now()
            expires += timedelta(days=60)
            response.set_cookie('login_cook', request.form['username'], expires=expires)
            return response
    return render_template('user.html', myform=form_reg)

@app.route('/showUser', methods=['GET','POST'])
def show_user():
    formShow = UserShow()
    allUsers = getUsers()
    formShow.user_list.choices = [(int(allUsers.index(current)), current) for current in allUsers]
    if request.method == 'POST':
        if formShow.validate() == False:
            render_template('ShowUser.html', myform=formShow)
        else:
            nick = allUsers[int(request.form['user_list'])][0]
            del_user(
                u_nickname=nick)
            allUsers = getUsers()
            formShow.user_list.choices = [(int(allUsers.index(current)), current) for current in allUsers]
            return render_template('ShowUser.html', myform=formShow)
    return render_template('ShowUser.html', myform=formShow)


@app.route('/showTheme', methods=['GET', 'POST'])
def show_theme():
    formShow = ThemeShow()
    allTheme = get_theme()
    formShow.theme_list.choices = [(int(allTheme.index(current)), current) for current in allTheme]
    if request.method == 'POST':
        if formShow.validate() == False:
            render_template('ShowTheme.html', myform=formShow)
        else:
            if formShow.delete.data:
                theme_name = allTheme[int(request.form['theme_list'])][0]
                del_UhT(u_theme=theme_name, u_nick=session['username'])
                del_theme(
                    u_theme=theme_name)
                del_UhT(u_theme=theme_name, u_nick=session['username'])
                allTheme = get_theme()
                formShow.theme_list.choices = [(int(allTheme.index(current)), current[0]) for current in allTheme]
                return render_template('ShowTheme.html', myform=formShow)
            if formShow.add.data:
                result = add_theme(
                    u_theme=request.form["theme"]
                )
                if result!='ok':
                    return render_template('ShowTheme.html', myform=formShow, result=result)
                result=add_UhT(u_nick=session['username'], u_theme=request.form["theme"])
                if result!='ok':
                    return render_template('ShowTheme.html', myform=formShow, result=result)
                session['lection_theme'] = request.form["theme"]
                allTheme = get_theme()
                formShow.theme_list.choices = [(int(allTheme.index(current)), current[0]) for current in allTheme]
                result = 'you choose ' + session['lection_theme']
                return render_template('ShowTheme.html', myform=formShow, result=result)
            if formShow.update.data:
                theme_name = allTheme[int(request.form['theme_list'])][0]
                result = update_UhT(new_theme=request.form["theme"],
                    old_theme=theme_name)
                if result!='ok':
                    return render_template('ShowTheme.html', myform=formShow, result=result)
                result = update_theme(
                    new_theme=request.form["theme"],
                    old_theme=theme_name
                )
                if result!='ok':
                    return render_template('ShowTheme.html', myform=formShow, result=result)
                allTheme = get_theme()
                formShow.theme_list.choices = [(int(allTheme.index(current)), current[0]) for current in allTheme]

                return render_template('ShowTheme.html', myform=formShow)
            if formShow.choose.data:
                theme_name = allTheme[int(request.form['theme_list'])][0]
                session['lection_theme'] = theme_name
                result = 'you choose ' + session['lection_theme']
                return render_template('ShowTheme.html', myform=formShow, result=result)
            if formShow.filtering.data:
                allTheme = get_theme(request.form["theme"])
                formShow.theme_list.choices = [(int(allTheme.index(current)), current[0]) for current in allTheme]
                return render_template('ShowTheme.html', myform=formShow)
    return render_template('ShowTheme.html', myform=formShow)




@app.route('/showResourse', methods=['GET', 'POST'])
def show_resourse():
    formShow = ResourseShow()
    allResourse = get_resourse()
    formShow.resourse_list.choices = [(int(allResourse.index(current)), current) for current in allResourse]
    if request.method == 'POST':
        if formShow.validate() == False:
            render_template('ShowResourse.html', myform=formShow)
        else:
            if formShow.delete.data:
                resourse = allResourse[int(request.form['resourse_list'])][0]
                del_UhR(u_resourse=resourse, u_nick=session['username'])
                del_resourse(
                    u_resourse=resourse)
                allResourse = get_resourse()
                formShow.resourse_list.choices = [(int(allResourse.index(current)), current[0]) for current in allResourse]
                return render_template('ShowResourse.html', myform=formShow)
            if formShow.add.data:
                result = add_resourse(
                    u_resourse=request.form["resourse"]
                )
                if result!='ok':
                    return render_template('ShowResourse.html', myform=formShow, result=result)
                result = add_UhR(u_nick=session['username'], u_resourse=request.form["resourse"])
                if result!='ok':
                    return render_template('ShowResourse.html', myform=formShow, result=result)
                session['resourse'] = request.form["resourse"]
                allResourse = get_resourse()
                formShow.resourse_list.choices = [(int(allResourse.index(current)), current[0]) for current in allResourse]
                result = 'you choose ' + session['resourse']
                return render_template('ShowResourse.html', myform=formShow, result=result)
            if formShow.update.data:
                resourse = allResourse[int(request.form['resourse_list'])][0]
                result = update_UhR(new_resourse=request.form["resourse"],
                    old_resourse=resourse)
                if result!='ok':
                    return render_template('ShowResourse.html', myform=formShow, result=result)
                result = update_resourse(
                    new_resourse=request.form["resourse"],
                    old_resourse=resourse
                )
                if result!='ok':
                    return render_template('ShowResourse.html', myform=formShow, result=result)
                allResourse = get_resourse()
                formShow.resourse_list.choices = [(int(allResourse.index(current)), current[0]) for current in allResourse]
                return render_template('ShowResourse.html', myform=formShow)
            if formShow.choose.data:
                theme_name = allResourse[int(request.form['resourse_list'])][0]
                session['resourse'] = theme_name
                result = 'you choose ' + session['resourse']
                return render_template('ShowResourse.html', myform=formShow, result=result)
            if formShow.filtering.data:
                allResourse = get_resourse(request.form["resourse"])
                formShow.resourse_list.choices = [(int(allResourse.index(current)), current[0]) for current in
                                                  allResourse]
                return render_template('ShowResourse.html', myform=formShow)
    return render_template('ShowResourse.html', myform=formShow)


@app.route('/showInfo', methods=['GET','POST'])
def show_info():
    formShow = InfoShow()
    allInfo = get_information()
    formShow.info_list.choices = [(int(allInfo.index(current)), current) for current in allInfo]
    if request.method == 'POST':
        if formShow.validate() == False:
            render_template('ShowInfo.html', myform=formShow)
        else:
            if formShow.delete.data:
                nick = allInfo[int(request.form['info_list'])][1]
                inf_id = allInfo[int(request.form['info_list'])][0]
                del_info(
                    i_nickname=nick,
                    i_id=inf_id
                )
                allInfo = get_information()
                formShow.info_list.choices = [(int(allInfo.index(current)), current) for current in allInfo]
                return render_template('ShowInfo.html', myform=formShow)
            if formShow.add.data:
                result = add_info(
                    i_nickname=session['username'],
                    i_lec_name=session['lection_theme'],
                    i_resourse=session['resourse'],
                    i_link=request.form['info']
                )
                if result != 'ok':
                    return render_template('ShowInfo.html', myform=formShow, result=result)
                allInfo = get_information()
                formShow.info_list.choices = [(int(allInfo.index(current)), current) for current in allInfo]
                return render_template('ShowInfo.html', myform=formShow, result=result)
            if formShow.filtering.data:
                allInfo = get_information(request.form['filter_n'], request.form['filter_T'])
                formShow.info_list.choices = [(int(allInfo.index(current)), current) for current in allInfo]
                return render_template('ShowInfo.html', myform=formShow)


    return render_template('ShowInfo.html', myform=formShow)

@app.route('/showStat', methods=['GET','POST'])
def show_stat():
    first_stat = get_res()
    second_stat = get_res_1()
    labels = [str(cur[0])+' course' for cur in second_stat]
    values = [cur[1] for cur in second_stat]
    course_res=go.Pie(labels=labels, values=values)

    count_res =go.Bar(
        x=[cur[0] for cur in first_stat],
        y=[cur[1] for cur in first_stat]
    )
    dataPie = [course_res]
    dataBar = [count_res]
    graphJSONbar = json.dumps(dataBar, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSONPie = json.dumps(dataPie, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('statistic.html', graphJSONbar=graphJSONbar, graphJSONPie=graphJSONPie)


if __name__ == '__main__':
    app.run(debug=True)
