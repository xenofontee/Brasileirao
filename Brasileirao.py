import requests
import json
import os
import requests.exceptions

key = os.getenv("API_TOKEN")

API_URL = "https://api.api-futebol.com.br/v1/campeonatos/10/"


def authenticate():  # Autentica o usuário na API com o token de acesso.
    headers = {'Authorization': f'Bearer {key}'}
    return headers


def pretty_json(json_data):  # Imprime um objeto JSON formatado de forma legível.
    print(json.dumps(json_data, indent=4))


def get_data(endpoint):  # Faz uma requisição GET à API e retorna os dados em formato JSON.
    url = API_URL + endpoint
    headers = authenticate()
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # lança exceção se a resposta não for bem-sucedida
    return response.json()


def brasileirao_tabela():  # define a função da tabela do campeonato brasileiro
    endpoint = 'tabela'
    try:
        data = get_data(endpoint)
        pretty_json(data)
    except requests.exceptions.HTTPError as e:
        print(f'A solicitação GET falhou com o código de resposta {e.response.status_code}')


def brasileirao_artilharia():  # define a função da artilharia do campeonato brasileiro
    endpoint = 'artilharia'
    try:
        data = get_data(endpoint)
        pretty_json(data)
    except requests.exceptions.HTTPError as e:
        print(f'A solicitação GET falhou com o código de resposta {e.response.status_code}')


if __name__ == '__main__':
    print('Bem-vindo ao Script do BRASILEIRÃO')
    user_input = input('Digite 1 para TABELA e 2 para ARTILHARIA: ')

    if user_input == '1':
        brasileirao_tabela()
    elif user_input == '2':
        brasileirao_artilharia()
    else:
        print('Valor inválido. Digite 1 ou 2')
