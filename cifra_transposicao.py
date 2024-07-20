import math
import sys

#Cifra a mensagem 
def cifrar_mensagem(mensagem, chave):
    array_mensagem = list(mensagem)

    #Número de colunas é o comprimento da chave
    colunas = len(chave)
    #Calcular o número de linhas necessárias para cifragem
    num_linhas = math.ceil(len(array_mensagem) / colunas)
    
    #Inicializa a matriz com o numero de colunas e linhas 
    matriz = [['' for _ in range(colunas)] for _ in range(num_linhas)]
    
    #Preencher a matriz com os caracteres da mensagem
    index = 0
    for l in range(num_linhas):
        for c in range(colunas):
            if index < len(array_mensagem):
                matriz[l][c] = array_mensagem[index]
                index += 1
    
    #Ordenar as colunas com base na chave
    chave_ordenada = sorted(list(chave))#
    matriz_cifrada = [['' for _ in range(colunas)] for _ in range(num_linhas)]
    
    #Reorganizar as colunas na nova matriz cifrada
    for nova_coluna, k in enumerate(chave_ordenada):
        coluna_antiga = chave.index(k)
        for l in range(num_linhas):
            matriz_cifrada[l][nova_coluna] = matriz[l][coluna_antiga]
    
    #Formar o texto cifrado a partir da matriz cifrada
    texto_cifrado = ''.join([''.join(linha) for linha in matriz_cifrada])
    return texto_cifrado

#Decifra a mensagem 
def decifrar_mensagem(mensagem, chave):
    colunas = len(chave)
    
    #Calcular o número de linhas necessárias
    num_linhas = math.ceil(len(mensagem) / colunas)
    
    #Inicializar a matriz
    matriz = [['' for _ in range(colunas)] for _ in range(num_linhas)]
    
    #Ordenar a chave para obter a ordem original
    chave_ordenada = sorted(list(chave))
    
    #Reorganizar as colunas na matriz original
    for nova_coluna, k in enumerate(chave_ordenada):
        coluna_antiga = chave.index(k)
        for l in range(num_linhas):
            if l * colunas + nova_coluna < len(mensagem):
                matriz[l][coluna_antiga] = mensagem[l * colunas + nova_coluna]
    
    #Formar o texto decifrado a partir da matriz
    texto_decifrado = ''.join([''.join(linha) for linha in matriz])
    return texto_decifrado

#Valida a chave para que não tenha caracteres repetidos
def valida_caracter_repetido_chave(chave):
    letras = []
    for i in chave:
        if i not in letras:
            letras.append(i)
        else:
            return False
    return True

#Valida para que a chave não tenha sequencia alfabetica
def valida_sequencia_alfabetica(chave):
    for i in range(len(chave) - 1):
        if ord(chave[i]) + 1 == ord(chave[i + 1]):
            return False
    return True

#Processa o arquivo txt para ser cifrado ou decifrado
def processar_arquivo(nome_arquivo, chave, modo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        mensagem = arquivo.read()
    if modo == 'cifrar':
        texto_resultante = cifrar_mensagem(mensagem, chave)
        nome_arquivo_saida = nome_arquivo.replace('.txt', '_cripto.txt')
    elif modo == 'decifrar':
        if nome_arquivo == 'nome_arquivo_cripto.txt':
            texto_resultante = decifrar_mensagem(mensagem, chave)
            nome_arquivo_saida = nome_arquivo.replace('_cripto.txt', '_decripto.txt')
        else:
            texto_resultante = decifrar_mensagem(mensagem, chave)
            nome_arquivo_saida = nome_arquivo.replace('.txt', '_decripto.txt')
    
    with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
        arquivo_saida.write(texto_resultante)
    
    print('Arquivo processado: ' + nome_arquivo_saida)

#Faz com que o nome do arquivo, a chave e o modo tenham que ser passados como parametro na hora de chamar o arquivo 
nome_arquivo = sys.argv[1]
chave = sys.argv[2]
modo = sys.argv[3].lower()

#Faz a verificação nos parametros de entrada para ver se atendem os requisitos solicitados
if nome_arquivo == 'nome_arquivo.txt' or nome_arquivo == 'nome_arquivo_cripto.txt':
    if len(chave) <= 5 and len(chave) >= 3 and chave.isalpha() and valida_caracter_repetido_chave(chave) and valida_sequencia_alfabetica(chave):
        if modo == 'cifrar' or modo == 'decifrar':
            processar_arquivo(nome_arquivo, chave, modo)
        else:
            print('Erro modo escolido é inválido')
    else:
        print('Erro a chave deve conter apenas letras, ter no minimo 3 letras e no máximo 5, não repetir caracteres e não ter sequencia alfabetica.')
else:
    print('Erro nome do arquivo inválido')
