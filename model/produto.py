class Produto:
    def __init__(self, codigo,nome,quantidade,preco,descricao):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
        self.descricao = descricao
    def toString(self):
        return f"{self.codigo}, {self.nome}, {self.quantidade}, {self.preco},{self.descricao}"


produto = Produto(10,"livro arquitera comp mario mont", 1, 330,"biblia da arquitetura de computadores")
print(produto.toString())