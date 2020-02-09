class Solution:
    """
    @param rooms: a list of keys rooms[i]
    @return: can you enter every room
    """
    def canVisitAllRooms(self, rooms):
        visited = set()

        self.dfs(rooms, 0, visited)

        return len(visited) == len(rooms)

    def dfs(self, rooms, index, visited):
        for key in rooms[index]:
            if key in visited:
                continue
            visited.add(key)
            self.dfs(rooms, key, visited)
