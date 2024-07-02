class Player:
    '''
    Emulates the behaviors and attributes of a player
    '''
    
    def __init__(self, name: str, symbol: str) -> None:
        self.name = name
        self.symbol = symbol         
        
    @classmethod
    def get_player_name(cls) -> str:
        """_summary_ Get the name for a player

        Returns:
            str: the name entered by the user
        """
        name = input('Enter player name (Press enter to use default name): ')
        return name       