class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        pattern_dict = {}
        s_dict = {}
        for i, v in enumerate(pattern):
            if v not in pattern_dict:
                pattern_dict[v] = s[i]
            if s[i] not in s_dict:
                s_dict[s[i]] = v
            if pattern_dict[v] != s[i] or s_dict[s[i]] != v:
                return False
        return True