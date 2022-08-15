class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        array = [-1 for i in range(len(isConnected))]
        for i in range(len(array)):
            for j in range(len(array)):
                if i != j and isConnected[i][j] == 1:
                    self.union(array,i,j)
        count=0
        for i in range(len(array)):
            if array[i] == -1:
                count += 1
        return count
                    
        
        
    def find(self, array, index):
        if array[index] == -1:
            return index
        return self.find(array,array[index])

    def union(self, array, index1, index2):
        root1 = self.find(array, index1)
        root2 = self.find(array, index2)
        if root1 != root2:
            array[root2] = root1
