import os
import json

# Caminho do arquivo JSON
arquivo_cardapio = os.path.join(os.path.dirname(__file__), 'data\\cardapio.json')
CATEGORIAS_JSON = 'data\\categorias.json'

# Funções de manipulação do JSON
def carregar_dados(arquivo):
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f)
    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar_dados(dados, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def carregar_categorias():
    if not os.path.exists(CATEGORIAS_JSON):
        return []
    with open(CATEGORIAS_JSON, 'r') as f:
        return json.load(f)

# Função para adicionar um prato
def adicionar_prato():
    dados = carregar_dados(arquivo_cardapio)
    nome = input("Digite o nome do prato: ")
    descricao = input("Digite a descrição do prato: ")
    preco = float(input("Digite o preço do prato: "))
    ingredientes = input("Digite os ingredientes do prato (separados por vírgula): ").split(',')
    categoria = selecionar_categoria()

    novo_prato = {
        "id": len(dados) + 1,
        "nome": nome,
        "descricao": descricao,
        "preco": preco,
        "ingredientes": [ingrediente.strip() for ingrediente in ingredientes],
        "categoria": categoria
    }

    dados.append(novo_prato)
    salvar_dados(dados, arquivo_cardapio)
    print("Prato adicionado ao cardápio com sucesso!")

# Função para mostrar pratos por categoria
def mostrar_cardapio_por_categoria():
    dados = carregar_dados(arquivo_cardapio)
    categoria = selecionar_categoria()
    pratos_categoria = [prato for prato in dados if prato['categoria'] == categoria]

    if pratos_categoria:
        print(f"Categoria: {categoria}")
        print("=" * 50)
        for prato in pratos_categoria:
            print(f"ID: {prato['id']}")
            print(f"NOME: {prato['nome']}")
            print(f"DESCRIÇÃO: {prato['descricao']}")
            print(f"PREÇO: R${prato['preco']:.2f}")
            print("INGREDIENTES:")
            for ingrediente in prato['ingredientes']:
                print(f"- {ingrediente}")
            print("=" * 50)
    else:
        print(f"Nenhum prato encontrado na categoria {categoria}.")

# Função para atualizar um prato
def atualizar_prato():
    dados = carregar_dados(arquivo_cardapio)
    id_prato = int(input("Digite o ID do prato que deseja atualizar: "))
    prato = next((p for p in dados if p['id'] == id_prato), None)

    if prato:
        novo_nome = input(f"Digite o novo nome do prato (atual: {prato['nome']}): ")
        nova_descricao = input(f"Digite a nova descrição do prato (atual: {prato['descricao']}): ")
        novo_preco = float(input(f"Digite o novo preço do prato (atual: R${prato['preco']:.2f}): "))
        novos_ingredientes = input(f"Digite os novos ingredientes do prato (atual: {', '.join(prato['ingredientes'])}) (separados por vírgula): ").split(',')
        nova_categoria = selecionar_categoria()

        prato['nome'] = novo_nome
        prato['descricao'] = nova_descricao
        prato['preco'] = novo_preco
        prato['ingredientes'] = [ingrediente.strip() for ingrediente in novos_ingredientes]
        prato['categoria'] = nova_categoria

        salvar_dados(dados, arquivo_cardapio)
        print("Prato atualizado com sucesso!")
    else:
        print("Prato não encontrado.")

# Função para remover um prato
def remover_prato():
    dados = carregar_dados(arquivo_cardapio)
    id_prato = int(input("Digite o ID do prato que deseja remover: "))
    prato = next((p for p in dados if p['id'] == id_prato), None)

    if prato:
        dados.remove(prato)
        salvar_dados(dados, arquivo_cardapio)
        print("Prato removido com sucesso!")
    else:
        print("Prato não encontrado.")

# Função para selecionar categoria
def selecionar_categoria():
    categorias = carregar_categorias()
    print("Selecione uma categoria:")
    for i, categoria in enumerate(categorias, 1):
        print(f"{i}. {categoria['nome']}")
    opcao = int(input("Escolha uma opção: "))
    return categorias[opcao - 1]['nome']

# Função para exibir o menu principal
def exibir_menu():
    os.system('cls')
    print('-'*20)
    print("1- ADICIONAR PRATO")
    print("2- MOSTRAR PRATO")
    print("3- ATUALIZAR PRATO")
    print("4- REMOVER PRATO")
    print("5- SAIR")
    print('-'*20)

# Função principal
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_prato()
        elif opcao == '2':
            mostrar_cardapio_por_categoria()
            input("Pressione enter para continuar")
        elif opcao == '3':
            mostrar_cardapio_por_categoria()
            atualizar_prato()
        elif opcao == '4':
            mostrar_cardapio_por_categoria()
            remover_prato()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida, por favor tente novamente.")

if __name__ == '__main__':
    main()