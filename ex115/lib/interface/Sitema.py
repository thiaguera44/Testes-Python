from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Listas o conteudo do arquivo
        lerArquivo('cursoemvideo.txt')

    elif resposta == 2:
        #Opção de cadastrar nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        print('Saindo do sistema... Até logo')
        break
    else:
        print('\033[0;31mERRO! DIGITE UMA OPÇÃO VÁLIDA\033[m')
    sleep(2)