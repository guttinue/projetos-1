import json
import os
import carrinho as carrinhot
# Define o caminho para o arquivo JSON
carrinho = os.path.join(os.path.dirname(__file__), 'data\\carrinho.json')

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
def adicionar_ingrediente(prato_id, ingrediente):
    data = load_data()
    for prato in data:
        if prato["id"] == prato_id:
            prato["ingredientes"].append(ingrediente)
            save_data(data)
            print("Ingrediente adicionado ao prato com sucesso!")
            return
    print("Prato não encontrado.")

# Função para remover um ingrediente
def remover_ingrediente(prato_id, ingrediente):
    data = load_data()
    for prato in data:
        if prato["id"] == prato_id:
            if ingrediente in prato["ingredientes"]:
                prato["ingredientes"].remove(ingrediente)
                save_data(data)
                print("Ingrediente removido do prato com sucesso!")
                return
            else:
                print("Ingrediente não encontrado no prato.")
                return
    print("Prato não encontrado.")

# Função para mostrar os ingredientes
def mostrar_ingredientes(prato_id):
    data = load_data()
    for prato in data:
        if prato["id"] == prato_id:
            ingredientes = prato["ingredientes"]
            if ingredientes:
                print("Ingredientes do prato:")
                for ing in ingredientes:
                    print(f"- {ing}")
            else:
                print("Nenhum ingrediente no prato.")
            return
    print("Prato não encontrado.")

# Função para atualizar um ingrediente
def atualizar_ingrediente(prato_id, ingrediente_antigo, ingrediente_novo):
    data = load_data()
    for prato in data:
        if prato["id"] == prato_id:
            ingredientes = prato["ingredientes"]
            if ingrediente_antigo in ingredientes:
                index = ingredientes.index(ingrediente_antigo)
                ingredientes[index] = ingrediente_novo
                save_data(data)
                print("Ingrediente atualizado com sucesso!")
                return
            else:
                print("Ingrediente antigo não encontrado no prato.")
                return
    print("Prato não encontrado.")

# Função para exibir os detalhes do prato
def mostrar_prato(prato_id):
    data = load_data()
    for prato in data:
        if prato["id"] == prato_id:
            print("\nDetalhes do Prato:")
            print(f"ID: {prato['id']}")
            print(f"Nome: {prato['nome']}")
            print(f"Descrição: {prato['descricao']}")
            print(f"Preço: {prato['preco']}")
            print("Ingredientes: ", end="")
            if prato["ingredientes"]:
                print(", ".join(prato["ingredientes"]))
            else:
                print("Nenhum")
            return
    print("Prato não encontrado.")

# Função para exibir o menu
def mensagem_inicio():
    print('-'*20)
    print('PERSONALIZAÇÃO DE PEDIDO')
    print('1- ADICIONAR INGREDIENTE AO PRATO')
    print('2- REMOVER INGREDIENTE DO PRATO')
    print('3- MOSTRAR INGREDIENTES DO PRATO')
    print('4- ATUALIZAR INGREDIENTES DO PRATO')
    print('5- VOLTAR')
    print('-'*20)

# Função principal
def main():
    while True:
        prato_id = int(input("Digite o ID do prato que deseja personalizar: "))
        mostrar_prato(prato_id)
        mensagem_inicio()
        opcao = input("ESCOLHA UMA OPÇÃO:\n>>> ")

        if opcao == "1":
            ingrediente = input("Digite o ingrediente que deseja adicionar ao prato: ")
            adicionar_ingrediente(prato_id, ingrediente)
        elif opcao == "2":
            ingrediente = input("Digite o ingrediente que deseja remover do prato: ")
            remover_ingrediente(prato_id, ingrediente)
        elif opcao == "3":
            mostrar_ingredientes(prato_id)
        elif opcao == "4":
            ingrediente_antigo = input("Digite o ingrediente que deseja atualizar: ")
            ingrediente_novo = input("Digite o novo ingrediente: ")
            atualizar_ingrediente(prato_id, ingrediente_antigo, ingrediente_novo)
        elif opcao == "5":
            print("Voltando...")
            os.system('cls')
            carrinhot.main()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()