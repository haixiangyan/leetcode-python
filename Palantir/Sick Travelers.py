class Person:
    def __init__(self, name, state, cities):
        self.name = name
        self.state = state
        self.cities = cities
        self.curtCity = -1
        self.cityNum = len(cities)
        self.trackState = [state]

    def visitNextCity(self):
        self.curtCity = (self.curtCity + 1) % self.cityNum

    def __str__(self):
        return '{name: ' + self.name + ', state: ' + self.state + ', cities: ' + str(self.cities) + '}'


SICK = 'SICK'
HEALTHY = 'HEALTHY'
RECOVERING = 'RECOVERING'


def traceDisease(data):
    cityStates = {}
    people, healthyNum = parsePeople(data)
    n = len(people)
    days = 1

    while healthyNum != n and days <= 365:
        cityPeople = {}
        for person in people:
            # Visit next city
            person.visitNextCity()

            city = person.cities[person.curtCity]

            # Markdown this person
            if city not in cityPeople:
                cityPeople[city] = []
            cityPeople[city].append(person)

            # Update city state
            if city not in cityStates or len(cityPeople[city]) == 1:
                cityStates[city] = HEALTHY
            if days == 1:
                cityStates[city] = updateCityState(cityStates[city], person.state)
            else:
                cityStates[city] = updateCityState(cityStates[city], growState(person.state))

        # Update people state
        for city in cityPeople:
            while cityPeople[city]:
                curtPerson = cityPeople[city].pop()
                prevState = curtPerson.state
                if days == 1:
                    curtPerson.state = updatePeopleState(cityStates[city], curtPerson.state)
                else:
                    curtPerson.state = updatePeopleState(cityStates[city], growState(curtPerson.state))
                curtPerson.trackState.append(curtPerson.state)

                if prevState == HEALTHY and curtPerson.state != HEALTHY:
                    healthyNum -= 1
                if prevState != HEALTHY and curtPerson.state == HEALTHY:
                    healthyNum += 1
        days += 1
    results = []
    names = []
    for p in people:
        names.append(p.name)
    results.append(' '.join(names))
    for i in range(len(people[0].trackState)):
        curt_states = []
        for p in people:
            curt_states.append(p.trackState[i])
        results.append(' '.join(curt_states))

    results.append(str(days - 1 if days != 1 else 1))

    return results


# Parse input data
def parsePeople(people):
    results = []
    healthyNum = 0
    for person in people:
        data = person.split(' ')
        name = data[0]
        state = data[1]
        if state == HEALTHY:
            healthyNum += 1
        cities = data[2:]

        results.append(Person(name, state, cities))
    return results, healthyNum


# Union states
def updateCityState(curtState, newState):
    if (curtState == SICK or curtState == RECOVERING) and newState == HEALTHY:
        return SICK
    if (newState == SICK or newState == RECOVERING) and curtState == HEALTHY:
        return SICK
    if curtState == HEALTHY and newState == HEALTHY:
        return HEALTHY
    return RECOVERING


def updatePeopleState(cityState, peopleState):
    if (cityState == SICK or cityState == RECOVERING) and peopleState == HEALTHY:
        return SICK
    return peopleState


# Grow state
def growState(curtState):
    if curtState == SICK:
        return RECOVERING
    if curtState == RECOVERING:
        return HEALTHY
    return curtState


data = [
    'Isabella RECOVERING DC',
    'Jamal HEALTHY PaloAlto',
]

print(traceDisease(data))
