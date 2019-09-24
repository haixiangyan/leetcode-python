def maxShared(friends_nodes, friends_from, friends_to, friends_weight):
    store = {}

    for i in range(len(friends_from)):
        if (friends_from[i], friends_to[i]) not in store:
            store[(friends_from[i], friends_to[i])] = {
                'weight': 0,
                'interest': set()
            }
        store[(friends_from[i], friends_to[i])]['interest'].add(friends_weight[i])

    maxInterest = 0
    for edge in store:
        if len(store[edge]['interest']) > maxInterest:
            maxInterest = len(store[edge]['interest'])
    product = 0
    for edge in store:
        if len(store[edge]['interest']) == maxInterest:
            f, t = edge
            product = max(product, int(f) * int(t))

    return product

friends_nodes = 4
friends_from = [1, 1, 2, 2, 2]
friends_to = [2, 2, 3, 3, 4]
friends_weight = [1, 2, 1, 3, 3]
print(maxShared(friends_nodes, friends_from, friends_to, friends_weight))