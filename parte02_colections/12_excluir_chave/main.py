# Dicionário
usuario = {
    'nome': "Alex Machado",
    'idade': 41,
    'email': "alex@gmail.com",
    'telefone': "(61) 98765-4321",
    'endereço': "Campo da Esperança"
}

# Exibe a lista original
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")

# Informa a chave a ser deletada
chave_escolhida = input("Informe a chave a excluir: ").strip().lower()

# Deleta a chave
del usuario[chave_escolhida]

# Re-exibe o novo dicionário
for chave, valor in usuario.items():
    print(f"{chave}: {valor}")