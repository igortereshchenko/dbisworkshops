from flask import Flask, render_template, request, redirect, url_for
from forms import *
import datetime
from Models import *
from AI import AI

app = Flask(__name__)
app.config['SECRET_KEY'] = '6472674'
config = {"Desired_complexity": 3, "feature_id": -1}


@app.route('/')
def hello_world():
    return 'Для того чтоб сработал алгоритм предсказания сложности вам нужно использовать команду feature\n' \
           'Для смени сортировки по сложности complexity\n ' \
           'Походи виводится от самой подходящей сложности к менее'


@app.route('/api/<action>', methods=['GET'])
def apiget(action):
    if action == "complexity":
        return render_template("complexity.html")

    # if action == "hike":
    #     return render_template("hike.html")

    elif action == "feature":
        return render_template("feature.html")

    elif action == "all_hikes":
        if config["feature_id"] > 0:
            return render_template("all.html", select=AI.Serialise(AI.SortForID(int(config["feature_id"]),
                                                                                int(config["Desired_complexity"]))))
        else:
            return render_template("all.html", select=MasterSQL.Select(Hikes))

    elif action == "show_feature":
        return render_template("all.html", select=MasterSQL.Select(Feature))
    else:
        return render_template("404.html", action_value=action)


@app.route('/api/complexity', methods=['GET', 'POST'])
def api_complexity():
    form = DesiredComplexityForm()
    if form.is_submitted():
        result = request.form

        config["Desired_complexity"] = result["complexity"]
        return redirect(url_for('apiget', action="all_hikes"))
    return render_template('complexity.html', form=form)


# @app.route('/api/hike', methods=['GET', 'POST'])
# def api_hike():
#     form = HikeForm()
#     if form.is_submitted():
#         result = request.form
#
#         new_row = Hikes(
#             hike_name=result["hike_name"],
#             duration=result["duration"],
#             complexity=result["complexity"],
#             length=result["length"],
#             price=result["price"])
#
#         MasterSQL.Insert(new_row)
#         return redirect(url_for('apiget', action="all_hikes"))
#     return render_template('hike.html', form=form)


@app.route('/api/feature', methods=['GET', 'POST'])
def api_feature():
    form = FeatureForm()
    if form.is_submitted():
        result = request.form
        date = [int(i) for i in result["birth_date"].split('.')]

        new_row = Feature(birth_date=datetime.date(date[0], date[1], date[2]),
                          equipment=result["equipment"],
                          healthy=result["healthy"],
                          height=result["height"],
                          weight=result["weight"])

        MasterSQL.Insert(new_row)
        config["feature_id"] = new_row.feature_id
        return redirect(url_for('apiget', action="all_hikes"))
    return render_template('feature.html', form=form)


if __name__ == '__main__':
    app.run()
