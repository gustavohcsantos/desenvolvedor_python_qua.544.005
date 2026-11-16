# Importa as bibliotecas
import os
import time

# Limpa o terminal
os.system("cls")

# Entrada de dados
n = int(input("Informe um número inteiro: "))

# Contador
while n >= 0:
    os.system("cls")
    print(f"{n}...")
    time.sleep(1)
    n -= 1
print("BOOM!!!!")