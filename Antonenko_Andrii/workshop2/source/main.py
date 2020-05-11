from flask import Flask, render_template, request, redirect, url_for
from form import UserForm, DashboardForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_key'


@app.route('/api/<action>', methods=['GET'])
def get_template(action):
    if action == 'user':
        return render_template('user.html', user=user_dict)
    elif action == 'dashboard':
        return render_template('dashboard.html', dashboard=dashboard_dict)
    elif action == 'all':
        return render_template('all.html', user=user_dict, dashboard=dashboard_dict)
    else:
        return render_template('404.html', action_value=action)


@app.route('/api/user', methods=['GET', 'POST'])
def api_user():
    form = UserForm()
    if form.is_submitted():
        result = request.form
        user_dict['id'] = result['user_id']
        user_dict['firstName'] = result['user_first_name']
        user_dict['lastName'] = result['user_last_name']
        user_dict['email'] = result['user_email']
        return redirect(url_for('get_template', action="all"))
    return render_template('user.html', form=form)


@app.route('/api/dashboard', methods=['GET', 'POST'])
def api_dashboard():
    form = DashboardForm()
    if form.is_submitted():
        result = request.form
        dashboard_dict['id'] = result['dashboard_id']
        dashboard_dict['name'] = result['dashboard_name']
        dashboard_dict['userId'] = result['dashboard_user_id']
        return redirect(url_for('get_template', action="all"))
    return render_template('dashboard.html', form=form)


if __name__ == '__main__':
    user_dict = {
        'id': 'uuid',
        'firstName': 'Super',
        'lastName': 'User',
        'email': 'super.user@gmail.com',
        'passwordHash': 'jdhiuhkjhqwidhksjhaiudhqwd'
    }
    dashboard_dict = {
        'id': 'dashboard_uuid',
        'name': 'Great project 1',
        'userId': 'uuid',
    }

    app.run()
