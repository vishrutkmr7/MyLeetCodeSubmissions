class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            return len(s) - len(set(s)) >= 1

        diff = []
        for index, char in enumerate(s):
            if char != goal[index]:
                diff.append(index)
                if len(diff) > 2:
                    return False

        if len(diff) != 2:
            return False

        # check swaps
        if s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]:
            return True

        return False