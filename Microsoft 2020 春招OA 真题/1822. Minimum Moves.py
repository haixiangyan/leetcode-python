class Solution:
    """
    @param S: a string
    @return:  return the minimum number of moves
    """
    def MinimumMoves(self, S):
        a, moves, offset = 'a', 0, 0

        for char in S:
            if char == a:
                offset += 1
                if offset == 3:
                    moves += 1
                    offset = 0
            else:
                a, offset = char, 1
        return moves
