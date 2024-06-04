import os 
import json
import adicionar_prato as prato
import mudulo_proprietario as menu

FEEDBACKS_JSON = 'data\\feedback.json'

def carregar_feedbacks():
    if not os.path.exists(FEEDBACKS_JSON):
        return []
    with open(FEEDBACKS_JSON, 'r') as f:
        return json.load(f)

        # Função para listar todos os feedbacks

def listar_feedbacks():
    feedbacks = carregar_feedbacks()
    if feedbacks:
        print("Lista de Feedbacks:")
        for feedback in feedbacks:
            print(f"ID: {feedback['id']}")
            print(f"Nome: {feedback['nome']}")
            print(f"Mensagem: {feedback['mensagem']}")
            print("-" * 40)
                    
    else:
        print("Nenhum feedback encontrado.")

def exibir_menu():
    print('-'*20)
    print("1- LISTAR FEEDBACKS")
    print("2- VOLTAR")
    print('-'*20)

def main():
    while True:
        os.system('cls')
        exibir_menu()
        opcao = input("Digite a opção a sua escolha: ")
        if opcao == '1':
            listar_feedbacks()
            input('Digite qualquer tecla para voltar ao menu')
            menu.main()

        elif opcao == '2':
            menu.main()
        else:
            print("Digite um numero valido.")
            main()    
                    
if __name__ == '__main__':
    main()
