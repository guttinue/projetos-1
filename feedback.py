import os
import json
import time
import login as login

BANCO_DE_DADOS = 'data\\feedbacks.json'

def exibir_titulo():
    print('''
    ███╗░░░███╗███████╗███╗░░██╗░█████╗░░█████╗░████████╗██╗░░██╗
    ████╗░████║██╔════╝████╗░██║██╔══██╗██╔══██╗╚══██╔══╝██║░░██║
    ██╔████╔██║█████╗░░██╔██╗██║██║░░██║██║░░██║░░░██║░░░███████║
    ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░██║██║░░██║░░░██║░░░██╔══██║
    ██║░╚═╝░██║███████╗██║░╚███║╚█████╔╝╚█████╔╝░░░██║░░░██║░░██║
    ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝''')

def carregar_feedback():
    if not os.path.exists(BANCO_DE_DADOS):
        return []
    with open(BANCO_DE_DADOS) as arquivo:
        return json.load(arquivo)

def salvar_feedback(lista_feedback):
    with open(BANCO_DE_DADOS) as arquivo:
        json.dump(lista_feedback, arquivo, indent=4)

def criar_feedback(nome, mensagem):
    lista_feedback = carregar_feedback()
    feedback_id = max([variavel['id'] for variavel in lista_feedback], default=0) + 1
    novo_feedback = {
        'id': feedback_id,
        'nome': nome,
        'mensagem': mensagem
    }
    lista_feedback.append(novo_feedback)
    salvar_feedback(lista_feedback)
    print(f'Feedback adicionado com ID {feedback_id}.')

def ler_feedback():
    lista_feedback = carregar_feedback()
    if not lista_feedback:
        print('Nenhum feedback encontrado.')
    for feedback in lista_feedback:
        print(f"ID: {feedback['id']}, Nome: {feedback['nome']}, Mensagem: {feedback['mensagem']}")

def atualizar_feedback(feedback_id, novo_nome, nova_mensagem):
    lista_feedback = carregar_feedback()
    for feedback in lista_feedback:
        if feedback['id'] == feedback_id:
            feedback['nome'] = novo_nome
            feedback['mensagem'] = nova_mensagem
            salvar_feedback(lista_feedback)
            print(f'Feedback ID {feedback_id} atualizado.')
            return
    print(f'Feedback ID {feedback_id} não encontrado.')

def excluir_feedback(feedback_id):
    lista_feedback = carregar_feedback()
    lista_feedback = [variavel for variavel in lista_feedback if variavel['id'] != feedback_id]
    salvar_feedback(lista_feedback)
    print(f'Feedback ID {feedback_id} excluído.')

def tempo_espera():
    my_time = 30

    for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)

    +-print("TIME'S UP!")

def main():
    exibir_titulo()
    while True:
        print("\nMenu de Feedback:")
        print("1. Adicionar Feedback")
        print("2. Ler Feedbacks")
        print("3. Atualizar Feedback")
        print("4. Excluir Feedback")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Nome: ")
            mensagem = input("Mensagem: ")
            criar_feedback(nome, mensagem)
        elif escolha == '2':
            ler_feedback()
        elif escolha == '3':
            feedback_id = int(input("ID do Feedback para atualizar: "))
            novo_nome = input("Novo Nome: ")
            nova_mensagem = input("Nova Mensagem: ")
            atualizar_feedback(feedback_id, novo_nome, nova_mensagem)
        elif escolha == '4':
            feedback_id = int(input("ID do Feedback para excluir: "))
            excluir_feedback(feedback_id)
        elif escolha == '5':
            tempo_espera()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()