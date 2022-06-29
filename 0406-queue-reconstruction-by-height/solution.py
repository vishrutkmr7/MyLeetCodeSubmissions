class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        output = []
        people.sort(key=lambda x: (-x[0], x[1]))
        for peep in people:
            output.insert(peep[1], peep)
        return output
        
