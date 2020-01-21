import math

class Solution:
    def teamFormation2(self, skills, k, lowerbound, upperbound):
        skills = self.filter_skills(skills, lowerbound, upperbound)

        n = len(skills)
        total = k
        formations = 0

        while total <= n:
            formations += math.factorial(n) / (math.factorial(total) * math.factorial(n - total))

        return formations

    def filter_skills(self, skills, lowernbound, upperbound):
        valid_skills = []

        for skill in skills:
            if lowernbound <= skill <= upperbound:
                valid_skills.append(skill)

        return valid_skills