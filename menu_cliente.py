import os
import json
import personalizacao as personalizacao

arquivo_cardapio = os.path.join(os.path.dirname(__file__), 'data\\cardapio.json')
arquivo_carrinho = os.path.join(os.path.dirname(__file__), 'data\\carrinho.json')

def carregar_dados(arquivo):
    if not os.path.exists(arquivo):
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump([], f)
    with open(arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_dados(dados, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4)

def mostrar_pratos_categoria(categoria):
    dados = carregar_dados(arquivo_cardapio)
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

def selecionar_prato(categoria):
    while True:
        opcao = input("Digite o ID do prato que deseja adicionar ao carrinho ('V' para voltar): ").strip().lower()
        if opcao == 'v':
            return
        try:
            id_prato = int(opcao)
            dados = carregar_dados(arquivo_cardapio)
            for prato in dados:
                if prato['id'] == id_prato and prato['categoria'] == categoria:
                    carrinho = carregar_dados(arquivo_carrinho)
                    carrinho.append(prato)
                    salvar_dados(carrinho, arquivo_carrinho)
                    print("Prato adicionado ao carrinho com sucesso!")
                    return
            print("Prato não encontrado.")
        except ValueError:
            print("Opção inválida. Por favor, digite um número válido ou 'V' para voltar.")

def selecionar_categoria():
    categorias = ["Entradas", "Promoções", "Bebidas", "Sobremesas", "Pratos Principais"]
    print("Selecione uma categoria:")
    for i, categoria in enumerate(categorias, 1):
        print(f"{i}. {categoria}")
    opcao = input("Escolha uma opção (ou 'S' para sair): ").strip().lower()
    if opcao == 's':
        return None
    try:
        opcao = int(opcao)
        return categorias[opcao - 1]
    except (ValueError, IndexError):
        print("Opção inválida. Por favor, escolha uma opção válida ou 'S' para sair.")

def main():
    os.system('cls')
    while True:
        categoria = selecionar_categoria()
        if categoria is None:
            break
        os.system('cls')
        mostrar_pratos_categoria(categoria)
        selecionar_prato(categoria)
        continuar = input("Deseja continuar (S/N)?").strip().lower()
        if continuar != 's':
            break
            

if __name__ == '__main__':
    main()
