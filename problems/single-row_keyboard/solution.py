class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        time = 0
        curr = 0
        for char in word:
            index = keyboard.index(char)
            time += abs(curr - index)
            curr = index
        return time