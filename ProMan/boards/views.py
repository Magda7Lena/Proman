from flask import render_template, request, Blueprint, jsonify, Response
from ProMan import data_manager


boards = Blueprint('boards', __name__)
cards =Blueprint('cards', __name__)

@boards.route("/api/user/<int:user_id>/boards", methods=['GET'])
def api_get_boards(user_id:int) -> Response:
    resp = data_manager.get_boards(user_id)
    return jsonify(resp)


@boards.route("/api/user/<int:user_id>/boards", methods=['POST'])
def api_add_board(user_id: int) -> Response:
    print(type(user_id))
    new_board = request.get_json()
    resp = data_manager.add_new_board(new_board, user_id)
    return jsonify(resp)


@boards.route("/api/user/<int:user_id>/boards/<int:board_id>", methods=["DELETE"])
def api_delete_board(user_id:int, board_id: int) -> Response:
    owner_id = data_manager.get_board_owner_id(board_id)
    if owner_id == user_id:
        resp = data_manager.delete_board(board_id)
        return jsonify(resp)
    return jsonify('unauthorized')



@boards.route("/board/<int:board_id>", methods=["GET", "POST"])
def route_board(board_id:int):
    return render_template('board.html')

@boards.route("/api/get-cards/<board_id>", methods=['GET'])
def api_get_cards(board_id):
    cards = data_manager.get_cards(board_id)
    return cards


@boards.route("/api/get-columns/<board_id>", methods=['GET'])
def api_get_columns(board_id):
    columns = data_manager.get_columns(board_id)
    return columns


