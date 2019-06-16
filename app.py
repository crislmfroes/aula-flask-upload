import os

from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from werkzeug.utils import secure_filename

from arquivo import Arquivo
from arquivo_dao import ArquivoDao

arquivo_dao = ArquivoDao()

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

@app.route('/listar')
def listar():
    arquivos = arquivo_dao.listar()
    return render_template('listar.html', arquivos=arquivos)

def main():
    app.env = 'development'
    app.run(port=5000, debug=True)

if __name__ == '__main__':
    main()