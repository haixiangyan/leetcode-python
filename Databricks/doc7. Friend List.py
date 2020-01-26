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
print(friend_list(friendship_list))
