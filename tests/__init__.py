import requests
print('Nova versao do projeto ETL')

def extrai_dados_bitcoin():
    url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'
    response = requests.get(url)
    dados = response.json()
    return dados

def transforma_dados_bitcoin(dados):
    cripto = dados['data']['base']
    valor_bitcoin = dados['data']['amount']
    moeda = dados['data']['currency']
    return {
        'cripto': cripto,
        'valor': valor_bitcoin,
        'moeda': moeda
    }

if __name__ == '__main__':
    dados = extrai_dados_bitcoin()
    dados_transformados = transforma_dados_bitcoin(dados)
    print(dados)
    print(dados_transformados)