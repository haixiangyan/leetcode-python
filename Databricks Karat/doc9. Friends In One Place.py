from collections import deque
def friends_one_place(friendships):
    friends = get_friends(friendships)
    queue = deque(['1'])
    visited = {'1'}

    while queue:
        node = queue.popleft()
        for friend in friends[node]:
            if friend not in visited:
                queue.append(friend)
                visited.add(friend)

    return len(visited) == len(friends)

def get_friends(friendships):
    friends = {}
    for friendship in friendships:
        a, b = friendship.split(',')
        if a not in friends:
            friends[a] = set()
        if b not in friends:
            friends[b] = set()
        friends[a].add(b)
        friends[b].add(a)
    return friends

friendship_list = {
    "1,2",
    "1,3",
    "1,6",
    "2,4",
    "7,8"
}

print(friends_one_place(friendship_list))
