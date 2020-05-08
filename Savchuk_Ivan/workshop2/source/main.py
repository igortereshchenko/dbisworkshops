from flask import Flask, render_template, request, redirect, url_for
from forms import EntityForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '28th43'


@app.route('/api/<action>', methods=['GET'])
def apiget(action):
    if action == "cat":
        return render_template("cat.html", cat=cat_dict)

    elif action == "dog":
        return render_template("dog.html", dog=dog_dict)

    elif action == "all":
        return render_template("all.html", cat=cat_dict,
                               dog=dog_dict)

    else:
        return render_template("404.html", action_value=action)


@app.route('/api/cat', methods=['GET', 'POST'])
def api_cat():
    form = EntityForm()
    if form.is_submitted():
        result = request.form
        cat_dict['pet_name'] = result['pet_name']
        cat_dict['color'] = result['color']
        cat_dict['height(cm)'] = result['height']
        cat_dict['weight(kg)'] = result['weight']
        cat_dict['ability'] = result['ability']
        return redirect(url_for('apiget', action="all"))
    return render_template('cat.html', form=form)


@app.route('/api/dog', methods=['GET', 'POST'])
def api_dog():
    form = EntityForm()
    if form.is_submitted():
        result = request.form
        dog_dict['pet_name'] = result['pet_name']
        dog_dict['color'] = result['color']
        dog_dict['height(cm)'] = result['height']
        dog_dict['weight(kg)'] = result['weight']
        dog_dict['ability'] = result['ability']
        return redirect(url_for('apiget', action="all"))
    return render_template('dog.html', form=form)


if __name__ == '__main__':
    # Створення словників на сервері
    # Словники містять інформацію про сутності кота та собаки
    cat_dict = {'pet_name': 'Gosha',
                'color': 'grey',
                'weight(kg)': 6,
                'height(cm)': 25,
                'ability': 'meowing'}
    dog_dict = {'pet_name': 'Dollar',
                'color': 'brown',
                'weight(kg)': 13,
                'height(cm)': 40,
                'ability': 'barking'}
    app.run()
