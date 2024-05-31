import os
import json
import menu_cliente as cliente
import feedback as feedback
import personalizacao as personalizacao 
import modulo_cliente as modulo

arquivo_carrinho = os.path.join(os.path.dirname(__file__), 'data\\carrinho.json')
arquivo_pedidos = os.path.join(os.path.dirname(__file__), 'data\\pedidos.json')

def carregar_dados(arquivo):
    if not os.path.exists(arquivo):
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump([], f)
    with open(arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_dados(dados, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4)

def mostrar_pedido():
    dados = carregar_dados(arquivo_carrinho)

    if dados:  # Verifica se há dados no arquivo
        print("=" * 50)
        print("DETALHES DOS PRATOS:")
        print("-" * 50)
        for prato in dados:  # Itera sobre cada prato na lista
            print(f"ID: {prato['id']}")
            print(f"NOME: {prato['nome']}")
            print(f"DESCRIÇÃO: {prato['descricao']}")
            print(f"PREÇO: R${prato['preco']:.2f}")
            print("INGREDIENTES:")
            for ingrediente in prato['ingredientes']:
                print(f"- {ingrediente}")
            print("=" * 50)
    else:
        print("😒 NENHUM PRATO NO CARRINHO.")

def remover_pedido():
    salvar_dados([], arquivo_carrinho)  # Sobrescreve o arquivo com uma lista vazia
    print("😡 TODOS OS PRATOS FORAM EXCLUÍDOS COM SUCESSO!")

def atualizar_pedido():
    dados = carregar_dados(arquivo_carrinho)

    if dados:  # Verifica se há dados no arquivo
        id_prato = int(input("Digite o ID do prato que deseja atualizar: "))
        for prato in dados:
            if prato['id'] == id_prato:  # Verifica se o ID do prato corresponde ao fornecido pelo usuário
                novos_ingredientes = input("Digite os novos ingredientes do prato (separados por vírgula):\n>>> ").split(',')
                prato['ingredientes'].extend([ingrediente.strip() for ingrediente in novos_ingredientes])
                salvar_dados(dados, arquivo_carrinho)
                print("😙 PRATO ATUALIZADO COM SUCESSO!")
                return
        print("ID do prato não encontrado.")
    else:
        print("Nenhum prato para atualizar.")

def finalizar_pedido():
    dados_carrinho = carregar_dados(arquivo_carrinho)

    if dados_carrinho:  # Verifica se há pedidos no carrinho
        print("Seu pedido foi finalizado com sucesso!")
        print("Aqui estão os detalhes do seu pedido:")
        mostrar_pedido()
        
        # Carrega os pedidos existentes
        pedidos = carregar_dados(arquivo_pedidos)
        
        # Adiciona os pedidos do carrinho ao arquivo de pedidos
        pedidos.extend(dados_carrinho)
        
        # Salva os pedidos atualizados no arquivo de pedidos
        salvar_dados(pedidos, arquivo_pedidos)
        
        # Limpa o carrinho
        salvar_dados([], arquivo_carrinho)
    else:
        print("Não há pedidos para finalizar.")

def exibir_titulo():
    print('''
 ███╗░░░███╗███████╗███╗░░██╗░█████╗░░█████╗░████████╗██╗░░██╗
 ████╗░████║██╔════╝████╗░██║██╔══██╗██╔══██╗╚══██╔══╝██║░░██║
 ██╔████╔██║█████╗░░██╔██╗██║██║░░██║██║░░██║░░░██║░░░███████║
 ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░██║██║░░██║░░░██║░░░██╔══██║
 ██║░╚═╝░██║███████╗██║░╚███║╚█████╔╝╚█████╔╝░░░██║░░░██║░░██║
 ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝''')

def mensagem_inicio():
    print('-'*20)
    print('| CARRINHO                      |')
    print('| 1- MOSTRAR PEDIDO             |')
    print('| 2- REMOVER PEDIDO             |')
    print('| 3- ATUALIZAR PEDIDO           |')
    print('| 4- ADICIONAR NOVO PEDIDO      |')
    print('| 5- PERSONALIZAR PEDIDO        |')
    print('| 6- FINALIZAR PEDIDO           |')
    print('| 7- VOLTAR AO MENU CLIENTE     |')
    print('-'*20)

def main():
    while True:
        mensagem_inicio()
        opcao = (input("Escolha uma opção: "))

        if opcao == '1':
            os.system('cls')
            mostrar_pedido()
        elif opcao == '2':
            remover_pedido()
        elif opcao == '3':
            os.system('cls')
            mostrar_pedido()
            atualizar_pedido()
        elif opcao == '4':
            cliente.main()
        elif opcao == '5':
            os.system('cls')
            mostrar_pedido()
            personalizacao.main()
        elif opcao == '6':
            os.system('cls')
            finalizar_pedido()
            # funcao do feedback
            opcao_feedback = input("Deseja realizar um feedback? (s/n): ")
            if opcao_feedback.lower() == 's':
                feedback.main()
                
            elif opcao_feedback.lower() == 'n':
                feedback.temporizador()
                break
            else:
                print("Opção inválida, por favor digite novamente")
                finalizar_pedido()
            
        elif opcao == '7':
            modulo.main()
        else:
            print("Opção inválida, por favor digite novamente")

if __name__ == '__main__':
    main()
