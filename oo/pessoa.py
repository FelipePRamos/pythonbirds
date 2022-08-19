class Pessoa:
    olhos=2
    def __init__(self, *filhos, nome=None, idade=31):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
   olhos = 3

if __name__ == '__main__':
    felipe = Mutante(nome='Felipe')
    luciano = Homem(felipe, nome='Luciano')
    print(Homem.cumprimentar(luciano))
    print(id(luciano))

    print(luciano.nome)
    print(luciano.idade)

    for filho in luciano.filhos:
        print(filho.nome)

    luciano.sobrenome = 'Ramos'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(felipe.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(felipe.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(felipe.olhos))

    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes(),luciano.nome_e_atributos_de_classes())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(felipe.olhos)