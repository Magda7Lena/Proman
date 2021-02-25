from flask import Blueprint, render_template, url_for, redirect, request, flash, session, jsonify
board = Blueprint('board', __name__)


@board.route("/board", methods=["GET", "POST"])
def board_page():
    return render_template('board.html')



@board.route("/boards", methods=["GET", "POST"])
def route_board():
    return render_template('board-option.html')



