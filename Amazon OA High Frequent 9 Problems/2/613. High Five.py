import heapq

class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score

class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, records):
        store = {}
        results = {}

        for record in records:
            if record.id not in store:
                store[record.id] = []
            heapq.heappush(store[record.id], -record.score)

        for id in store:
            idSum = 0
            for _ in range(5):
                idSum += -heapq.heappop(store[id])
            results[id] = idSum / 5

        return results
