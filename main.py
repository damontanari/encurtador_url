from flask import Flask, jsonify
from sqlalchemy.dialects.postgresql import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Instanciando banco de dados
db = SQLAlchemy(app)

from views import * 

if __name__ == '__main__':    
    app.run(debug=True)