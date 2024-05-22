import time
import login as carne

# 1800 segundos - 30 minutos
my_time = 10

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")

email = input('Digite seu email:')
senha = input('Crie sua senha: ')
carne.cadastrar_usuario(email, senha)

