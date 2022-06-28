class Solution:
    def freqDict(self, string):
        # Create a dictionary to store the frequency of each character
        freq = {}
        for char in string:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        return freq

    def minDeletions(self, string: str) -> int:
        freq = self.freqDict(string)
        numList = sorted(list(freq.values()))
        count = 0
        while len(numList) > 0:
            top = numList[-1]
            del numList[-1]
            if len(numList) == 0:
                return count
            if numList[-1] == top:
                if top > 1:
                    numList.append(top - 1)
                count += 1
            numList = sorted(numList)
            
        return count
        
