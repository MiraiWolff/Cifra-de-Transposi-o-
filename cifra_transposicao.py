import math

def cifrar_mensagem(mensagem, chave):
    array_mensagem = list(mensagem)
    colunas = len(chave)
    num_linhas = math.ceil(len(array_mensagem) / colunas)
    matriz = [['' for _ in range(colunas)] for _ in range(num_linhas)]
    
    index = 0
    for l in range(num_linhas):
        for c in range(colunas):
            if index < len(array_mensagem):
                matriz[l][c] = array_mensagem[index]
                index += 1
    
    chave_ordenada = sorted(list(chave))#
    matriz_cifrada = [['' for _ in range(colunas)] for _ in range(num_linhas)]
    
    for nova_coluna, k in enumerate(chave_ordenada):
        coluna_antiga = chave.index(k)
        for l in range(num_linhas):
            matriz_cifrada[l][nova_coluna] = matriz[l][coluna_antiga]
    
    texto_cifrado = ''.join([''.join(linha) for linha in matriz_cifrada])
    
    return texto_cifrado

def decifrar_mensagem(mensagem, chave):
    colunas = len(chave)
    num_linhas = math.ceil(len(mensagem) / colunas)
    matriz = [['' for _ in range(colunas)] for _ in range(num_linhas)]
    chave_ordenada = sorted(list(chave))
    
    for nova_coluna, k in enumerate(chave_ordenada):
        coluna_antiga = chave.index(k)
        for l in range(num_linhas):
            if l * colunas + nova_coluna < len(mensagem):
                matriz[l][coluna_antiga] = mensagem[l * colunas + nova_coluna]
    
    texto_decifrado = ''.join([''.join(linha) for linha in matriz])
    return texto_decifrado

def processar_arquivo(nome_arquivo, chave, modo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        mensagem = arquivo.read()
    if modo == 'cifrar':
        texto_resultante = cifrar_mensagem(mensagem, chave)
        nome_arquivo_saida = nome_arquivo.replace('.txt', '_cripto.txt')
    elif modo == 'decifrar':
        texto_resultante = decifrar_mensagem(mensagem, chave)
        nome_arquivo_saida = nome_arquivo.replace('_cripto.txt', '_decripto.txt')
    
    with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
        arquivo_saida.write(texto_resultante)
    
    print(f"Arquivo processado: {nome_arquivo_saida}")

nome_arquivo = input('Digite o nome do arquivo nome_arquivo.txt ou nome_arquivo_cripto.txt: ')

if nome_arquivo == 'nome_arquivo.txt' or nome_arquivo == 'nome_arquivo_cripto.txt':
    chave = input('Digite a chave de cifragem: ')
    modo = input('Digite cifrar para criptografar ou decifrar para descriptografar: ').lower()
    if modo == 'cifrar' or modo == 'decifrar':
            processar_arquivo(nome_arquivo, chave, modo)
    else:
            print('Erro modo escolido é inválido')
else:
    print('Erro nome do arquivo inválido')
