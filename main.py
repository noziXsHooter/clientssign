
from cadastraclientes import CadastraCliente, Dado
from encontracliente import EncontraCliente, Object

opcao = input('Escolha uma opção: [1] para cadastro ou [2] para localizar cliente: ')

if opcao == '1':

    nome = input('Digite o nome do cliente: ')
    endereco = input('Digite o endereço do cliente: ')

    telefone = input('Digite o telefone do cliente: ')

    nota = input('Digite o numero da nota: ')

    valor = input('Digite o valor da compra: ')

    print()
    print('Por favor, confira os dados abaixo: ')

    print('Nome: ', nome)
    print('Endereço: ', endereco)
    print('Telefone: ', telefone)
    print('Nota: ', nota)
    print('Valor: ', valor)
    print()

    cliente = CadastraCliente()
    dcompra = Dado(nome, endereco, telefone, nota, valor)
    cliente.insere_dado(dcompra)

    cliente.transforma_dict()

    cliente.salva_na_db()

    print('Compra cadastrada com sucesso!')

elif opcao == '2':
    varbusca = input('Digite o nome do cliente: ')

    busca = EncontraCliente()
    dbusca = Object(varbusca)
    busca.insere_objeto(dbusca)

else:
    print('Por favor, digite uma opção válida.')

#client1 = cadastraclientes.CadastraCliente(nome, endereco, telefone, numero_da_nota, valor)
'''def busca(self):
        with open('jsondb.json', 'r') as jsondbread:
            datajsondb = json.load(jsondbread)

            if self.objetobusca not in datajsondb:
                print ('Objeto não encontrado!')'''
