
class Mercado:
    nome = ""
    pais = ""
    estado = ""
    preço = ""
    autorizacao = ""

    def __init__(self,nome,pais,estado,preco,autorizacao):
        self.nome = nome
        self.pais = pais
        self.estado = estado
        self.preco = preco
        self.autorizacao = autorizacao

    def apresentarSe(self):
        print(f"Olá, sou um mercado de ação, Meu nome é {self.nome}!")    
