class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        n = len(tops)
        for x in range(1, 7):
            top_count = 0
            bottom_count = 0
            for i in range(n):
                if tops[i] != x and bottoms[i] != x:
                    break
                elif tops[i] != x:
                    top_count += 1
                elif bottoms[i] != x:
                    bottom_count += 1
            else:
                return min(top_count, bottom_count)
        return -1