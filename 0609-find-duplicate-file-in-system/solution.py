from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        dic = defaultdict(lambda: [])
        for path in paths:
            lst = path.split(" ")
            for j in range(1, len(lst)):
                sp = lst[j].index("(")
                dic[lst[j][sp:]].append(f"{lst[0]}/{lst[j][:sp]}")
        return [dic[i] for i in dic if len(dic[i]) > 1]
