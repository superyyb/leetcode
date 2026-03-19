class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        """
        1. total skill of each team needs to be the same, so we sort the skill first
         to figure out the smallest skill(skill[0]) and the largest skill(skill[-1]),
         the sum of skill[0] and skill[-1] should be the total skill of each team.
        2. Then we use two pointers to check if the sum of every pair equals the target total skill.
        """
        skill.sort()
        i, j = 0, len(skill) - 1
        target_skill = skill[0] + skill[-1]
        total = 0
        while i < j:
            if skill[i] + skill[j] != target_skill:
                return -1
            total += skill[i] * skill[j]
            i += 1
            j -= 1
        return total