def get_depart_stat(employees, friendships):
    friends = get_friends(friendships)

    departments = {}
    results = {}
    persons = {}

    for employee in employees:
        id, name, depart = employee.split(',')

        persons[id] = depart

        if depart not in departments:
            departments[depart] = set()
        if depart not in results:
            results[depart] = [0, 0]

        departments[depart].add(id)

    for depart in departments:
        results[depart][0] = len(departments[depart])

        for employee in departments[depart]:
            if employee not in friends:
                continue
            for friend in friends[employee]:
                if persons[friend] != depart:
                    results[depart][1] += 1
                    break
    return results


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


employees = {
    "1,Richard,Engineering",
    "2,Erlich,HR",
    "3,Monica,Business",
    "4,Dinesh,Engineering",
    "6,Carla,Engineering",
    "9,Laurie,Directors"
}

friendships = {
    "1,2",
    "1,3",
    "1,6",
    "2,4"
}

print(get_depart_stat(employees, friendships))


def get_depart_stat(employees, friendships):
    friend_list = get_friend_list(friendships)

    departments = {}
    results = {}
    persons = {}

    for employee in employees:
        id, name, depart = employee.split(',')

        if depart not in departments:
            departments[depart] = set()
        departments[depart].add(id)

        if id not in persons:
            persons[id] = depart

        if depart not in results:
            results[depart] = [0, 0]

    for depart in results:
        results[depart][0] = len(departments[depart])

        for eid in departments[depart]:
            if eid not in friend_list:
                continue
            for friend in friend_list[eid]:
                if persons[friend] != depart:
                    results[depart][1] += 1
                    break
    return results

def get_friend_list(friendships):
    friend_list = {}
    for fs in friendships:
        a, b = fs.split(',')
        if a not in friend_list:
            friend_list[a] = []
        if b not in friend_list:
            friend_list[b] = []

        friend_list[a].append(b)
        friend_list[b].append(a)
    return friend_list

employees = {
    "1,Richard,Engineering",
    "2,Erlich,HR",
    "3,Monica,Business",
    "4,Dinesh,Engineering",
    "6,Carla,Engineering",
    "9,Laurie,Directors"
}

friendships = {
    "1,2",
    "1,3",
    "1,6",
    "2,4"
}

print(get_depart_stat(employees, friendships))
