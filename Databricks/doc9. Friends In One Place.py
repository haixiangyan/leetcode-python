# 3rd Question: 输出是否所有employee都在一个社交圈 -> 我当时想的就是随便找一个点，用DFS遍历一遍，如果所有点都被遍历到就return true
from collections import deque


def friends_one_place(friendship_list):
    friends = friend_list(friendship_list)
    counts = 0

    queue = deque(['1'])
    visited = {'1'}

    while queue:
        curt = queue.popleft()
        counts += 1

        for friend in friends[curt]:
            if friend not in visited:
                queue.append(friend)
                visited.add(friend)

    return len(friends) == counts

def friend_list(friendship_list):
    graph = {}
    for friendship in friendship_list:
        a, b = friendship.split(',')

        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        if b not in graph:
            graph[b] = []
        graph[b].append(a)
    return graph

friendship_list = {
    "1,2",
    "1,3",
    "1,6",
    "2,4"
}

print(friends_one_place(friendship_list))