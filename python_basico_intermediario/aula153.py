import json

pessoa = {
    'nome': 'André Chagas 2',
    'sobrenome': 'Luis',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R1', 'numero': 55},
   ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
 }

with open('aula153.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo, 
        ensure_ascii=False,
        indent=2,
    )

with open('aula153.json', 'r') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])