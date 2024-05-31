import os 
import json

CATEGORIAS_JSON = 'data\\categorias.json'

def carregar_categorias():
    if not os.path.exists(CATEGORIAS_JSON):
        return []
    with open(CATEGORIAS_JSON, 'r') as f:
        return json.load(f)

            # Função para salvar as categorias no arquivo JSON
def salvar_categorias(categorias):
        with open(CATEGORIAS_JSON, 'w') as f:
            json.dump(categorias, f, indent=4)

            # Função para criar uma nova categoria
def create_categoria(nome, arquivo):
    categorias = carregar_categorias()
    nova_categoria = {
        'id': len(categorias) + 1,
        'nome': nome,
    }
    categorias.append(nova_categoria)
    salvar_categorias(categorias)
    print(f"Categoria '{nome}' criada com sucesso.")

            # Função para ler (listar) todas as categorias
def read_categorias():
    categorias = carregar_categorias()
    if categorias:
        print("Lista de categorias:")
        for categoria in categorias:
            print(f"ID: {categoria['id']}, Nome: {categoria['nome']}")
    else:
        print("Nenhuma categoria encontrada.")

            # Função para atualizar os dados de uma categoria
def update_categoria(categoria_id, novo_nome=None):
    categorias = carregar_categorias()
    for categoria in categorias:
        if categoria['id'] == categoria_id:
            if novo_nome:
                categoria['nome'] = novo_nome
            salvar_categorias(categorias)
            print(f"Categoria ID '{categoria_id}' atualizada com sucesso.")
            return
    print(f"Categoria ID '{categoria_id}' não encontrada.")

            # Função para excluir uma categoria
def delete_categoria(categoria_id):
    categorias = carregar_categorias()
    categorias = [categoria for categoria in categorias if categoria['id'] != categoria_id]
    salvar_categorias(categorias)
    print(f"Categoria ID '{categoria_id}' excluída com sucesso.")


            # Exemplo de uso
def main():
    while True:
        print('-'*20)
        print("\nMenu de Categorias:")
        print("1. CRIAR NOVA CATEGORIA")
        print("2. LISTAR CATEGORIAS")
        print("3. ATUALIZAR CATEGORIA")
        print("4. EXCLUIR CATEGORIA")
        print("5. VOLTAR")
        print('-'*20)
                    
        escolha = input("Escolha uma opção (1-5): ")
                    
        if escolha == '1':
            nome = input("Nome da nova categoria: ")
            arquivo = input("Nome do arquivo JSON para a categoria: ")
            create_categoria(nome, arquivo)
        elif escolha == '2':
            read_categorias()
        elif escolha == '3':
            categoria_id = int(input("ID da categoria a ser atualizada: "))
            novo_nome = input("Novo nome da categoria (pressione Enter para manter o nome atual): ")
            update_categoria(categoria_id, novo_nome if novo_nome else None)
        elif escolha == '4':
            categoria_id = int(input("ID da categoria a ser excluída: "))
            delete_categoria(categoria_id)
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
