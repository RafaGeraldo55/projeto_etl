from json import load
import requests
from tinydb import TinyDB
import time


def extrai_dados_bitcoin():
    url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'
    response = requests.get(url)
    return(response.json())
    
def transforma_dados_bitcoin(dados):
    cripto = dados['data']['base']
    valor_bitcoin = dados['data']['amount']
    moeda = dados['data']['currency']
    dados_transformados = {
        'cripto': cripto,
        'valor': valor_bitcoin,
        'moeda': moeda
    }
    return dados_transformados

def load(dados_transformados):
        db = TinyDB('db.json')
        db.insert(dados_transformados)
        print('Dados carregados com sucesso')


if __name__ == '__main__':
    while True: 
        try:
            dados = extrai_dados_bitcoin()
            dados_transformados = transforma_dados_bitcoin(dados)
            load(dados_transformados)
            time.sleep(5)
        except Exception as e:
            print(f'Erro: {e}')
            time.sleep(5)