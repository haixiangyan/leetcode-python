def friend_list(friendship_list):
    friends = {}

    for friendship in friendship_list:
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
    "2,4"
}
print(friend_list(friendship_list))
