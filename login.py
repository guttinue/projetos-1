import os

#Função para armazenar a logo
def exibir_titulo():
    print('''
    ███╗░░░███╗███████╗███╗░░██╗░█████╗░░█████╗░████████╗██╗░░██╗
    ████╗░████║██╔════╝████╗░██║██╔══██╗██╔══██╗╚══██╔══╝██║░░██║
    ██╔████╔██║█████╗░░██╔██╗██║██║░░██║██║░░██║░░░██║░░░███████║
    ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░██║██║░░██║░░░██║░░░██╔══██║
    ██║░╚═╝░██║███████╗██║░╚███║╚█████╔╝╚█████╔╝░░░██║░░░██║░░██║
    ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝''')

#Função para armazenar a mensagem de opções
def mensagem_inicio():
    print('-'*20)
    print('| Seja bem-vindo!   |')
    print('| 1 - Cadastrar     |')
    print('| 2 - Login         |')
    print('| 3 - Sair          |')
    print('-'*20)

#Função para escolher uma opção do menu
def escolha():
    opcao = int(input("Escolha uma opçaõ: "))
    
    while opcao != 200:
        if opcao == 1:
            email = input('Digite seu email:')
            senha = input('Crie sua senha: ')
            cadastrar_usuario(email, senha)
            voltar_inicio()

        elif opcao == 2:
            email = input('Digite o email cadastrado: ')
            senha = input('Digite sua senha: ')
            fazer_login(email, senha)
            voltar_inicio()


        elif opcao == 3:
            print('Programa finalizado.')
            break

        else:
            print('Escolha uma opção válida')
            voltar_inicio()
            

#Função para voltar o menu inicial
def voltar_inicio():
    input('Digite qualquer tecla para voltar o menu')
    main()
        
usuarios = []  #Lista vazia para armazenar novos valores


#Função para cadastro |   2 parâmetros
def cadastrar_usuario    (email, senha):
    usuarios.append({'email': email, 'senha': senha})  #usuarios.append adiciona um valor na lista, e vai armazenar um dicionario com valores na lista(nome e senha)
    print("Usuário cadastrado com sucesso!")
    #>>função de prosseguir<< 
    
def fazer_login(email, senha):
    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            print("Login bem-sucedido!")
            
        else: 
            print("Nome de usuário ou senha incorretos.")


def main():
    os.system('cls')
    exibir_titulo()
    mensagem_inicio()
    escolha()

if __name__ == '__main__':
    main()