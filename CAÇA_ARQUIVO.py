
import os

pasta = 'C:/'
nome = input('pesquisar arquivo: ')
cont = 0

print('Carregando...')

arquivos_encontrados = []
local_aquivos_encontrado = []
tamanho_dos_arquivos = []

for raiz, diretorios, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        if nome in arquivo:
            local_arquivo = os.path.join(raiz, arquivo)
            arquivos_encontrados.append(arquivo)
            local_aquivos_encontrado.append(local_arquivo)

            tamanho = os.path.getsize(local_arquivo)
            tamanho = tamanho/1000000
            tamanho_dos_arquivos.append(tamanho)

            cont += 1

print(f'{cont} arquivos encontrados no seu sistema!')
print()

for i in range(len(arquivos_encontrados)):
    print(f'ARQUIVO: {arquivos_encontrados[i]}')

nome_preciso = input('\nPesquisa com precisão: ')
print()

for i in range(len(arquivos_encontrados)):
    if nome_preciso in arquivos_encontrados[i]:
        print(f'ARQUIVO: {arquivos_encontrados[i]}')
        print(f'TAMANHO: {tamanho_dos_arquivos[i]:.2f} MB')
        print(f'LOCAL: {local_aquivos_encontrado[i]}')
        print('\n', '-='*10, '\n')
        break
