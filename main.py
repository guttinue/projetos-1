import os
import mudulo_proprietario as proprietario
import modulo_cliente as cliente
import login as login

def menu_inicial ():
    print ("=" *55 )
    print (" ---->>> BEM VINDO AO MENOOTH <<<---- ")
    print ("          1 - MÓDULO USUÁRIO ")
    print ("          2 - MÓDULO PROPRIETÁRIO ")
    print ("          3 - SAIR ")
    print ("=" *55)

def voltar_inicio():
    input('Digite qualquer tecla para voltar o menu')
    os.system('cls')
    main()
    
def finalizar_programa():
    input('Programa finalizado. Digite qualquer tecla para sair')
    exit()

def main():
    menu_inicial()
    opcao_inicial = input("INFORME UMA OPÇÃO: ")
    
    while True:
        if opcao_inicial == '1':
            cliente.main()
        elif opcao_inicial == '2':
            proprietario.main()
        elif opcao_inicial == '3':
            finalizar_programa()
            break
        else:
            voltar_inicio()    
                                
if __name__ == "__main__":
    main()