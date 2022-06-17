from comprasdb import *
from cadastraclientes import *

opcao = input('Escolha uma opção: \n'
              '[1] para cadastrar compra, \n'
              '[2] para localizar cliente ou compra, \n'
              '[3] para cadastrar cliente manualmente: \n'
              '[4] para editar cliente:  ')

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

    compras = ComprasDB('compras.db')
    compras.inserir(nome, endereco, telefone, nota, float(valor))

    print('Compra cadastrada com sucesso!')

    compras.editar('Marcos Vinicius')

    print('Saldo reajustado!')


elif opcao == '2':
    varbusca = input('Digite o nome do cliente ou qualquer informação de compra: ')

    compras = ComprasDB('compras.db')
    compras.buscar(varbusca)

elif opcao == '3':

    nomec = input('Digite o nome do cliente: ')
    enderecoc = input('Digite o endereço do cliente: ')
    telefonec = input('Digite o telefone do cliente: ')
    print()
    print('Por favor, confira os dados abaixo: ')

    print('Nome: ', nomec)
    print('Endereço: ', enderecoc)
    print('Telefone: ', telefonec)
    print()
    clientes = CadastroClientesDB('clientes.db')
    compras.inserir(nomec, enderecoc, telefonec)

    print('Cliente cadastrado com sucesso!')

elif opcao == '4':

    opcaoedit = input('Escolha uma opção: \n'
                      '[1] para editar cliente, \n'
                      '[2] para excluir cliente: ')

    if opcaoedit == '1':
        '''informaid = int(input('Digite o id do cliente: '))
        nomeedit = input('Digite o nome do cliente: ')
        enderecoedit = input('Digite o endereço do cliente: ')
        telefoneedit = input('Digite o telefone do cliente: ')
        saldo = input('Digite o saldo: ')
        pontos = input('Digite os pontos: ')
        print()
        print('Os dados editados foram: ')
'''
        #print('Nome: ', nomeedit)
        #print('Endereço: ', enderecoedit)
        #print('Telefone: ', telefoneedit)
        #print('Saldo: ', saldo)
        #print('Pontos: ', pontos)
        #print()
        #editacliente = EditaClientes('clientes.db')
        editacliente = CadastroClientesDB('clientes.db')
        editacliente.listar()
        #editacliente.editar(nomeedit, enderecoedit, telefoneedit, saldo, pontos, informaid)
        #cadastro.listar()

    elif opcaoedit == '2':
        idcliente = int(input('Digite o id do cliente a ser excluido: '))
        editacliente = EditaClientes('clientes.db')
        editacliente.excluir(idcliente)
        print('Cliente exlcuido com sucesso!.')
    else:
        print('Opcao Invalida!.')
else:
    print('Por favor, digite uma opção válida.')
