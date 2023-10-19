import requests
import json


def pretty_json(json_data):  # define o Json_pretty
    print(json.dumps(json_data, indent=4))


def BRASILEIRAO_TABELA():  # define a função da tabela do campeonato brasileiro
    URL = 'https://api.api-futebol.com.br/v1/campeonatos/10/tabela'
    token = 'SuaChaveDeAPIAqui'
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        pretty_json(data)
        # print(data)
    else:
        print(f"A solicitação GET falhou com o código de resposta {response.status_code}")


def BRASILEIRAO_ARTILHARIA():  # define a função da artilharia do campeonato brasileiro
    URL = 'https://api.api-futebol.com.br/v1/campeonatos/10/artilharia'
    token = 'SuaChaveDeAPIAqui'
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        pretty_json(data)
        # print(data)
    else:
        print(f"A solicitação GET falhou com o código de resposta {response.status_code}")


print("Bem-vindo ao Script do BRASILEIRÃO")
user_input = input("Digite 1 para TABELA e 2 para ARTILHARIA: ")

if user_input == '1':
    BRASILEIRAO_TABELA()
elif user_input == '2':
    BRASILEIRAO_ARTILHARIA()
else:
    print("Valor inválido. Digite 1 ou 2")
