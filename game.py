def display_how_to_play() -> None:
    '''
    Displays the game instructions
    '''
    display = True
    
    while display:
        print('How To Play')
        print('-------------')
        try:
            with open('HowToPlay.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    print(line)
        except FileNotFoundError:
            print('HowToPlay file missing')
        except Exception as e:
            print(e)
            
        user_entry = input('Press Enter to go back to the main menu')
        display = False
        clear_console()

def clear_console() -> None:
    '''
    Clears the console
    '''
    print("\033[H\033[2J");  
      

def welcome_message() -> None:
    """_summary_ Welcomes the user and prints patch notes
    """
    print('Welcome to tic-tac-toe game by Sanders')
    print('patch 1.0.0\n')
 
def farewell_message() -> None:
    """_summary_ Prints farewell message
    """
    print('\nThank you trying this game')
    print('More by Sanders at https://github.com/users/Sanders493')
    
def run_game() -> None:
    """_summary_ Runs the game until the user enters exit
    """
    run = True
    while run:
        user_entry = input('Select an option by typing the name: \n\n- Multiplayer\n- Singleplayer\n- How to play\n- Exit\n')
        user_entry.lower()
        
        match user_entry:
            case 'multiplayer' | 'm':
                pass
            case 'singleplayer' | 's':
                pass
            case 'how to play' | 'h':
                display_how_to_play()
            case 'exit' | 'e':
                run = False
            case _:
                continue
        clear_console()