class Forma:
    def __init__(self,nome):
        self.nome = nome

    def calcula_Area(self):
            raise NotImplementedError("O método deve ser implementado em uma subclasse")

    def calcula_Perimetro(self):
            raise NotImplementedError("O método deve ser implementado em uma subclasse")

    def __str__(self):
            return f"Nome da Forma: {self.nome}"