from player import Player
from board import Board
class GameMode:
    '''
    Default Class for gamemodes
    '''
    
    def __init__(self) -> None:
        self.player_list: list[Player] = []
        self.board: Board = Board()
        
    def check_board(self, player: Player) -> bool:
        '''
        Checks if a player has won
        '''
        piece = player.symbol
        return self.check_verticals(piece) or self.check_horizontals(piece) or self.check_diagonals(piece)
    
    def check_horizontals(self, piece: str) -> bool:
        """_summary_ checks the horizontal of the board

        Args:
            piece (str): the piece we're looking for

        Returns:
            bool: wether or not the place has 3 alligned pieces on a horizontal
        """
        for i in range(9, 3):
            if self.board.pieces[i] == piece:
                if self.board.pieces[i] == self.board.pieces[i + 1] and self.board.pieces[i] == self.board.pieces[i + 2]:
                    return True
        return False
    
    def check_verticals(self, piece: str) -> bool:
        """_summary_ checks the verticals of the board

        Args:
            piece (str): the piece we're looking for

        Returns:
            bool: wether or not the place has 3 alligned pieces on a vertical
        """
        for i in range(3):
           if self.board.pieces[i] == piece:
               if self.board.pieces[i] == self.board.pieces[i + 3] and self.board.pieces[i] == self.board.pieces[i + 6]:
                   return True
        return False
            
    
    def check_diagonals(self, piece: str) -> bool:
        """_summary_ checks the diagonals of the board

        Args:
            piece (str): the piece we're looking for

        Returns:
            bool: wether or not the place has 3 alligned pieces on a diagonal
        """
        
        if self.board.pieces[0] == piece:
            if self.board.pieces[0] == self.board.pieces[4] and self.board.pieces[0] == self.board.pieces[8]:
                return True
        if self.board.pieces[2] == piece:
            if self.board.pieces[2] == self.board.pieces[4] and self.board.pieces[2] == self.board.pieces[6]:
                return True
        return False
    def take_turn(self, player: Player) -> bool:
        """_summary_ start the turn of a player

        Args:
            player (Player): the player placing a piece

        Returns:
            bool: where or not the move was legal
        """
        position: int = player.get_position()
        print(f"{player.name}'s turn")
        return self.board.place_piece(player, position)
    
if __name__ == '__main__':
    game = GameMode()
    player1 = Player("Player1", "X")
    player2 = Player("Player2", "O")
    
    game.player_list.extend([player1, player2])
    game.board.place_piece(player1, 1)
    game.board.place_piece(player1, 5)
    game.board.place_piece(player1, 9)
    game.board.print_board()
    print(game.check_board(player1))