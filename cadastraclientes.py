import json


class CadastraCliente:
    global dictmain

    def __init__(self):
        self.dados = []

    def insere_dado(self, dado):
        self.dados.append(dado)

    def transforma_dict(self):
        formulario = ['Nome', 'Endereco', 'Telefone', 'Nota', 'Valor']
        fromdados = []

        for dado in self.dados:
            fromdados = [dado.nome, dado.endereco, dado.telefone, dado.nota, dado.valor]
        dictdados = dict(zip(formulario, fromdados))
        self.dictmain = dictdados

    def salva_na_db(self):
        with open('jsondb.json', 'r') as jsondbread:
            datajsondb = json.load(jsondbread)
            datalist = list(datajsondb)
            for i in range(0, len(datalist)):
                datalist[i] = (int(datalist[i]))
            ultima_compra = str(datalist[-1] + 1)
            datajsondb[ultima_compra] = self.dictmain
        print(self.dictmain)
        print(datajsondb)
        print(ultima_compra)

        with open('jsondb.json', 'w') as jsondbwrite:
            json.dump(datajsondb, jsondbwrite, indent=4)

class Dado:
    def __init__(self, nome, endereco, telefone, nota, valor):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.nota = nota
        self.valor = valor
