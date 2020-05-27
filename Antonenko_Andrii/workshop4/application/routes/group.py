from flask import request, render_template, redirect, abort, jsonify
from datetime import datetime as dt
from flask import current_app as app
from ..models import Group, User, User_Group
from .. import db
from ..forms import GroupForm, AddUserToGroup


@app.route('/group', methods=['POST'])
def create_group():
    """Create a group via query string parameters."""
    name = request.form['name']
    if name:
        existing_group = Group.query.filter(Group.name == name).first()
        if existing_group:
            return abort(400, 'Group with such name already exist')

        new_group = Group(name=name, created=dt.now())

        db.session.add(new_group)
        db.session.commit()
    return redirect('/group')


@app.route('/group', methods=['GET'])
def get_all_groups():
    groups = Group.query.join(User, Group.users, isouter=True).all()
    form = GroupForm()
    return render_template('groups.jinja2', groups=groups, form=form)


@app.route('/group/add-user', methods=['GET'])
def get_add_user_to_group_template():
    form = AddUserToGroup()
    return render_template('add_user_to_group.jinja2', form=form)


@app.route('/group/add-user', methods=['POST'])
def add_user_to_group():
    user_email = request.form['user_email']
    group_name = request.form['group_name']
    role = request.form['role']

    if user_email and group_name and role:
        existing_group = Group.query.filter(Group.name == group_name).first()
        existing_user = User.query.filter(User.email == user_email).first()
        if not existing_user:
            return abort(400, 'Wrong user email')

        if not existing_group:
            return abort(400, 'Wrong group name')

        new_user_group = User_Group(user_id=existing_user.id,
                                    group_id=existing_group.id,
                                    role=role)
        db.session.add(new_user_group)
        db.session.commit()
    return redirect('/group')


@app.route('/group/<group_id>', methods=['DELETE'])
def delete_group(group_id):
    # We need to add CASCADE deleting instead of
    db.session.query(User_Group).filter(User_Group.group_id == int(group_id)).delete()
    db.session.query(Group).filter(Group.id == int(group_id)).delete()
    db.session.commit()

    return jsonify(redirect=request.host + '/group'), 201

#
# @app.route('/group/<group_id>', methods=['PUT'])
# def update_group(group_id):
#     name = request.form['name']
#     if group_id:
#         db.session.query(Group).filter(Group.id == int(group_id)).update({name: name})
#         db.session.commit()
#     return jsonify(redirect=request.host + '/group'), 201
#
#
# @app.route('/group_update/<group_id>', methods=['GET'])
# def group_update_page(group_id):
#     form = GroupForm()
#     group = Group.query.get(group_id)
#     form.name.data = group.name
#     return render_template(
#         'update_group.jinja2',
#         form=form,
#         update_url='http://' + request.host + '/group/' + str(group_id)
#     )
