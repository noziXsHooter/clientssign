
from cadastraclientes import CadastraCliente, Dado


numero = input('Digite o numero da compra: ')

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
dcompra = Dado(numero, nome, endereco, telefone, nota, valor)
cliente.insere_dado(dcompra)

cliente.transforma_dict()

cliente.salva_na_db()

print('Compra cadastrada com sucesso!')

#cliente1.lista_dados()






#client1 = cadastraclientes.CadastraCliente(nome, endereco, telefone, numero_da_nota, valor)
