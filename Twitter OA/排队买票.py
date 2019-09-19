from collections import deque

def solution(tickets, p):
    if not tickets:
        return 0
    queue = deque([])
    myTicket, count = tickets[p], 0 if p == 0 else 1
    position = p
    n = len(tickets)

    for ticket in tickets:
        queue.append(ticket)

    while myTicket != 0:
        count += 1

        ticket = queue.popleft()
        ticket -= 1

        if ticket > 0:
            queue.append(ticket)

        if position == 0:
            myTicket -= 1
            position = n - 1

        position = position - 1

    return count
