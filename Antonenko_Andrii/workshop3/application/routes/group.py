from flask import request, render_template, redirect, abort
from datetime import datetime as dt
from flask import current_app as app
from ..models import Group
from .. import db
from ..forms import GroupForm


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
    groups = db.session.query(Group)
    form = GroupForm()
    return render_template('groups.jinja2', groups=groups, form=form)
