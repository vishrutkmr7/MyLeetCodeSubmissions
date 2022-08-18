class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        totalLen = len(arr)
        targetLen = totalLen // 2
        count = 0
        hashMap = Counter(arr).most_common()
        for x in hashMap:
            totalLen -= x[1]
            count += 1
            if totalLen <= targetLen:
                break

        return count
