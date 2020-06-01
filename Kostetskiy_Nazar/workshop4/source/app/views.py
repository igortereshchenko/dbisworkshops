from app import app, socketio
from flask import request, render_template, redirect, url_for
from app.db_models import User, UserPost
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required
from app import login_manager
from app.socket_events import SocketEvent
from app.static_data import ALL_STATIC_POSTS

API = '/api'


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/faq')
def faq_page():
    return render_template('faq.html')


# User requests
@app.route(f'/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        app.logger.info('Current user already authenticated')
        return redirect(url_for('index_page'))
    elif request.method == 'GET':
        return render_template('sign_in.html')
    else:
        data = request.form.to_dict()
        app.logger.info(f'Trying to login user with data: {data}')  # Todo: remove password in logs
        if data:
            email = data.get('email')
            password = data.get('password')
            user = User.find(email=email)
            if user and password:
                if check_password_hash(user.password, password):
                    login_user(user)
                    return redirect(url_for('index_page'))
                else:
                    return render_template('sign_in.html')
            else:
                return render_template('sign_in.html')
        return render_template('sign_in.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    data = request.form.to_dict()
    app.logger.info(f'Trying to register user with data: {data}')  # Todo: remove password in logs
    if request.method == 'GET':
        return render_template('sign_up.html')
    else:
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
                        return redirect(url_for('index_page'))
                else:
                    return render_template('sign_up.html')
        return render_template('sign_up.html')


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    app.logger.info('User {} logged out'.format(current_user))
    logout_user()
    return redirect(url_for('index_page'))


# TODO
@app.route(f'/user/<user_id>', methods=['GET'])
def get_user_info(user_id):
    user = User.find(id=user_id)
    if user:
        user = user.get_data()
        return render_template('user.html', user=user)
    return '<h1>Code 404</h1>Page not found', 404


# Todo: remove static data
@app.route('/posts', methods=['GET'])
def posts():
    all_posts = [*ALL_STATIC_POSTS, *UserPost.get_all()]
    return render_template('posts.html', all_posts=all_posts)


@app.route('/create_post',  methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'GET':
        return render_template('create_post.html')
    else:
        data = request.form.to_dict()
        app.logger.info('Creating post with data: ', data)
        if data:
            user_id = current_user.id
            body = data.get('text')
            price_usd = data.get('price_usd')
            position = data.get('position')
            if user_id and body and price_usd:
                date = datetime.now()
                post = UserPost.create(body=body, position=position, user_id=user_id,
                                       price_usd=price_usd, created_at=date,
                                       last_update=date)

                all_posts = [*ALL_STATIC_POSTS, *UserPost.get_all()]
                return render_template('posts.html',  all_posts=all_posts)
        return 'Invalid data', 400


@app.route(f'{API}/posts')
def get_all_posts():
    return {'result': True, 'data': [user.to_json() for user in UserPost.get_all()]}, 200


@socketio.on(SocketEvent.EVT_GET_POSTS_REQ, namespace='/board')
def get_posts(msg):
    pass


@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html')