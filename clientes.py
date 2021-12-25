from produtos import Produto
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

    def depositar_dinheiro(self, valor):
        self.__dinheiro += valor

    def comprar(self, id_produto):
        if id_produto <= len(Produto.lista_de_produtos):
            produto = Produto.lista_de_produtos[id_produto]
            produto_apresentacao = Produto.apresentacao_dos_produtos[id_produto]
            if self.__dinheiro >= produto.preco:
                self.__dinheiro -= produto.preco
                Produto.lista_de_produtos.remove(produto)
                Produto.apresentacao_dos_produtos.remove(produto_apresentacao)
                print("{} Comprado por {}".format(produto.nome, produto.preco))
            else:
                print("Você não possui dinheiro suficiente")
        else:
            print("Produto não existe")