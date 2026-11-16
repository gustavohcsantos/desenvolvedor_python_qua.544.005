# Biblioteca
import os

# Declaração de funções
def boas_vindas(nome):
    print(f"{nome}, seja bem-vindo!")

def limpar():
    os.system("cls" if os.name == "nt" else "clear")


# Algoritmo principal
limpar()
nome = input("Informe seu nome: ").strip().title()
boas_vindas(nome)