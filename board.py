class Board:
    '''
    implements the behaviors and attributes of a Board
    '''
    
    def __init__(self) -> None:
        self.pieces = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
    def reset(self) -> None:
        '''
        Resets the board
        '''
        for i in range(len(self.pieces)):
            self.pieces[i] = str(i + 1)
        
    def print_board(self) -> None:
        '''
        Prints the board
        '''
        self.print_board_separator()
        i = 1
        for piece in self.pieces:
            print(f'| {piece}', end=' ')
            if i % 3 == 0 and i > 1:
                print("|")
                self.print_board_separator()
            
            i += 1

    def print_board_separator(self) -> None:
        '''
        Helper method that prints the horizontal lines for the print board method
        '''  
        print("+---+---+---+")
        
    def check_piece(self, position: int) -> bool:
        if self.pieces[position - 1] == 'X' or self.pieces[position - 1] == 'O':
            return False
        return True
    


if __name__ == '__main__':
    board = Board()
    board.print_board()
    
    
    