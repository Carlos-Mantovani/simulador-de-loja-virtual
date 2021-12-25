class Produto:

    lista_de_produtos = []
    apresentacao_dos_produtos = []

    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
        if len(Produto.lista_de_produtos) == 0:
            self.__id = 0
        else:
            self.__id = len(Produto.lista_de_produtos) + 1
        Produto.lista_de_produtos.append(self)
        self.apresentacao = (f"Nome: {self.__nome}, Preço: {self.__preco}")
        Produto.apresentacao_dos_produtos.append(self.apresentacao)

    #def mostrar_produto(self):
        #print("Nome do produto: {}, Preço: {}".format(self.__nome, self.__preco))
    @property
    def nome(self):
        return self.__nome
    @property
    def preco(self):
        return self.__preco
    @property
    def id(self):
        return self.__id
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco
    def mostrar_produto(self):
        print(Produto.apresentacao_dos_produtos[self.__id])