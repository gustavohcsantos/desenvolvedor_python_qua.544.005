# Classe
class Pessoa:
    def __init__(self,nome,idade,cpf,telefone,email):
        self.__nome = nome 
        self.__idade = idade
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email

    # Métodos set e get
    @property # Método get
    def nome(self):
        return self.__nome

    @nome.setter # Método set
    def nome(self,nome):
        self.__nome = nome

    @property # Método get
    def idade(self):
        return self.__idade

    @idade.setter # Método set
    def idade(self,idade):
        self.__idade = idade

    @property # Método get
    def cpf(self):
        return self.__cpf

    @cpf.setter # Método set
    def cpf(self,cpf):
        self.__cpf = cpf

    @property # Método get
    def telefone(self):
        return self.__telefone

    @telefone.setter # Método set
    def telefone(self,telefone):
        self.__telefone = telefone

    @property # Método get
    def email(self):
        return self.__email

    @email.setter # Método set
    def email(self,email):
        self.__email = email