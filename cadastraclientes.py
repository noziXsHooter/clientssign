import db as db
import json


class CadastraCliente:
    # global dictdados
    global dictmain

    def __init__(self):
        self.dados = []

    def insere_dado(self, dado):
        self.dados.append(dado)

    def transforma_dict(self):
        formulario = ['Nome', 'Endereco', 'Telefone', 'Nota', 'Valor']
        fromdados = []

        for dado in self.dados:
            fromdados = [dado.numero, dado.nome, dado.endereco, dado.telefone, dado.nota, dado.valor]
        self.dnum, *fromdadossemnumero = fromdados
        dictdados = dict(zip(formulario, fromdadossemnumero))
        self.dictmain = dictdados
        # print(dictdados)
        # print(dnum)
        # print(self.dictmain)
        # print(self.dictmain.keys())

    #        with open('db.py', 'w') as dictdb:
    #            dictdb.write(json.dumps(self.dictmain))
    #            print(dictdb.get("1"))

    def salva_na_db(self):
        with open('jsondb.json', 'r') as jsondbread:
            datajsondb = json.load(jsondbread)
            datajsondb[self.dnum] = self.dictmain
        # print(datajsondb)
        # print(self.dictmain)
        with open('jsondb.json', 'w') as jsondbwrite:
            json.dump(datajsondb, jsondbwrite, indent=4)
        # with open('jsondb.json', 'w') as arquivo:
        # json.dump(self.dictmain, arquivo, indent = 4)


#        with open('jsondb.json', 'w') as jsondb:
#           json.dump(self.dictmain, jsondb)
# print(datajsondb)
# with open('db.py', 'w') as dictdb:
# dictdbjson = json.dumps(self.dictmain)
# print(dictdbjson)

class Dado:
    def __init__(self, numero, nome, endereco, telefone, nota, valor):
        self.numero = numero
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.nota = nota
        self.valor = valor


'''    def lista_dados(self):
            for dado in self.dados:
                print('Os dados são: ')
                print(dado.nome, dado.endereco, dado.telefone, dado.nota, dado.valor)
'''
