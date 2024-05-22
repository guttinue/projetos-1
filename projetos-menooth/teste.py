import json
import os
from time import sleep


class cor:
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'
    RESET = '\033[0m'


arquivo = os.path.join(os.path.dirname(__file__), 'pratos1.json')



def adicionar_usuario(nome, idade):
    with open(arquivo, 'r') as f:
        usuarios = json.load(f)

    usuarios.append({'nome': nome, 'idade': idade})

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4)
    print("😎 USUÁRIO ADICIONADO COM SUCESSO!")

def listar_usuarios():
    with open(arquivo, 'r') as f:
        usuarios = json.load(f)

    if usuarios:
        print("=" *50)
        print("LISTA DE USUÁRIOS:")
        print("-" *50)
        for usuario in usuarios:
            print("*" *50)
            print(f"NOME: {usuario['nome']}, IDADE: {usuario['idade']}")
            print("*" *50)
            print("=" *50)
    else:
        print("😒 NENHUM USUÁRIO CADASTRADO.")

def atualizar_usuario(nome_antigo, novo_nome, nova_idade):
    with open(arquivo, 'r') as f:
        usuarios = json.load(f)

    for usuario in usuarios:
        if usuario['nome'] == nome_antigo:
            usuario['nome'] = novo_nome
            usuario['idade'] = nova_idade
            break

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4)
    print("😙 USUÁRIO ATUALIZADO COM SUCESSO!")

def excluir_usuario(nome):
    with open(arquivo, 'r') as f:
        usuarios = json.load(f)

    for usuario in usuarios:  
        if usuario['nome'] == nome:
            usuarios.remove(usuario)

    with open(arquivo, 'w') as f:
        json.dump(usuarios, f, indent=4)
        print("😡 USUÁRIO EXCLUÍDO COM SUCESSO!")

def buscar_usuario (nome):
    with open(arquivo, 'r') as f:
        usuarios = json.load(f)
    
    encontrado = False

    for usuario in usuarios:
        if usuario['nome'] == nome:
            print(f"NOME: {usuario['nome']}, IDADE: {usuario['idade']}")
            encontrado = True
    if not encontrado:
            print("😒 NENHUM USUÁRIO CADASTRADO.")
    

def linha_horizontal(cor):
    return cor + "=" * 50 + cor['RESET']

def menu_inicial ():
    print (cor.CIANO + "=" *55 + cor.RESET)
    print (cor.VERMELHO + " ---->>> BEM VINDO AO SISTEMA MERCADO CLEAN <<<---- ")
    print ("          1 - MÓDULO USUÁRIO ")
    print ("          2 - MÓDULO ESTOQUE ")
    print ("          3 - SAIR ")
    print (cor.CIANO + "=" *55 + cor.RESET)
    
def exibir_menu():
    print("\nMENU:")
    print("1. ADICIONAR USUÁRIO")
    print("2. LISTAR USUÁRIOS")
    print("3. ATUALIZAR USUÁRIO")
    print("4. EXCLUIR USUÁRIO")
    print("5. LISTAR UM USUÁRIO")
    print("6. VOLTAR AO MENU ANTERIOR")



def main():
    
    while True:
        menu_inicial()
        opcao_inicial = int(input("INFORME UMA OPÇÃO"))

        match (opcao_inicial):
            case 2:
                print("MÓDULO EM DESENVOLVIMENTO")

            case 1:
                while True: 
                    exibir_menu()
                    opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")

                    if opcao == "1":
                        nome = input(" DIGITE O NOME:\n>>>")
                        idade = input(" DIGITE A IDADE:\n>>>")
                        adicionar_usuario(nome, idade)
                    elif opcao == "2":
                        listar_usuarios()
                    elif opcao == "3":
                        nome_antigo = input("DIGITE O NOME A SER ATUALIZADO:\n>>>")
                        novo_nome = input("DIGITE O NOVO NOME:\n>>>")
                        nova_idade = input("DIGITE A NOVA IDADE:\n>>>")
                        atualizar_usuario(nome_antigo, novo_nome, nova_idade)
                    elif opcao == "4":
                        nome = input("DIGITE O NOME DO USUÁRIO A SER EXCLUÍDO:\n>>>")
                        excluir_usuario(nome)
                    elif opcao == "5":
                        nome = input("DIGITE O NOME DO USUÁRIO:\n>>>")
                        buscar_usuario(nome)
                    elif opcao == "6":
                        print("VOLTAR AO MENU ANTERIOR...")
                        sleep(3)
                        break
                    else:
                        print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            case 3:
                print("🚀 SAINDO...")
                sleep(3)
                break
            case __:
                print("😡 OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()