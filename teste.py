
from cadastraclientes import CadastraCliente, Dado
import json

teste = CadastraCliente()
dcompra = Dado(numero='1', nome='Junior', endereco='Rua', telefone='219854785', nota='100', valor='500')
teste.insere_dado(dcompra)
teste.transforma_dict()
#teste.salva_na_db()