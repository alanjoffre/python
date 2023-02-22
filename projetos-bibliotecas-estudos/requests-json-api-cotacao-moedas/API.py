import requests
import json

# esse link pode mudar se os donos da API mudarem
cotacoes = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes_dic = cotacoes.json()
cotacao_dolar = cotacoes_dic['USDBRL']['bid']
print(cotacao_dolar)