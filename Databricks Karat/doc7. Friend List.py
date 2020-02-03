def friend_list(friendship_list):
    result = {}
    for f in friendship_list:
        a, b = f.split(',')
        if a not in result:
            result[a] = []
        if b not in result:
            result[b] = []
        result[a].append(b)
        result[b].append(a)
    return result

friendship_list = {
    "1,2",
    "1,3",
    "1,6",
    "2,4"
}
print(friend_list(friendship_list))
