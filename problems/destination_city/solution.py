class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = {flight[0] for flight in paths}
        for flight in paths:
            if flight[1] not in cities:
                return flight[1]