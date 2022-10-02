import sqlite3

con = sqlite3.connect('agenda.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS contatos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, ddd REAL, '
            'telefone REAL)')


class Agenda:
    def __init__(self):
        pass

    def cadastrar_contato(self, nome, ddd, telefone):
        cur.execute('INSERT INTO contatos (nome, ddd, telefone) VALUES (?, ?, ?)', (nome, ddd, telefone))
        con.commit()

    def mostrar_agenda(self):
        cur.execute('SELECT * FROM contatos')
        for linha in cur.fetchall():
            print('Cód: %d      Nome: %s        DDD: %d     Telefone: %d' % linha)

    def excluir_contato(self, nome):
        cur.execute(f'DELETE FROM contatos WHERE nome = (?)', [nome])
        con.commit()

    def atualizar_nome(self, nome, novo_nome):
        cur.execute('UPDATE contatos SET nome = (?) WHERE nome = (?)', ((novo_nome), (nome)))

    def atualizar_numero(self, nome, novo_numero):
        cur.execute('UPDATE contatos SET telefone = (?) WHERE nome = (?)', ((novo_numero), (nome)))

