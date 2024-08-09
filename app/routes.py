from flask import request, jsonify, abort, render_template
from app import db
from app.models import Game

def register_routes(app):
    @app.route('/')
    def index():
        print('Request for index page received')
        return render_template('index.html')

    @app.route('/create', methods=['POST'])
    def create_game():
        new_game = Game()
        db.session.add(new_game)
        app.logger.info(f"New game created with id {new_game.id}")
        db.session.commit()
        return jsonify({"gameId": new_game.id}), 200
        

    @app.route('/move', methods=['POST'])
    def make_move():
        try:
            data = request.get_json()
            app.logger.info(f"Received move request: {data}")
            game_id = data.get("gameId")
            player_id = data.get("playerId")
            x = int(data["square"]["x"])  # Ensure x is an integer
            y = int(data["square"]["y"])  # Ensure y is an integer

            game = Game.query.get(game_id)
            if not game:
                return jsonify({"error": "Game not found"}), 404

            if game.status != "ongoing":
                return jsonify({"error": "Game already completed"}), 400

            index = 3 * y + x
            if game.board_state[index] != "-":
                return jsonify({"error": "Square already taken"}), 400

            if game.current_player != player_id:
                return jsonify({"error": "It's not your turn"}), 400

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
            app.logger.info(f"Move successful. Game status: {game.status}")
            return jsonify({"status": game.status, "board": game.board_state}), 200
        except Exception as e:
            app.logger.error(f"Error making move: {e}")
            return jsonify({"error": str(e)}), 500


    @app.route('/status', methods=['GET'])
    def get_status():
        game_id = request.args.get("gameId")
        game = Game.query.get(game_id)
        if not game:
            app.logger.error(f"Game with id {game_id} not found")
            return abort(404, description="Game not found")
        
        app.logger.info(f"Game status requested. Game status")
        return jsonify({
            "board": game.board_state,
            "currentPlayer": game.current_player,
            "status": game.status
        }), 200

    def check_win(board, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for condition in win_conditions:
            if all(board[i] == player for i in condition):
                app.logger.info(f"Player {player} wins with {condition}")
                return True
        app.logger.info(f"Player {player} does not win")
        return False

