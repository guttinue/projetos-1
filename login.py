import os
import main as top

def exibir_titulo():
    print('''
    ███╗░░░███╗███████╗███╗░░██╗░█████╗░░█████╗░████████╗██╗░░██╗
    ████╗░████║██╔════╝████╗░██║██╔══██╗██╔══██╗╚══██╔══╝██║░░██║
    ██╔████╔██║█████╗░░██╔██╗██║██║░░██║██║░░██║░░░██║░░░███████║
    ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░██║██║░░██║░░░██║░░░██╔══██║
    ██║░╚═╝░██║███████╗██║░╚███║╚█████╔╝╚█████╔╝░░░██║░░░██║░░██║
    ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝''')

def mensagem_inicio():
    print('-'*20)
    print('1- CADASTRAR USUÁRIO')
    print('2- LOGIN')
    print('3- SAIR')
    print('-'*20)

def main():
    os.system('cls')
    exibir_titulo()
    mensagem_inicio()
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
            os.system('cls')
            top.main()
            break
        elif opcao == 3:
            print('Programa finalizado.')
            break

        else:
            print('Escolha uma opção válida')
            voltar_inicio()
            
def voltar_inicio():
    input('Digite qualquer tecla para voltar o menu')
    main()
        
usuarios = []  

def cadastrar_usuario(email, senha):
    usuarios.append({'email': email, 'senha': senha})  
    print("Usuário cadastrado com sucesso!") 
    
def fazer_login(email, senha):
    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            print("Login bem-sucedido!")
            
        else: 
            print("Nome de usuário ou senha incorretos.")
            voltar_inicio()

if __name__ == '__main__':
    main()