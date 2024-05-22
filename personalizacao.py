import json
import os

# Define o caminho para o arquivo JSON
carrinho = os.path.join(os.path.dirname(__file__), 'carrinho.json')

# Função para carregar os dados do arquivo JSON
def load_data():
    if os.path.exists(carrinho):
        with open(carrinho, 'r') as f:
            return json.load(f)
    return {"Pratos Principais": {"id": 1, "nome": "", "descricao": "", "calorias": "", "ingredientes": []}}

# Função para salvar os dados no arquivo JSON
def save_data(data):
    with open(carrinho, 'w') as f:
        json.dump(data, f, indent=4)

# Função para adicionar um ingrediente
def adicionar_ingrediente(ingrediente):
    data = load_data()
    data["Pratos Principais"]["ingredientes"].append(ingrediente)
    save_data(data)
    print("Ingrediente adicionado ao prato com sucesso!")

# Função para remover um ingrediente
def remover_ingrediente(ingrediente):
    data = load_data()
    if ingrediente in data["Pratos Principais"]["ingredientes"]:
        data["Pratos Principais"]["ingredientes"].remove(ingrediente)
        save_data(data)
        print("Ingrediente removido do prato com sucesso!")
    else:
        print("Ingrediente não encontrado no prato.")

# Função para mostrar os ingredientes
def mostrar_ingredientes():
    data = load_data()
    ingredientes = data["Pratos Principais"]["ingredientes"]
    if ingredientes:
        print("Ingredientes do prato:")
        for ing in ingredientes:
            print(f"- {ing}")
    else:
        print("Nenhum ingrediente no prato.")

# Função para atualizar um ingrediente
def atualizar_ingrediente(ingrediente_antigo, ingrediente_novo):
    data = load_data()
    ingredientes = data["Pratos Principais"]["ingredientes"]
    if ingrediente_antigo in ingredientes:
        index = ingredientes.index(ingrediente_antigo)
        ingredientes[index] = ingrediente_novo
        save_data(data)
        print("Ingrediente atualizado com sucesso!")
    else:
        print("Ingrediente antigo não encontrado no prato.")

# Função para exibir os detalhes do prato
def mostrar_prato():
    data = load_data()
    prato = data["Pratos Principais"]
    print("\nDetalhes do Prato:")
    print(f"ID: {prato['id']}")
    print(f"Nome: {prato['nome']}")
    print(f"Descrição: {prato['descricao']}")
    print(f"Calorias: {prato['calorias']}")
    print("Ingredientes: ", end="")
    if prato["ingredientes"]:
        print(", ".join(prato["ingredientes"]))
    else:
        print("Nenhum")

# Função para exibir o menu
def mensagem_inicio():
    print('-'*20)
    print('PERSONALIZAÇÃO DE PEDIDO')
    print('1- ADICIONAR INGREDIENTE AO PRATO')
    print('2- REMOVER INGREDIENTE DO PRATO')
    print('3- MOSTRAR INGREDIENTES DO PRATO')
    print('4- ATUALIZAR INGREDIENTES DO PRATO')
    print('5- ENVIAR PEDIDO AO CARRINHO')
    print('6- VOLTAR')
    print('-'*20)

# Função principal
def main():
    while True: 
        mostrar_prato()
        mensagem_inicio()
        opcao = input("ESCOLHA UMA OPÇÃO:\n>>> ")

        if opcao == "1":        
            ingrediente = input("Digite o ingrediente que deseja adicionar ao prato: ")
            adicionar_ingrediente(ingrediente)
        elif opcao == "2":
            ingrediente = input("Digite o ingrediente que deseja remover do prato: ")
            remover_ingrediente(ingrediente)
        elif opcao == "3":
            mostrar_ingredientes()
        elif opcao == "4":
            ingrediente_antigo = input("Digite o ingrediente que deseja atualizar: ")
            ingrediente_novo = input("Digite o novo ingrediente: ")
            atualizar_ingrediente(ingrediente_antigo, ingrediente_novo)
        elif opcao == "5":
            print("Pedido enviado ao carrinho com sucesso!!")
            break
        elif opcao == '6':
            print("Voltando...")
            #prato()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
