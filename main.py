from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import *

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Instanciando banco de dados
db = SQLAlchemy(app)

from views import * 

if __name__ == '__main__':    
    app.run(debug=True)