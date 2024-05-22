import json
import os
from time import sleep

arquivo = os.path.join(os.path.dirname(__file__), 'pratos.json')
ingredientesP = []



def adicionar_prato(nome, preco, calorias, ingredientes):
    with open(arquivo, 'r') as f:
        pratos = json.load(f)

    pratos.append({'nome': nome, 'preco': preco, 'calorias': calorias, 'ingredientes': ingredientes})

    with open(arquivo, 'w') as f:
        json.dump(pratos, f, indent=4)
    print("😎 USUÁRIO ADICIONADO COM SUCESSO!")

def listar_pratos():
    with open(arquivo, 'r') as f:
        pratos = json.load(f)

    if pratos:
        print("=" *50)
        print("LISTA DE USUÁRIOS:")
        print("-" *50)
        for prato in pratos:
            print("*" *50)
            print(f"NOME: {prato['nome']}, PRECO: {prato['preco']}, CALORIAS: {prato['calorias']}")
            print("*" *50)
            print("=" *50)
    else:
        print("😒 NENHUM PRATO CADASTRADO.")

def atualizar_prato(nome_antigo, novo_nome, novo_preco, novas_calorias, novos_ingredientes):
    with open(arquivo, 'r') as f:
        pratos = json.load(f)

    for prato in pratos:
        if prato["nome"] == nome_antigo:
            prato['nome'] = novo_nome
            prato['preco'] = novo_preco
            prato['calorias'] = novas_calorias
            prato['ingredientes'] = novos_ingredientes
            break

    with open(arquivo, 'w') as f:
        json.dump(pratos, f, indent=4)
    print("😙 USUÁRIO ATUALIZADO COM SUCESSO!")

def excluir_prato(nome):
    with open(arquivo, 'r') as f:
        pratos = json.load(f)

    for prato in pratos:  
        if prato['nome'] == nome:
            pratos.remove(prato)

    with open(arquivo, 'w') as f:
        json.dump(pratos, f, indent=4)
        print("😡 USUÁRIO EXCLUÍDO COM SUCESSO!")

def buscar_prato (nome):
    with open(arquivo, 'r') as f:
        pratos = json.load(f)
    
    encontrado = False

    for prato in pratos:
        if prato['nome'] == nome:
            print(f"NOME: {prato['nome']}, PRECO: {prato['preco']}, CALORIAS: {prato['calorias']}")
            encontrado = True
    if not encontrado:
            print("😒 NENHUM PRATO CADASTRADO.")
    

def linha_horizontal(cor):
    return cor + "=" * 50 + cor['RESET']
    
def exibir_menu():
    print("\nMENU:")
    print("1. ADICIONAR PRATO")
    print("2. LISTAR USUÁRIOS")
    print("3. ATUALIZAR USUÁRIO")
    print("4. EXCLUIR USUÁRIO")
    print("5. LISTAR UM USUÁRIO")
    print("6. VOLTAR AO MENU ANTERIOR")



def main():
    while True: 
            exibir_menu()
            opcao = input("ESCOLHA UMA OPÇÃO:\n>>>")

            if opcao == "1":
                
                while True:
                    nome = input(" DIGITE O NOME:\n>>>")
                    preco = input(" DIGITE O PREÇO:\n>>>")
                    calorias = input(" DIGITE AS CALORIAS:\n:>>>")
                    ingrediente = input("DIGITE O INGREDIENTE: (ou digitar 'n'n para encerrar \n>>>)")
                    if ingrediente.upper() == "N":
                        break
                    quantidade = int(input("DIGITE A QUANTIDADE:\n>>>"))
                    
                    quantidade = input(" DIGITE OS INGREDIENTES:\n:>>>")

                    ingredientes = {'ingrediente': ingrediente, 'quantidade': quantidade}
                    ingredientesP.append(ingredientes)

                    adicionar_prato(nome, preco, calorias, ingredientes)
                
            elif opcao == "2":
                listar_pratos()
            elif opcao == "3":
                nome_antigo = input("DIGITE O NOME A SER ATUALIZADO:\n>>>")
                novo_nome = input("DIGITE O NOVO NOME:\n>>>")
                novo_preco = input("DIGITE A NOVA preco:\n>>>")
                novas_calorias = input("DIGITE A NOVA calroais:\n>>>")
                atualizar_prato(nome_antigo, novo_nome, novo_preco, novas_calorias)
            elif opcao == "4":
                nome = input("DIGITE O NOME DO USUÁRIO A SER EXCLUÍDO:\n>>>")
                excluir_prato(nome)
            elif opcao == "5":
                nome = input("DIGITE O NOME DO USUÁRIO:\n>>>")
                buscar_prato(nome)
            elif opcao == "6":
                print("VOLTAR AO MENU ANTERIOR...")
                sleep(3)
                break  
            
if __name__ == "__main__":
    main()