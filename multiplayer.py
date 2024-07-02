from player import Player
from gamemode import GameMode
class Multiplayer(GameMode):
    """_summary_ Emulates a multiplayer gamemode

    Args:
        GameMode (_type_): the default gamemode class
    """
    def __init__(self) -> None:
        super().__init__()
        self.player1 = self._get_player1()
        self.player2 = self._get_player2()
        self.player_list.extend([self.player1, self.player2])
        
    def _get_player1(self) -> Player:
        """_summary_ Gets player 1 name and symbol

        Returns:
            Player: player 1 object
        """
        name = Player.get_player_name()
        
        if name == '':
            return Player("Player 1", "X")
        return Player(name, "X")
    
    def _get_player2(self) -> None:
        """_summary_ Gets player 1 name and symbol

        Returns:
            Player: player 1 object
        """
        name = Player.get_player_name()
        
        if name == '':
            return Player("Player 2", "O")
        return Player(name, "O")
    
if __name__ == '__main__':
    game = Multiplayer()
    
    game.board.place_piece(game.player1, 1)
    game.board.place_piece(game.player1, 5)
    game.board.place_piece(game.player1, 9)
    game.board.print_board()
    print(game.check_board(game.player1))