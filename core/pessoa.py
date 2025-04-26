class Pessoa:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_idade(self):
        return self.idade

    def get_dados(self):
        return self.nome, self.idade

    def set_dados(self, nome, idade):
        self.nome = nome
        self.idade = idade




## minha alteracao sem add