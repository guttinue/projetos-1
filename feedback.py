import os
import json
import time 
import main as top

BANCO_DE_DADOS = 'data\\feedback.json'

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
    with open(BANCO_DE_DADOS, 'r') as arquivo:
        return json.load(arquivo)

def salvar_feedback(lista_feedback):
    with open(BANCO_DE_DADOS, 'w') as arquivo:
        json.dump(lista_feedback, arquivo, indent=4)

def criar_feedback(nome, mensagem):
    lista_feedback = carregar_feedback()
    feedback_id = max([fb['id'] for fb in lista_feedback], default=0) + 1
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
    lista_feedback = [fb for fb in lista_feedback if fb['id'] != feedback_id] 
    salvar_feedback(lista_feedback)
    print(f'Feedback ID {feedback_id} excluído.')

def temporizador():
    tempo = 10

    for x in range(tempo, 0, -1):
        segundos = x % 60
        minutos = int(x / 60) % 60
        horas = int(x / 3600)
        print(f"{horas:02}:{minutos:02}:{segundos:02}")
        time.sleep(1)

    print("O seu pedido chegará em breve!!")


def main():
    while True:
        print('-'*20)
        print("\nMenu de Feedback:")
        print("1. ADICIONAR FEEDBACK")
        print("2. LISTAR FEEDBACKS")
        print("3. ATUALIZAR FEEDBACK")
        print("4. EXCLUIR FEEDBACK")
        print("5. ENCERRAR PEDIDO")
        print('-'*20)

        escolha = input("ESCOLHA UMA OPCAO: ")
        
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
            temporizador()
            input("Digite qualquer tecla para sair")
            top.main()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()