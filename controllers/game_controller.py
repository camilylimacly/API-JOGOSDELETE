from models.game_model import Game, games

def create_game(data):
    game = Game(
        data["titulo"],
        data["genero"],
        data["desenvolvedor"],
        data["plataforma"]
    )

    games.append(game)

    return game.to_dict()


def get_all_games():
    return [game.to_dict() for game in games]


def get_game_by_id(game_id):
    for game in games:
        if game.id == game_id:
            return game

    return None


def update_game(game_id, data):
    game = get_game_by_id(game_id)

    if game:
        game.titulo = data.get("titulo", game.titulo)
        game.genero = data.get("genero", game.genero)
        game.desenvolvedor = data.get("desenvolvedor", game.desenvolvedor)
        game.plataforma = data.get("plataforma", game.plataforma)

        return game.to_dict()

    return None


def delete_game(game_id):
    game = get_game_by_id(game_id)

    if game:
        games.remove(game)
        return True

    return False