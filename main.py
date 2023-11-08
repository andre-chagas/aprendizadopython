caminho_arquivo = 'aula152.txt'

with open(caminho_arquivo, 'w', enconding='utf-8') as arquivo:
    
    arquivo.write('Atenção\r\n')
    arquivo.write('linha 1\r\n')
    arquivo.write('linha 2\r\n')
    arquivo.writelines(
         ('linha 3\n', 'Linha 4\n')
    )