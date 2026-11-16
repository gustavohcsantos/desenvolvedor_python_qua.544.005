from dataclasses import dataclass


@dataclass
class Pessoa:
    # Atributos
    nome: str
    cpf: str
    email: str
    idade: int
    altura: float