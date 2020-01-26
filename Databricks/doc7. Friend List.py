# 1st Question: 输出所有的employee的friendlist -> 就是用一个map存起来然后打印就好了（这个是无向图，e.g: 1和2是朋友，2的列表里也要有1）
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
