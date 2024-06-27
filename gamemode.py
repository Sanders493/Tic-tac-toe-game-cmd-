from player import Player
from board import Board
class GameMode:
    '''
    Default Class for gamemodes
    '''
    
    def __init__(self) -> None:
        self.player_list: list[Player] = []
        self.board: Board = Board()
        
    def checkBoard(self, player: Player) -> bool:
        '''
        Checks if a player has won
        '''
        pass
    def checkHorizontals(self) -> bool:
        '''
        Checks the horizontals of the board
        '''
        for i in range(9, 3):
            if self.board.pieces[i] == self.board.pieces[i + 1] == self.board.pieces[i + 2]:
                return True
        return False
    
    def checkVerticals(self) -> bool:
        '''
        Checks the verticals of the board
        '''
       # for i in range(9, 3):
            
    
    def checkDiagonals() -> bool:
        pass