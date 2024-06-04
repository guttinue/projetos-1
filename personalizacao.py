import json
import os
import carrinho as carrinhot

carrinho = os.path.join(os.path.dirname(__file__), 'data\\carrinho.json')

def carreagar_dados():
    if os.path.exists(carrinho):
        with open(carrinho, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError as e:
                print(f"Erro ao carregar dados: {e}")
                return []
    return []

def salvar_dados(data):
    with open(carrinho, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def adicionar_ingrediente(prato_id, ingrediente):
    data = carreagar_dados()
    prato_encontrado = False
    for prato in data:
        if str(prato["id"]) == str(prato_id):
            prato["ingredientes"].append(ingrediente)
            salvar_dados(data)
            print("Ingrediente adicionado ao prato com sucesso!")
            prato_encontrado = True
            break
    if not prato_encontrado:
        print("Prato não encontrado.")

def remover_ingrediente(prato_id, ingrediente):
    data = carreagar_dados()
    prato_encontrado = False
    for prato in data:
        if str(prato["id"]) == str(prato_id):
            if ingrediente in prato["ingredientes"]:
                prato["ingredientes"].remove(ingrediente)
                salvar_dados(data)
                print("Ingrediente removido do prato com sucesso!")
            else:
                print("Ingrediente não encontrado no prato.")
            prato_encontrado = True
            break
    if not prato_encontrado:
        print("Prato não encontrado.")

def mostrar_ingredientes(prato_id):
    data = carreagar_dados()
    prato_encontrado = False
    for prato in data:
        if str(prato["id"]) == str(prato_id):
            ingredientes = prato["ingredientes"]
            if ingredientes:
                print("Ingredientes do prato:")
                for ing in ingredientes:
                    print(f"- {ing}")
            else:
                print("Nenhum ingrediente no prato.")
            prato_encontrado = True
            break
    if not prato_encontrado:
        print("Prato não encontrado.")

def atualizar_ingrediente(prato_id, ingrediente_antigo, ingrediente_novo):
    data = carreagar_dados()
    prato_encontrado = False
    for prato in data:
        if str(prato["id"]) == str(prato_id):
            ingredientes = prato["ingredientes"]
            if ingrediente_antigo in ingredientes:
                index = ingredientes.index(ingrediente_antigo)
                ingredientes[index] = ingrediente_novo
                salvar_dados(data)
                print("Ingrediente atualizado com sucesso!")
            else:
                print("Ingrediente antigo não encontrado no prato.")
            prato_encontrado = True
            break
    if not prato_encontrado:
        print("Prato não encontrado.")
def mostrar_prato(prato_id):
    data = carreagar_dados()
    prato_encontrado = False
    for prato in data:
        if str(prato["id"]) == str(prato_id):
            print("\nDetalhes do Prato:")
            print(f"ID: {prato['id']}")
            print(f"Nome: {prato['nome']}")
            print(f"Descrição: {prato['descricao']}")
            print(f"Preço: {prato.get('preco', 'N/A')}")
            print("Ingredientes: ", end="")
            if prato["ingredientes"]:
                print(", ".join(prato["ingredientes"]))
            else:
                print("Nenhum")
            prato_encontrado = True
            break
    if not prato_encontrado:
        print("Prato não encontrado.")

def mensagem_inicio():
    print('-'*20)
    print('PERSONALIZAÇÃO DE PEDIDO')
    print('1- ADICIONAR INGREDIENTE AO PRATO')
    print('2- REMOVER INGREDIENTE DO PRATO')
    print('3- MOSTRAR INGREDIENTES DO PRATO')
    print('4- ATUALIZAR INGREDIENTES DO PRATO')
    print('5- VOLTAR')
    print('-'*20)

def main():
    prato_id = input("Digite o ID do prato que deseja personalizar: ")
    mostrar_prato(prato_id)

    while True:
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
            print("Opção inválida, por favor digite novamente")

if __name__ == "__main__":
    main()
