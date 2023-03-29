from flask import render_template, jsonify, redirect, flash, url_for, request
import pyshorteners
from main import app, db
from models import encurta_link
import random

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/encurtar', methods=['POST'])
def encurtar_url():
    if request.method == 'POST':
        url = request.form.get('site')
        link = pyshorteners.Shortener()
        code = ''
        for i in range(7):
            random_num = random.randint(65, 90)
            code += chr(random_num)  
        shorten_url = link.tinyurl.short(url)
        armazena = encurta_link(link=url, link_encurtado=code)
        # Inserindo novo jogo no banco de dados
        db.session.add(armazena)
        db.session.commit()
        return render_template('url_encurtado.html', url_encurtada=code)
    
@app.route('/api', methods=['GET'])
def retorno_api():
    code = request.args.get('code', default = '*', type = str)
    print(code)
    url = encurta_link.query.filter_by(link_encurtado=code).first()
    return redirect(url.replace("<encurta_url ", "").replace(">",""), code=302)
    # return redirect(url, code=302)
    
@app.route('/retornar')
def retornar():
    return render_template('retornar.html')

@app.route('/original', methods=['POST'])
def original():
    if request.method == 'POST':
        url = request.form.get('codigo')
        code = encurta_link.query.filter_by(link_encurtado=url).first()
        print(code)
        return render_template('original.html', link_original=code)