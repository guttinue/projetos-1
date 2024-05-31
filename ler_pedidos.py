import os 
import json 
import modulo_cliente as menu

PEDIDOS_JSON = 'data\\pedidos.json'

def carregar_pratos():
    if not os.path.exists(PEDIDOS_JSON):
        return []
    with open(PEDIDOS_JSON, 'r') as f:
        return json.load(f)

def listar_pedidos():
    pratos = carregar_pratos()
    if pratos:
        print("Lista de Pratos:")
        for prato in pratos:
            print(f"ID: {prato['id']}")
            print(f"Nome: {prato['nome']}")
            print(f"Descrição: {prato['descricao']}")
            print(f"Preço: R${prato['preco']:.2f}")
            print(f"Ingredientes: {', '.join(prato['ingredientes'])}")
            print(f"Categoria: {prato['categoria']}")
            print("-" * 40)
    else:
        print("Nenhum prato encontrado.")

def exibir_menu():
    print('-'*20)
    print("1- LISTAR PEDIDOS")
    print("2- VOLTAR")
    print('-'*20)

def main():
    while True:
        exibir_menu()
        opcao = input("Digite a opção a sua escolha: ")
        if opcao == '1':
            listar_pedidos()
            input('Digite qualquer tecla para voltar ao menu')
            menu.main()

        elif opcao == '2':
            menu.main()
        else:
            print("Digite um numero valido.")
            main()    
                    
if __name__ == '__main__':
    main()


