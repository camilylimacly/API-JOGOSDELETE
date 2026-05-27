from flask import Blueprint, request, jsonify
from controllers.game_controller import *

game_routes = Blueprint('game_routes', __name__)


@game_routes.route('/games', methods=['POST'])
def create():
    data = request.json

    return jsonify(create_game(data)), 201


@game_routes.route('/games', methods=['GET'])
def get_all():
    return jsonify(get_all_games())


@game_routes.route('/games/<int:id>', methods=['GET'])
def get_by_id(id):
    game = get_game_by_id(id)

    if game:
        return jsonify(game.to_dict())

    return jsonify({"erro": "Jogo não encontrado"}), 404


@game_routes.route('/games/<int:id>', methods=['PUT'])
def update(id):
    data = request.json

    game = update_game(id, data)

    if game:
        return jsonify(game)

    return jsonify({"erro": "Jogo não encontrado"}), 404


@game_routes.route('/games/<int:id>', methods=['DELETE'])
def delete(id):

    if delete_game(id):
        return jsonify({"mensagem": "Jogo removido com sucesso"})

    return jsonify({"erro": "Jogo não encontrado"}), 404