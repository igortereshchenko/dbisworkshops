from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/api/<action>', methods=['GET'])
def get_api(action):
    if action == "doctor":
        return render_template("doctors.html", doctor=doc_dict)
    elif action == "patient":
        return render_template("patient.html", patient=patient_dict)
    elif action == "all":
        return render_template("all.html", doctor=doc_dict, patient=patient_dict)
    else:
        return render_template("404.html", action_value=action)


@app.route('/api/doctor/submit', methods=['POST'])
def user_submit():
    if request.method == 'POST':
        return str("Doctor ID: ") + str(request.form['doc_id']) + "<br>"\
               + str("First name: ") + str(request.form['first_name']) + "<br>"\
               + str("Last name: ") + str(request.form['last_name']) + "<br>"\
               + str("Specialization: ") + str(request.form['spec'])


@app.route('/api/patient/submit', methods=['POST'])
def question_submit():
    if request.method == 'POST':
        return str("Question ID: ") + str(request.form['patient_id']) + "<br> "\
               + str("First name: ") + str(request.form['first_name']) + "<br> "\
               + str("Last name: ") + str(request.form['first_name']) + "<br> "\
               + str("Street: ") + str(request.form['first_name']) + "<br> "\
               + str("Year of birth: ") + str(request.form['last_name'])

if __name__ == '__main__':
    doc_dict = {
        "doc_id": "98213728",
        "first_name": "Olga",
        "last_name": "Petrenko",
        "spec": "pediatrician",
    }
    patient_dict = {
        "patient_id": "21343224",
        "first_name": "Petro",
        "last_name": "Golovin",
        "street": "Tarasa Shevchenko 3",
        "year_birth": "2000/02/13",
    }

    app.run(port=5001, debug=True)