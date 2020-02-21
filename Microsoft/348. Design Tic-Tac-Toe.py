class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.size = n

    def move(self, row: int, col: int, player: int):
        if self.board[row][col] == 0:
            self.board[row][col] = player

        # left -> right
        for i in range(self.size):
            if self.board[row][i] != player:
                break
            if i == self.size - 1:
                return player

        # top -> bottom
        for i in range(self.size):
            if self.board[i][col] != player:
                break
            if i == self.size - 1:
                return player

        # top left -> bottom right
        for i in range(self.size):
            if self.board[i][i] != player:
                break
            if i == self.size - 1:
                return player

        # top right -> bottom left
        for i in range(self.size):
            if self.board[i][self.size - i - 1] != player:
                break
            if i == self.size - 1:
                return player

        return 0
