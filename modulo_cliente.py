import os 
import json
import menu as menu
import carrinho as carrinho
import main as top

arquivo = os.path.join(os.path.dirname(__file__), 'data\\cardapio.json')

def menu_cliente():
        print('-'*20)
        print("1- VER CARDÁPIO")
        print("2- VER CARRNHO")
        print("3- VOLTAR")
        print('-'*20)

def main():
    while True: 
        os.system('cls')
        menu_cliente()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            os.system('cls')
            menu.main()
        elif opcao == '2':
            os.system('cls')
            carrinho.main()
        elif opcao == '3':
            os.system('cls')
            top.main()
        else:
            print("Opção inválida")
            main()

if __name__ == '__main__':
    main()