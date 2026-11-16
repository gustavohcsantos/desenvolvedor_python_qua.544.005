class Pessoa:
    # Construtor
    def __init__(self,nome,idade,altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    # Método string
    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {len(self)}\nAltura: {float(self)}"

    # Método length
    def __len__(self):
        return self.idade

    # Método float
    def __float__(self):
        return self.altura

    # Destrutor
    def __del__(self):
        print(f"Objeto {self.nome} destruído com sucesso!")