class Solution:
    def reorganizeString(self, s: str) -> str:
        maps = Counter(s)
        li = [[-val, key] for key, val in maps.items()]
        heapq.heapify(li)
        prev = None
        res = ""

        while li or prev:
            if prev and not li:
                return ""
            cnt, char = heapq.heappop(li)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(li, prev)
                prev = None

            if cnt:
                prev = [cnt, char]

        return res
