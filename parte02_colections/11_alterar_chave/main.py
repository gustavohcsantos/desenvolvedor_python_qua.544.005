# Biblioteca
import os

# Dicionário
usuario = {
    'nome': "Thomas Anderson",
    'idade': 40,
    'email': "mranderson@gmail.com",
    'telefone': "(61) 96666-6666"
}

# Limpa terminal
os.system("cls" if os.name == "nt" else "clear")

# Loop
while True:
    # Exibe o dicionário
    for chave, valor in usuario.items():
        print(f"{chave}: {valor}")

    # Informa o nome da chave
    chave_escolhida = input("Informe o nome da chave que deseja alterar ou Enter para encerrar: ").strip().lower()
    # Verifica se a chave é válida
    if chave_escolhida:
        # Informa o novo valor
        usuario[chave_escolhida] = input("Informe o novo valor: ").strip()
        continue
    else:
        break