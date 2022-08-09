class Pessoa:
    olhos=2
    def __init__(self, *filhos, nome=None, idade=31):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'

if __name__ == '__main__':
    felipe = Pessoa(nome='Felipe')
    luciano =Pessoa(felipe, nome='Luciano')
    print(Pessoa.cumprimentar)
    print(id(luciano))
    print(luciano.cumprimentar)
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(felipe.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(felipe.olhos))


