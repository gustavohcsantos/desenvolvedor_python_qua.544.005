# Dicionário
usuario = {
    'nome': "Alex Machado",
    'idade': 41,
    'altura': 1.72,
    'email': "alex@gmail.com",
    'cpf': "123.456.789-12",
    'telefone': "(61) 98765-4321"
}

# Exibe valor específico
print(f"Nome: {usuario['nome']}")
print(f"E-mail: {usuario.get('email')}")

# Percorre o dicionário
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}.")