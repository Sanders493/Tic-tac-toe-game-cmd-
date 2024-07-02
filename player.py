class Player:
    '''
    Emulates the behaviors and attributes of a player
    '''
    
    def __init__(self, name: str, symbol: str) -> None:
        self.name: str = name
        self.symbol: str = symbol         
        
    @classmethod
    def get_player_name(cls) -> str:
        """_summary_ Get the name for a player

        Returns:
            str: the name entered by the user
        """
        name = input('Enter player name (Press enter to use default name): ')
        return name

    def get_position(self) -> int:
        """_summary_ get the position where the player wants to place a piece

        Returns:
            int: the position
        """
        
        position: int = -1
        done: bool = False
        while not done:
            user_input: str = input("Enter the position to place a piece: ")
            
            if user_input.isnumeric():
                position = int(user_input)
                if position > 9 or position < 1:
                    print("Error: Enter a position between 1 and 9")
                else:
                    done = True
        return position