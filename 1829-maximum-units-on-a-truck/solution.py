class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        
        maxUnits = 0
        # Greedy
        for numberOfBoxes, unitsPerBox in boxTypes:
            numBoxes = min(truckSize, numberOfBoxes)
            maxUnits += numBoxes * unitsPerBox
            truckSize -= numBoxes
        return maxUnits
            
