import os 
import json
import adicionarprato_teste as prato
import ler_feedback_proprietario as feedback
import crud_alterarcategorias_proprietario as categoria
import ler_pedidos as pedidos  
import main as top 

arquivo = os.path.join(os.path.dirname(__file__), 'data\\cardapio.json')
CATEGORIAS_JSON = 'data\\categorias.json'


def menu_proprietario():
        print('-'*20)
        print("1- AJUSTAR PRATOS")
        print("2- AJUSTAR CATEGORIAS")
        print("3- LER PEDIDOS")
        print("4- LER FEEDBACKS")
        print("5- VOLTAR")
        print('-'*20)

def main():
    while True: 
        os.system('cls')
        menu_proprietario()
        opcao = input("Escolha uma opção: ")
    
        if opcao == '1':
            prato.main()

        elif opcao == '2':
            categoria.main()

        elif opcao == '3':    
            pedidos.main()

        elif opcao == '4': 
            feedback.main()
                    
        elif  opcao == '5':
            os.system('cls')
            top.main()

        else:
            print("Digite uma opção válida.")
            main()

if __name__ == '__main__':
    main()