class Solution:
    def differentTeams(self, skills):
        if not skills or len(skills) % 5 != 0:
            return 0

        skill_to_count = {}

        # Count skills
        for skill in skills:
            if skill not in skill_to_count:
                skill_to_count[skill] = 0
            skill_to_count[skill] = skill_to_count[skill] + 1

        # Not enough skills
        if len(skill_to_count) < 5:
            return 0

        # The number team should be depend on the minimum count of skills
        min_count = float('inf')
        for skill in skill_to_count:
            min_count = min(min_count, skill_to_count[skill])

        return min_count

s = Solution()
skills = 'pcmbzpcmbz'
print(s.differentTeams(skills))
