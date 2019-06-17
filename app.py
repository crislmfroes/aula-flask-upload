import os
import sys

from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from werkzeug.utils import secure_filename

from arquivo import Arquivo, ArquivoBinario
from arquivo_dao import ArquivoDao, ArquivoBinarioDao

arquivo_dao = ArquivoDao()
arquivo_dao_bin = ArquivoBinarioDao()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

def permitido(name):
    return '.' in name and name.split('.')[-1].lower() in ['zip', 'png']

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        arquivo = request.files['file']
        if arquivo and permitido(arquivo.filename):
            nome_arquivo = secure_filename(arquivo.filename)
            arquivo.save(os.path.join('static', app.config['UPLOAD_FOLDER'], nome_arquivo))
            arquivo_data = Arquivo(caminho=os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo))
            arquivo_dao.inserir(arquivo_data)
            return redirect(url_for('listar'))
    return render_template('formulario.html', endpoint=request.endpoint)

@app.route('/binupload', methods=['GET', 'POST'])
def binupload():
    if request.method == 'POST':
        arquivo = request.files['file']
        if arquivo and permitido(arquivo.filename):
            arquivo_data = ArquivoBinario(data=arquivo.read())
            arquivo_dao_bin.inserir(arquivo_data)
            return redirect(url_for('binlistar'))
    return render_template('formulario.html', endpoint=request.endpoint)

@app.route('/listar')
def listar():
    arquivos = arquivo_dao.listar()
    return render_template('listar.html', arquivos=arquivos)

@app.route('/binlistar')
def binlistar():
    arquivos = arquivo_dao_bin.listar()
    return render_template('listarbytes.html', arquivos=arquivos, sys=sys)

def main():
    app.env = 'development'
    app.run(port=5000, debug=True)

if __name__ == '__main__':
    main()