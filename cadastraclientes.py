class CadastraCliente:

    def __init__(self):
        self.dados = []

    def insere_dado(self, dado):
        self.dados.append(dado)

    def transforma_dict(self):
        formulario = ["Nome","Endereço","Telefone","Nota","Valor"]
        fromdados = []

        for dado in self.dados:
            fromdados = [dado.nome, dado.endereco, dado.telefone, dado.nota, dado.valor]
        dictdados = dict(zip(formulario, fromdados))
        print(dictdados)


class Dado:
    def __init__(self, nome, endereco, telefone, nota, valor):
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
