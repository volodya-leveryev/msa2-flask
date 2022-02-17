from flask import json

from app import app, api

with app.app_context():
    urlvars = False  # Build query strings in URLs
    swagger = True  # Export Swagger specifications
    data = api.as_postman(urlvars=urlvars, swagger=swagger)
    print(json.dumps(data))
