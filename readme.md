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

Для конвертирования формата Postman:

```
python postman.py > postman1.json
npm install postman-collection-transformer
node_modules/.bin/postman-collection-transformer convert -i postman1.json -o postman2.json -j 1.0.0 -p 2.0.0 -P
```
