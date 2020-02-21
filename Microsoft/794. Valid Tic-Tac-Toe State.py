class Solution:
    def validTicTacToe(self, board) -> bool:
        x_num, o_num = 0, 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    x_num += 1
                elif board[i][j] == 'O':
                    o_num += 1

        if o_num > x_num or x_num - o_num > 1:
            return False

        if self.check_win(board, 'O'):
            if self.check_win(board, 'X'):
                return False

            return o_num == x_num

        if self.check_win(board, 'X'):
            if self.check_win(board, 'O'):
                return False

            return x_num - 1 == o_num

        return True

    def check_win(self, board, player):
        # Row
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True

        # Col
        for i in range(len(board)):
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True

        # Diagonal
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False
