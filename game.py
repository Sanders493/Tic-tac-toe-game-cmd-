def display_how_to_play() -> None:
    '''
    Displays the game instructions
    '''
    try:
        with open('HowToPlay.txt', 'r') as file:
            for line in file.readline():
                print(line)
    except FileNotFoundError:
        print('HowToPlay file missing')
    except Exception as e:
        print(e)

def welcome_message() -> None:
    '''
    Welcomes the user and prints patch notes
    '''
    print('Welcome to tic-tac-toe game by Sanders')
    print('patch 1.0.0\n')
 
def farewell_message() -> None:
    '''
    Prints farewell message
    '''  
    print('\nThank you trying this game')
    print('More by Sanders at https://github.com/users/Sanders493')
    
def run_game() -> None:
    '''
    Runs the game until the user enters exit
    '''
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
                pass
            case 'exit' | 'e':
                run = False
            case _:
                continue