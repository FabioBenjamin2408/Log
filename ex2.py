class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 
    def exibir(self):
        print(f" marca: {self.marca}, modelo: {self.modelo}, ano: {self.ano}")
        
c1 = Carro("fiat", "Idea", 1989)
c2 = Carro("Honda", "City", 2024)
c3 = Carro("Toyota", "supra", 1999)
c1.exibir()
c2.exibir()