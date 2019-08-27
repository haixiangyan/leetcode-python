class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid):
        mp = obstacleGrid
        for i in range(len(mp)):
            for j in range(len(mp[i])):
                if i == 0 and j == 0:
                    mp[i][j] = 1 - mp[i][j]
                elif i == 0:
                    if mp[i][j] == 1:
                        mp[i][j] = 0
                    else:
                        mp[i][j] = mp[i][j - 1]
                elif j == 0:
                    if mp[i][j] == 1:
                        mp[i][j] = 0
                    else:
                        mp[i][j] = mp[i - 1][j]
                else:
                    if mp[i][j] == 1:
                        mp[i][j] = 0
                    else:
                        mp[i][j] = mp[i - 1][j] + mp[i][j - 1]
        if mp[-1][-1] > 2147483647:
            return -1
        else:
            return mp[-1][-1]