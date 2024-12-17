class Inimigo:
    inimigos = []

    def __init__(self, nome, vida, fraqueza):
        self.nome = nome
        self.vida = vida
        self.fraqueza = fraqueza
        Inimigo.inimigos.append(self)

    def __str__(self):
        return f'{self.nome} | pontos de vida: {self.vida} . '
    
    def listar_inimigos():
        for i in Inimigo.inimigos:
            print(f'{i.nome} | {i.vida}')