## Install:
1) Install into virtual environment requirements: ```pip install -r reqiurements.txt```
<br>
2) Init flask migrations: ```flask db init```
<br>

## Run

###1) Run DB migration:
(if db models changed and auto-migration does'nt work)
<br>
1)``` flask db migrate```
<br>
2)```flask db upgrade```

###2) Run app
```(venv) python run.py```<br> or <br>
 ```set  FLASK_APP=app.py```<br> ```flask run```


## Testing:
Run tests: ```python -m pytest``` (from root directory)