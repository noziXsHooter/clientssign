
from cadastraclientes import CadastraCliente, Dado

cliente1 = CadastraCliente()

nome = input('Digite o nome do cliente: ')

endereco = input('Digite o endereço do cliente: ')

telefone = input('Digite o telefone do cliente: ')

nota = input('Digite o numero da nota: ')

valor = input('Digite o valor da compra: ')

print('Por favor, confira os dados abaixo: ')

print('Nome: ', nome)
print('Endereço: ', endereco)
print('Telefone: ', telefone)
print('Nota: ', nota)
print('Valor: ', valor)



dcompra = Dado(nome, endereco, telefone, nota, valor)
cliente1.insere_dado(dcompra)

cliente1.transforma_dict()

#cliente1.lista_dados()






#client1 = cadastraclientes.CadastraCliente(nome, endereco, telefone, numero_da_nota, valor)
