from player import Player
from board import Board
class GameMode:
    '''
    Default Class for gamemodes
    '''
    
    def __init__(self) -> None:
        player_list: list[Player] = []
        board: Board = Board()