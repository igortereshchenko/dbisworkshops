from flask import Flask, render_template, request,  redirect, url_for
from classes import *
from oracledb import OracleDb

import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

app = Flask(__name__)

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

engine = create_engine(oracle_connection_string.format(

    username="SYSTEM",
    password="0000",
    sid="XE",
    host="localhost",
    port="1521",
    database="workshop5",
), echo=True)

Session = sessionmaker(bind=engine)
session = Session()

@app.route('/home', methods = ['GET'])
@app.route('/', methods = ['GET'])
def start_page():
    return render_template("main.html")
    
@app.route('/notes/<int:id>/delete')
def note_delete(id):
        note = session.query(Note).get(id)
        session.delete(note)
        session.commit()
        return redirect(url_for('actinfo', action="note"))
    
@app.route('/notes/<int:id>/update', methods=['POST', 'GET'])
def note_update(id):
    if request.method == "POST":
        note.name = request.form['name']
        note.Description = request.form['Description']
        session.commit()
    else:
        note = session.query(Note).get(id)
        return render_template("update_note.html", note=note)

    
@app.route('/<action>', methods = ['GET'])
def actinfo(action):
    if action == "note":
        session = db.sqlalchemy_session
        notes = session.query(Note).all()
        return render_template("note.html", notes=notes)


@app.route('/create_note', methods = ['POST', 'GET'])
def create_note():
    if request.method == "POST":
        name = request.form['name']
        Description = request.form['Description']
        note = Note(name = name, Description = Description)
        try:
            session.add(note)
            session.commit()
            return redirect(url_for('actinfo', action="note"))
        except:
            return "Произошла ошибка"
    else:
        return render_template("create_note.html")

@app.route('/graf.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    users = session.query(Country).all()
    notes = session.query(Users).all()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig


if __name__ == '__main__':

    app.run(use_reloader=False, debug=True)

