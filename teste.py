
from cadastraclientes import CadastraCliente, Dado
from encontracliente import*
import json

#teste = CadastraCliente()
#dcompra = Dado(nome='Marcelo', endereco='Rua', telefone='2185763200', nota='150', valor='5000')
#teste.insere_dado(dcompra)
#teste.transforma_dict()
#teste.salva_na_db()

busca = EncontraCliente()
dbusca = Object('Junior')
busca.insere_objeto(dbusca)
busca.busca_objeto()