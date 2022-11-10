class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        array = [-1 for _ in range(len(isConnected))]
        for i in range(len(array)):
            for j in range(len(array)):
                if i != j and isConnected[i][j] == 1:
                    self.union(array,i,j)
        return sum(array[i] == -1 for i in range(len(array)))
                    
        
        
    def find(self, array, index):
        return index if array[index] == -1 else self.find(array,array[index])

    def union(self, array, index1, index2):
        root1 = self.find(array, index1)
        root2 = self.find(array, index2)
        if root1 != root2:
            array[root2] = root1