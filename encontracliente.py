import json


class EncontraCliente():
    def __init__(self):
        self.objetobusca = []

    def insere_objeto(self, objeto):
        self.objetobusca.append(objeto)
        for i in self.objetobusca:
            self.stringobjeto = i.objeto
            print(self.stringobjeto)

    def busca_objeto(self):
        with open('jsondb.json', 'r') as jsondbread:
            datajsondb = json.load(jsondbread)
            print(type(datajsondb))
            print(datajsondb.get(('1'), ('Nome')))

        '''for v in datajsondb.values():
            v = v['Nome']
            if v == self.stringobjeto:
                print('O objeto da busca {} foi encontrado!'.format(v))'''


class Object:
    def __init__(self, objeto):
        self.objeto = objeto
