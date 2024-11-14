class Pessoa:
    def __init__(self, idade, nome):
        self.nome = nome
        self.idade = idade
    def exibir(self):
        print(f"nome: {self.nome}, idade: {self.idade}")
        
p1 = Pessoa("Fabio", 14)
p2 = Pessoa("Sirte", 59)
p1.exibir()
p2.exibir()