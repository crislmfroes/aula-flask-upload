import os
import sys
import time

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
    return '.' in name and name.split('.')[-1].lower() in ['zip', 'png', 'pdf', 'txt']

@app.before_first_request
def init_fun():
    if not os.path.isdir(os.path.join('static')):
        os.mkdir(os.path.join('static'))
        if not os.path.isdir(os.path.join('static', 'uploads')):
            os.mkdir(os.path.join('static', 'uploads'))

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
            extension = arquivo.filename.split('.')[-1]
            arquivo_data = ArquivoBinario(data=arquivo.read(), extension=extension)
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

@app.route('/binmostrar/<int:cod>')
def binmostrar(cod):
    arquivo = arquivo_dao_bin.buscar(cod)
    filename = str(time.time()).replace('.', '_') + '.' + arquivo.extension
    with open(os.path.join('static', 'uploads', filename), 'wb') as f:
        f.write(arquivo.data)
        f.close()
    return redirect(url_for('static', filename="{}/{}".format(
        app.config['UPLOAD_FOLDER'],
        filename
    )))

def main():
    app.env = 'development'
    app.run(port=5000, debug=True)

if __name__ == '__main__':
    main()