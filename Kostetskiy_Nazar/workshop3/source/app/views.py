from app import app
from flask import request, jsonify, render_template, redirect, url_for
from app.db_models import User, UserPost

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required
from app import login_manager

API = '/api'


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))


@app.route('/')
def index():
    return render_template('index.html')


@app.route(f'{API}/login', methods=['POST'])
def login():
    data = request.get_json()
    if current_user.is_authenticated:
        app.logger.info('Current user already authenticated')
        return jsonify(msg='Already authenticated', result=False), 200
    if data:
        app.logger.info('Login with data: {}'.format(data))
        email = data.get('email')
        password = data.get('password')
        user = User.find(email=email)
        if user and password:
            if check_password_hash(user.password, password):
                login_user(user)
                return jsonify(msg='Authenticated', data=user.get_data(), result=True),  200
            else:
                return jsonify(msg='Invalid password', result=False), 200
        else:
            return jsonify(msg='User does not exists', result=False), 200

    return jsonify(msg='Invalid credentials', result=False), 401


# TODO
@app.route(f'{API}/user/', methods=['POST', 'GET'])
def get_user_info():
    if request.method == 'GET':
        pass
    elif request.method == 'Post':
        pass


@app.route(f'{API}/posts/create')
@login_required
def create_post():
    data = request.get_json()
    app.logger.info('Creating post')
    if data:
        user_id = current_user.id
        body = data.get('text')
        price = data.get('price')
        if user_id and body and price:
            post = UserPost.create(body=body, user_id=user_id, price=price)
            return jsonify(data={'id': post.id, **data}, result=True), 200
        return jsonify(result=False, msg='Invalid data'), 200
    else:
        return jsonify(result=False), 200


@app.route(f'{API}/posts')
def get_all_posts():
    return {'result': True, 'data': [user.to_json() for user in UserPost.get_all()]}, 200


@app.route(f'{API}/logout', methods=['GET'])
@login_required
def logout():
    app.logger.info('User {} logged out'.format(current_user))
    logout_user()
    return render_template('index.html')


@app.route(f'{API}/register', methods=['POST', 'GET'])
def register():
    data = request.get_json()
    app.logger.info('Trying to register user')
    if data:
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        if username and password and email:
            if not User.find(email=email):
                password = generate_password_hash(password)
                user = User.create(username=username, password=password,  email=email)
                if user:
                    login_user(user)
                    return jsonify(data=user.get_data(), result=True), 200
            else:
                return jsonify(msg='User with this email already exists', data={}, result=False), 200

    return jsonify(msg='Invalid data', result=False), 400


@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html')