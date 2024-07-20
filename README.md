# Cifra de Transposição

Você deve utilizar esse programa por linha de comando exemplo Exemplo:`>python cifra_transposicao.py {nome_arquivo} {chave} {modo}`

## Cifrar

### Entradas 
- Arquivo: Arquivo .txt com o nome 'nome_arquivo', este arquivo deve estar na mesma pasta que o programa de cifragem/decifragem, ao executar o arquivo passe o nome 'nome_arquivo.txt';
- Chave: A chave aceita apenas caracteres, sem caracteres repetidos, no minimo 3 caractres e no maximo 5, não podem estar em sequencia alfabetica(exemplo: 'ab', 'gmn', 'tref' e etc...) lembre de guardar a chave usada para poder decifrar o arquivo depois, se tentar utilizar outra chave para decifrar vai dar errado;
- Modo: Para cifrar escolha o modo 'cifrar'.

Ao final da cifragem sera gerado o arquivo 'nome_arquivo_cripto.txt'.

## Decifrar

### Entradas
- Arquivo: Arquivo 'nome_arquivo_cripto.txt' que foi gerado ao finalizar a cifragem do arquivo original;
- Chave: Deve ser utilizada a mesma chave que foi utilizado para cifrar o arquivo original;
- Modo: Para cifrar escolha o modo 'decifrar'.

Ao decifrar o arquivo sera gerado o arquivo 'nome_arquivo_decripto.txt' que terá o mesmo texto do arquivo original.

## Exemplo de utilização

### Exemplo Cifrar
`C:\Users\Wolff\Desktop\Pasta\Cifra>python cifra.py nome_arquivo.txt cafe cifrar`

Perceba que **C:\Users\Wolff\Desktop\Pasta\Cifra** é o caminho onde o programa de cifragem/decifragem e o arquivo a ser cifrado estavam no meu computador.

### Exemplo Decifrar
`C:\Users\Wolff\Desktop\Pasta\Cifra>python cifra.py nome_arquivo_cripto.txt cafe decifrar`

Perceba que **C:\Users\Wolff\Desktop\Pasta\Cifra** é o caminho onde o programa de cifragem/decifragem e o arquivo a ser decifrado estavam no meu computador.
