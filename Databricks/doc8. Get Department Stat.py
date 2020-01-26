def get_depart_stat(employees, friendships):
    friends = get_friends(friendships)
    persons = {}
    departments = {}
    results = {}

    for employee in employees:
        id, name, depart = employee.split(',')

        # Get Person
        persons[id] = depart

        # Get department
        if depart not in departments:
            departments[depart] = []
        departments[depart].append(id)

        # Init results
        results[depart] = [0, 0]

    for depart in results.keys():
        # Number of people in this department
        results[depart][0] = len(departments[depart])
        # Get all employees
        for id in departments[depart]:
            if id not in friends:
                continue
            # Get their friends
            for friend in friends[id]:
                # Check if in the same department
                if persons[friend] != depart:
                    results[depart][1] += 1
    return results


def get_friends(friendship_list):
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
