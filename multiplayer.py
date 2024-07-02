from player import Player
from gamemode import GameMode
class Multiplayer(GameMode):
    """_summary_ Emulates a multiplayer gamemode

    Args:
        GameMode (_type_): the default gamemode class
    """
    def __init__(self) -> None:
        super().__init__()
        self.player1: Player = self._get_player1()
        self.player2: Player = self._get_player2()
        self.player_list.extend([self.player1, self.player2])
        
    def _get_player1(self) -> Player:
        """_summary_ Gets player 1 name and symbol

        Returns:
            Player: player 1 object
        """
        name: str = Player.get_player_name()
        
        if name == '':
            return Player("Player 1", "X")
        return Player(name, "X")
    
    def _get_player2(self) -> None:
        """_summary_ Gets player 1 name and symbol

        Returns:
            Player: player 1 object
        """
        name: str = Player.get_player_name()
        
        if name == '':
            return Player("Player 2", "O")
        return Player(name, "O")
    
    def play(self) -> tuple[bool, list[object]]:
        """_summary_ play a game of tic-tac-toe

        Returns:
            tuple[bool, list[object]]: wether or not the players want to play again and the game result
        """
        turn: int = 1
        won: bool = False
        again: bool = False
        winner: str = "draw"
        
        while turn <= 9 and not won:
            if turn % 2 != 0:
                done = self.take_turn(self.player1)
                while not done:
                    done = self.take_turn(self.player1)
            else:
                done = self.take_turn(self.player2)
                while not done:
                    done = self.take_turn(self.player2)
            turn += 1
            if self.check_board(self.player1):
                won = True
                winner = self.player1.name
            elif self.check_board(self.player2):
                won = True
                winner = self.player2.name
        if won:
            print(f'{winner} won the game')       
        else:
            print('the game ended in a draw')
        self.board.print_board()
        user_entry: str = input("Do you want to play another game (Y/N): ").upper()
        
        if user_entry[0] == 'Y':
            again = True
        return (again, [winner, turn])
    
    def run(self) -> dict[str, object]:
        """_summary_ runs the gamemode

        Returns:
            dict[str, object]: the gamelog from the game(s)
        """
        gamelog: dict[str, object] = {}
        game_num: int = 1
        run: bool = True
        while run:
            result = self.play()
            run = result[0]
            gamelog["game" + str(game_num)] = result[1]
            game_num += 1
            self.board.reset()
            self.player1, self.player2 = self.player2, self.player1
            
        return gamelog