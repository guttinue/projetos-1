import os
import json

CATEGORIAS_JSON = 'data\\categorias.json'
CARDAPIO_JSON = 'data\\cardapio.json'

def carregar_categorias():
    if not os.path.exists(CATEGORIAS_JSON):
        return []
    with open(CATEGORIAS_JSON, 'r') as f:
        return json.load(f)

def salvar_categorias(categorias):
    with open(CATEGORIAS_JSON, 'w') as f:
        json.dump(categorias, f, indent=4)

def criar_categoria(nome):
    categorias = carregar_categorias()
    nova_categoria = {
        'id': len(categorias) + 1,
        'nome': nome
    }
    categorias.append(nova_categoria)
    salvar_categorias(categorias)
    print(f"Categoria '{nome}' criada com sucesso.")

def ler_categorias():
    categorias = carregar_categorias()
    if categorias:
        print("Lista de categorias:")
        for categoria in categorias:
            print(f"ID: {categoria['id']}, Nome: {categoria['nome']}")
    else:
        print("Nenhuma categoria encontrada.")

def atualizar_categoria(categoria_id, novo_nome=None):
    categorias = carregar_categorias()
    for categoria in categorias:
        if categoria['id'] == categoria_id:
            if novo_nome:
                categoria['nome'] = novo_nome
            salvar_categorias(categorias)
            print(f"Categoria ID '{categoria_id}' atualizada com sucesso.")
            return
    print(f"Categoria ID '{categoria_id}' não encontrada.")

def deletar_categoria(categoria_id):
    categorias = carregar_categorias()
    categorias = [categoria for categoria in categorias if categoria['id'] != categoria_id]
    salvar_categorias(categorias)
    print(f"Categoria ID '{categoria_id}' excluída com sucesso.")

def main():
    while True:
        os.system('cls')
        print('-'*20)
        print("MENU DE CATEGORIAS")
        print("1. CRIAR NOVA CATEGORIA")
        print("2. LISTAR CATEGORIAS")
        print("3. ATUALIZAR CATEGORIA")
        print("4. EXCLUIR CATEGORIA")
        print("5. VOLTAR")
        print('-'*20)
                    
        escolha = input("Escolha uma opção (1-5): ")
                    
        if escolha == '1':
            nome = input("Nome da nova categoria: ")
            criar_categoria(nome)
        elif escolha == '2':
            ler_categorias()
        elif escolha == '3':
            ler_categorias()
            categoria_id = int(input("ID da categoria a ser atualizada: "))
            novo_nome = input("Novo nome da categoria (pressione Enter para manter o nome atual): ")
            atualizar_categoria(categoria_id, novo_nome if novo_nome else None)
        elif escolha == '4':
            ler_categorias()
            categoria_id = int(input("ID da categoria a ser excluída: "))
            deletar_categoria(categoria_id)
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
