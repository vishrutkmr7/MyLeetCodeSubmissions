class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        rank = {}
        for x, y in stones:
            self.set_param(x, parent, rank)
            self.set_param(~y, parent, rank)
            self.union(x, ~y, parent, rank)

        root = {self.find(value, parent) for value in parent.values()}
        return len(stones) - len(root)
        
    def set_param(self, x, parent, rank):
        if(x not in parent):
            parent[x] = x
            rank[x] = 0

    def find(self, x, parent):
        if(x != parent[x]):
            parent[x] = self.find(parent[x], parent)
        return parent[x]
    
    def union(self, x, y, parent, rank):
        parent_x = self.find(x, parent)
        parent_y = self.find(y, parent)
        
        if(parent_x == parent_y):
            return
        rank_x = rank[parent_x]
        rank_y = rank[parent_y]
        
        if(rank_x > rank_y):
            parent[parent_y] = parent_x
        elif(rank_x < rank_y):
            parent[parent_x] = parent_y
        else:
            parent[parent_y] = parent_x
            rank[parent_x] += 1