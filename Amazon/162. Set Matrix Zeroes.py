class Solution:
    """
    @param matrix: A lsit of lists of integers
    @return: nothing
    """
    def setZeroes(self, matrix):
        if not matrix:
            return matrix
        
        rowNum = len(matrix)
        colNum = len(matrix[0])

        rows = [False for _ in range(rowNum)]
        cols = [False for _ in range(colNum)]

        for i in range(rowNum):
            for j in range(colNum):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        
        for i in range(rowNum):
            for j in range(colNum):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
        
        return matrix
