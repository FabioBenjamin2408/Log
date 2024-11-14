class animal:
    def __init__(self, nome):
        self.nome = nome

    def som(self):
        return "Som de animal"
    
class Cachorro(animal):
    def som(self):
        return "Latido"
    
class Gato(animal):
    def som(self):
        return "Miau"
    
cachorro = Cachorro("Leila")
gato = Gato("Jack")

print(cachorro.nome)
print(cachorro.som())
print(gato.nome)
print(gato.som())