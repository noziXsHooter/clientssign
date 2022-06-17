import sqlite3


class CadastroClientesDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, endereco, telefone, saldo=0, pontos=0):
        consulta = 'INSERT OR IGNORE INTO clientes (nome, endereco, telefone, saldo, pontos) VALUES (?, ?, ?, ?, ?)'
        self.cursor.execute(consulta, (nome, endereco, telefone, saldo, pontos))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM clientes')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, buscavalor):
        consulta = 'SELECT * FROM clientes WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{buscavalor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

class EditaClientes:
    def editar(self, nome, endereco, telefone, saldo, pontos, id):
        consulta = 'UPDATE OR IGNORE clientes SET nome=?, endereco =?,telefone=?, saldo=?, pontos=? WHERE id=?'
        self.cursor.execute(consulta, (nome, endereco, telefone, saldo, pontos, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM clientes WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()


if __name__ == '__main__':
    cadastro = CadastroClientesDB('clientes.db')
    edita = EditaClientes('clientes.db')

