import psycopg2

from arquivo import Arquivo, ArquivoBinario

class Dao:
    def __init__(self, host="localhost", port="5432", user="postgres", password="postgres", database="arquivo_db"):
        self._connection_string = "host={} port={} user={} password={} dbname={}".format(
            host,
            port,
            user,
            password,
            database
        )

class ArquivoDao(Dao):
    def __init__(self, host="localhost", port="5432", user="postgres", password="postgres", database="arquivo_db"):
        super(ArquivoDao, self).__init__(host, port, user, password, database)
    
    def inserir(self, arquivo):
        try:
            with psycopg2.connect(self._connection_string) as conn:
                cursor = conn.cursor()
                sql = "INSERT INTO Arquivo(caminho) VALUES(%s) RETURNING cod"
                cursor.execute(sql, (arquivo.caminho,))
                arquivo.cod = cursor.fetchone()[0]
        except BaseException as e:
            print("Erro ao inserir arquivo no banco ...")
            raise e

    def listar(self):
        try:
            with psycopg2.connect(self._connection_string) as conn:
                cursor = conn.cursor()
                sql = "SELECT * FROM Arquivo"
                cursor.execute(sql)
                rows = cursor.fetchall()
                arquivos = list()
                for row in rows:
                    arquivo = Arquivo(caminho=row[1], cod=row[0])
                    arquivos.append(arquivo)
            return arquivos
        except BaseException as e:
            print("Erro ao consultar banco ...")
            raise e

class ArquivoBinarioDao(Dao):
    def __init__(self, host="localhost", port="5432", user="postgres", password="postgres", database="arquivo_db"):
        super(ArquivoBinarioDao, self).__init__(host, port, user, password, database)
    
    def inserir(self, arquivoBinario):
        try:
            with psycopg2.connect(self._connection_string) as conn:
                cursor = conn.cursor()
                sql = "INSERT INTO ArquivoBinario(data) VALUES(%s) RETURNING cod"
                cursor.execute(sql, (arquivoBinario.data,))
                arquivoBinario.cod = cursor.fetchone()[0]
        except BaseException as e:
            print("Erro ao inserir arquivo no banco ...")
            raise e
        
    def listar(self):
        try:
            with psycopg2.connect(self._connection_string) as conn:
                cursor = conn.cursor()
                sql = "SELECT * FROM ArquivoBinario"
                cursor.execute(sql)
                rows = cursor.fetchall()
                arquivos = list()
                for row in rows:
                    arquivo = ArquivoBinario(data=bytes(row[1]), cod=row[0])
                    arquivos.append(arquivo)
            return arquivos
        except BaseException as e:
            print("Erro ao consultar banco ...")
            raise e
