from app import db
from uuid import uuid4

class Game(db.Model):
    """ Game model """
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4())) # UUID as primary key
    board_state = db.Column(db.String, nullable=False, default="-" * 9)  # 3x3 grid represented as a string
    current_player = db.Column(db.String(1), nullable=False, default="X") # 'X' or 'O'
    status = db.Column(db.String, nullable=False, default="ongoing")  #'ongoing', 'win' or 'draw'
