class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {list1[i]: i for i in range(len(list1))}
        dict2 = {list2[i]: i for i in range(len(list2))}
        min_sum = float("inf")
        for key in dict1:
            if key in dict2:
                min_sum = min(min_sum, dict1[key] + dict2[key])
        return [
            key
            for key, value in dict1.items()
            if key in dict2 and value + dict2[key] == min_sum
        ]