class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        buses = defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                buses[stop].append(i)
                
        q = [source]
        seenbus = set()
        depth = 0
        while q:
            temp = []
            for stop in q:
                if stop == target:
                    return depth
                for bus in buses[stop]:
                    if bus in seenbus:
                        continue
                    seenbus.add(bus)
                    temp += routes[bus]
            q = temp
            depth += 1
        
        return -1
        