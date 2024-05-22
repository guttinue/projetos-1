import os
import json
from time import sleep
import time

arquivo = os.path.join(os.path.dirname(__file__), 'data\\carrinho.json')

def mostrar_pedido():
    with open(arquivo, 'r') as f:
        dados = json.load(f)

    prato = dados.get("Pratos Principais")
    if prato:
        print("=" * 50)
        print("DETALHES DO PRATO:")
        print("-" * 50)
        print(f"ID: {prato['id']}")
        print(f"NOME: {prato['nome']}")
        print(f"DESCRIÇÃO: {prato['descricao']}")
        print(f"CALORIAS: {prato['calorias']}")
        print("INGREDIENTES:")
        for ingrediente in prato['ingredientes']:
            print(f"- {ingrediente}")
        print("=" * 50)
    else:
        print("😒 NENHUM PRATO NO CARRINHO.")

def remover_pedido():
    with open(arquivo, 'w') as f:
        json.dump({}, f, indent=4)
    print("😡 PRATO EXCLUÍDO COM SUCESSO!")

def atualizar_pedido():
    with open(arquivo, 'r') as f:
        dados = json.load(f)

    prato = dados.get("Pratos Principais")
    if not prato:
        print("Nenhum prato para atualizar.")
        return

    novos_ingredientes = input("Digite os novos ingredientes do prato (separados por vírgula):\n>>> ").split(',')

    # Recuperar os ingredientes atuais do prato
    ingredientes_atuais = prato.get('ingredientes', [])

    # Adicionar os novos ingredientes aos ingredientes atuais
    ingredientes_atuais.extend([ingrediente.strip() for ingrediente in novos_ingredientes])

    prato['ingredientes'] = ingredientes_atuais

    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)
    print("😙 PRATO ATUALIZADO COM SUCESSO!")


# direcionar para funcao de adicionar prato
def adicionar_prato_carrinho():
    nome = input("Digite o nome do prato: ")
    descricao = input("Digite a descrição do prato: ")
    calorias = input("Digite as calorias do prato: ")
    ingredientes = input("Digite os ingredientes do prato (separados por vírgula): ").split(',')

    novo_prato = {
        "id": 1,
        "nome": nome,
        "descricao": descricao,
        "calorias": calorias,
        "ingredientes": [ingrediente.strip() for ingrediente in ingredientes]
    }

    with open(arquivo, 'w') as f:
        json.dump({"Pratos Principais": novo_prato}, f, indent=4)
    print("Prato adicionado ao carrinho com sucesso!")

def finalizar_pedido():
    with open(arquivo, 'r') as f:
        dados = json.load(f)

    prato = dados.get("Pratos Principais")
    if prato:
        print("Seu pedido foi finalizado com sucesso!")
        print("Aqui estão os detalhes do seu pedido:")
        mostrar_pedido()
        with open(arquivo, 'w') as f:
            json.dump({}, f, indent=4)
    else:
        print("Não há pedidos para finalizar.")

def tempo_espera():
    my_time = int(input("Enter the time in seconds: "))

    for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)

    print("TIME'S UP!")

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
    print('| CARRINHO                                   |')
    print('| 1- MOSTRAR PEDIDO                          |')
    print('| 2- REMOVER PEDIDO                          |')
    print('| 3- ATUALIZAR PEDIDO                        |')
    print('| 4- ADICIONAR NOVO PEDIDO                   |')
    print('| 5- FINALIZAR PEDIDO                        |')
    print('-'*20)

def main():
    exibir_titulo()
    while True:
        mensagem_inicio()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            mostrar_pedido()
        elif opcao == 2:
            remover_pedido()
        elif opcao == 3:
            atualizar_pedido()
        elif opcao == 4:
            adicionar_prato_carrinho()
        elif opcao == 5:
            finalizar_pedido()
            # funcao do feedback
            opcao_feedback = input("Deseja realizar um feedback? (s/n): ")
            if opcao_feedback.lower() == 'n':
                print("Obrigado por usar o sistema!")
                break
        else:
            print("Opção inválida, por favor digite novamente")

if __name__ == '__main__':
    main()
