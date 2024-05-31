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
    main()

def main():
    while True:
        menu_inicial()
        opcao_inicial = int(input("INFORME UMA OPÇÃO: "))

        match (opcao_inicial):
            case 1:
                cliente.main()
            case 2:
                proprietario.main()
            case 3: 
                break
            case __:
                print("Opção inválida, por favor tente novamente.")
                voltar_inicio()      
                                
if __name__ == "__main__":
    main()