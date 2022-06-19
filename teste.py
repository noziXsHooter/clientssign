
#from cadastraclientes import CadastraCliente, Dado
from encontracliente import*
from datetime import datetime
import json


#dataagora = datetime.now()

#print(dataagora)
#print(dataagora.strftime("%d/%m/%Y %H:%M:%S"))

class TimeDB:
    def envia_tempo(self):
        self.dataagora = datetime.now()
        print(self.dataagora.strftime("%d/%m/%Y %H:%M:%S"))


if __name__ == '__main__':
    exectime = TimeDB()
    exectime.envia_tempo()


#teste = CadastraCliente()
#dcompra = Dado(nome='Marcelo', endereco='Rua', telefone='2185763200', nota='150', valor='5000')
#teste.insere_dado(dcompra)
#teste.transforma_dict()
#teste.salva_na_db()

#busca = EncontraCliente()
#dbusca = Object('Junior')
#busca.insere_objeto(dbusca)
#busca.busca_objeto()