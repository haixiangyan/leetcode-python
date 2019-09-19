import re
import functools
def solution(team1, team2, event1, event2):
    eventNames = ['G', 'Y', 'R', 'S']
    def compare(a, b):
        metaA, metaB = a.split(' '), b.split(' ')

        timeALike = re.findall('\d+\+?\d*', a)[0]
        timeBLike = re.findall('\d+\+?\d*', b)[0]
        timeA = int(timeALike) if timeALike.find('+') < 0 else int(timeALike.split('+')[0])
        timeB = int(timeBLike) if timeBLike.find('+') < 0 else int(timeBLike.split('+')[0])
        eventA, eventB = metaA[-1], metaB[-1]

        if timeA == timeB and eventA == eventB:
            return 0

        if timeA != timeB:
            return 1 if timeA > timeB else -1
        else:
            return 1 if eventNames.index(eventA) > eventNames.index(eventB) else -1

    results = []
    event1, event2 = sorted(event1, key=functools.cmp_to_key(compare)), sorted(event2, key=functools.cmp_to_key(compare))
    index1, index2 = 0, 0
    while index1 < len(event1) and index2 < len(event2):
        compareResult = compare(event1[index1], event2[index2])
        if compareResult == 1:
            results.append(team2 + ' ' + event2[index2])
            index2 += 1
        elif compareResult == -1:
            results.append(team1 + ' ' + event1[index1])
            index1 += 1
        else:
            if team1 < team2:
                results.append(team1 + ' ' + event1[index1])
                index1 += 1
            else:
                results.append(team2 + ' ' + event2[index2])
                index2 += 1

    while index1 < len(event1):
        results.append(team1 + ' ' + event1[index1])
        index1 += 1
    while index2 < len(event2):
        results.append(team2 + ' ' + event2[index2])
        index2 += 1

    return results

team1 = "ABC"
team2 = "CBA"
event1 = ["Mo Sa 45+2 Y", "A 13 G"]
event2 = ["D 23 S F", "Z 46 G"]
print(solution(team1, team2, event1, event2))
