class Animal:

    def __init__(self, nome: str, idade: int):

        self.nome = nome
        self.idade = idade

    def apresenta(self):

        print(f'Esse é o {self.nome} e tem {self.idade} anos.')

class Meu_animal(Animal):

    def __init__(self, nome, idade, raca: str, peso: str):
        super().__init__(nome, idade)
        self.raca = raca
        self.peso = peso

    def apresenta(self):
        super().apresenta()
        print(f'Ele é da raça {self.raca} e pesa {self.peso}.')

meu_pet = Meu_animal('Bidu', 12, 'lhasa apso',14)

meu_pet.apresenta()
print(meu_pet.nome)
print(meu_pet.idade)
print(meu_pet.raca)
print(meu_pet.peso)