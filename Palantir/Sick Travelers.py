class Person:
    def __init__(self, name, state, cities):
        self.name = name
        self.state = state
        self.cities = cities
        self.curtCity = -1
        self.cityNum = len(cities)

    def visitNextCity(self):
        self.curtCity = (self.curtCity + 1) % self.cityNum

    def __str__(self):
        return '{name: ' + self.name + ', state: ' + self.state + ', cities: ' + str(self.cities) + '}'


def solve(data):
    cityStates = {}
    people = parsePeople(data)

    for _ in range(99):
        cityPeople = {}
        for person in people:
            # Visit next city
            person.visitNextCity()

            # Update city state
            city = person.cities[person.curtCity]
            if city not in cityStates:
                cityStates[city] = 'healthy'
            cityStates[city] = updateCityState(cityStates[city], growState(person.state))

            # Markdown this person
            if city not in cityPeople:
                cityPeople[city] = []
            cityPeople[city].append(person)

        # Update people state
        for city in cityPeople:
            while cityPeople[city]:
                curtPerson = cityPeople[city].pop()
                curtPerson.state = updatePeopleState(cityStates[city], growState(curtPerson.state))
    # All people
    for p in people:
        print(p)
    return cityStates


# Parse input data
def parsePeople(people):
    results = []
    for person in people:
        data = person.split(' ')
        name = data[0]
        state = data[1]
        cities = data[2].split('-')

        results.append(Person(name, state, cities))
    return results


# Union states
def updateCityState(curtState, newState):
    if (curtState == 'sick' or curtState == 'recovering') and newState == 'healthy':
        return 'sick'
    if (newState == 'sick' or newState == 'recovering') and curtState == 'healthy':
        return 'sick'
    if curtState == 'healthy' and newState == 'healthy':
        return 'healthy'
    return 'recovering'

def updatePeopleState(cityState, peopleState):
    if (cityState == 'sick' or cityState == 'recovering') and peopleState == 'healthy':
        return 'sick'
    return peopleState

# Grow state
def growState(curtState):
    if curtState == 'sick':
        return 'recovering'
    if curtState == 'recovering':
        return 'healthy'
    return curtState


data = [
    'Pat sick XPU-JBK-TNU-BEN-HEM-ZJY-IMY-WFA-PPT',
    'Xan sick KSB-TRV-XPU-JBK-TNU-BEN-HEM-IMY-WFA-NND',
    'Mel sick KSB-TRV-XPU-TNU-BEN-HEM-ZJY-IMY-WFA-PPT-NND',
    'Nick healthy KSB-TRV-JBK-HEM-IMY-WFA',
    'Alf recovering KSB-TRV-XPU-JBK-TNU-BEN-IMY-WFA-NND',
    'Tim healthy TRV-XPU-TNU-HEM-ZJY-PPT-NND',
    'Irv recovering KSB-TRV-XPU-JBK-BEN-HEM-ZJY-IMY-PPT',
    'Andy recovering XPU-JBK-TNU-BEN-HEM-ZJY-IMY-PPT-NND',
]

print(solve(data))
