from PensamentoOrientado import Mercado
class Tipo(Mercado):
    nome = ""
    funçao = ""
    estado = ""

    def apresentarSe(self):
        print(f"Olá, sou um mercado de reposição, Meu nome é {self.nome}!") 