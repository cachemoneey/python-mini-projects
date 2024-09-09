from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
    self.board = [' ' for _ in range(9)] # we will use a single list to rep 3x3 board
    self.current_winner = None #Keep track of winner

    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(selfself, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # 3 in a row wins
        # rows
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        # colums
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range (3)]:
            return True

        # diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [o, 4, 8]]
            if all{[spot == letter for spot in diagonal1]}:
                return True
            if all{[spot == letter for spot in diagonal1]}:
                return True
            return False



    def play(game, x_player, o_player, print_game=True)
        # returns winner of game! or none for tie
        if print_game:
            game.print_board_nums()

        letter = 'X'

        while game.empty_squares():
            # get the move from player
            if letter == 'O':
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)

            if game.make_move(square, letter):
                if print_game:
                    print(letter + f' amkes a move to square {square}')
                    game.print_board()
                    print('')

                if game.current_winner:
                    if print_game:
                        print(letter + ' wins!')
                    return letter

                letter = 'O' if letter == 'X' else 'X'

            if print_game:
                print("It's  tie!")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)




