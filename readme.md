# Flask-RestFul example project

## Как начать работу

```
git clone https://github.com/volodya-leveryev/msa2-flask
cd msa2-flask
python -m venv venv
venv\scripts\activate.bat
pip install -r requirements.txt
set FLASK_APP=app
set FLASK_ENV=development
flask run
```

Для внесения изменений в структуру БД:

```
flask db migrate
flask db upgrade
``````
