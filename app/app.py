from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from uuid import uuid4

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tic_tac_toe.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Game(db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    board_state = db.Column(db.String, nullable=False, default="-" * 9)  # 3x3 grid 
    current_player = db.Column(db.String(1), nullable=False, default="X")
    status = db.Column(db.String, nullable=False, default="ongoing")  # could be 'ongoing', 'win', 'draw'

@app.route('/create', methods=['POST'])
def create_game():
    new_game = Game()
    db.session.add(new_game)
    db.session.commit()
    return jsonify({"gameId": new_game.id}), 200

@app.route('/move', methods=['POST'])
def make_move():
    data = request.get_json()
    game_id = data.get("gameId")
    player_id = data.get("playerId")
    x = data["square"]["x"]
    y = data["square"]["y"]

    game = Game.query.get(game_id)
    if not game:
        return abort(404, description="Game not found")

    if game.status != "ongoing":
        return abort(400, description="Game already completed")

    index = 3 * y + x
    if game.board_state[index] != "-":
        return abort(400, description="Square already taken")

    if game.current_player != player_id:
        return abort(400, description="It's not your turn")

    board = list(game.board_state)
    board[index] = player_id
    game.board_state = "".join(board)

    # Check for win or draw
    if check_win(board, player_id):
        game.status = f"{player_id} wins"
    elif "-" not in board:
        game.status = "draw"
    else:
        game.current_player = "O" if player_id == "X" else "X"

    db.session.commit()
    return jsonify({"status": game.status, "board": game.board_state}), 200

@app.route('/status', methods=['GET'])
def get_status():
    game_id = request.args.get("gameId")
    game = Game.query.get(game_id)
    if not game:
        return abort(404, description="Game not found")

    return jsonify({
        "board": game.board_state,
        "currentPlayer": game.current_player,
        "status": game.status
    }), 200

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

if __name__ == '__main__':
    app.run(debug=True)
