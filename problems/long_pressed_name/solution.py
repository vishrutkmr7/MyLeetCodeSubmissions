class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for index, value in enumerate(typed):
            if i < len(name) and name[i] == value:
                i += 1
            elif index == 0 or value != typed[index - 1]:
                return False
        return i == len(name)