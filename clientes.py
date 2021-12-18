class Cliente:
    def __init__(self, nome, email, dinheiro):
        self.__nome = nome
        self.__email = email
        self.__dinheiro = dinheiro

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def dinheiro(self):
        return self.__dinheiro

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @email.setter
    def email(self, novo_email):
        self.__email = novo_email


