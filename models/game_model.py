games = []
current_id = 1

class Game:
    def __init__(self, titulo, genero, desenvolvedor, plataforma):
        global current_id

        self.id = current_id
        self.titulo = titulo
        self.genero = genero
        self.desenvolvedor = desenvolvedor
        self.plataforma = plataforma

        current_id += 1

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "genero": self.genero,
            "desenvolvedor": self.desenvolvedor,
            "plataforma": self.plataforma
        }