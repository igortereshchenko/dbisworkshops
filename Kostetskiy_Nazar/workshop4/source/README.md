<h2>Install</h2>
1) Install into virtual environment requirements: ```pip install -r reqiurements.txt```
<br>
2) Init flask migrations: ```flask db init```
<br>

<h2>Run migrations</h2>

```flask db migrate```
<br>
```flask db upgrade```

<h2>Run app on localhost</h2>
```(venv) python run.py```
<br>
or
<br>

 ```set  FLASK_APP=app.py```<br> ```flask run```

<h2>Testing</h2>
Run tests: ```python -m pytest``` (from root directory)