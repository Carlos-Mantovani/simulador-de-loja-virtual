from produtos import Produto
from clientes import Cliente

celular = Produto("Cecular", 900.0)
camiseta = Produto("Camiseta", 50.0)

print(celular.mostrar_produto())
print(Produto.lista_de_produtos)

cliente1 = Cliente("Carlos", "sherifinho.augusto@gmail.com", 200.0)

cliente1.comprar(1)

print(Produto.lista_de_produtos)
print(cliente1.dinheiro)