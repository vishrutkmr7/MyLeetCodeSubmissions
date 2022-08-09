class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hash_table = {}
        for word in words:
            if word not in hash_table:
                hash_table[word] = 0
            hash_table[word] += 1

        keys = list(hash_table.keys())
        result, considered, same_odd_set = 0, set(), set()

        for key in keys:
            if key not in considered:
                if key[0] == key[1]:
                    result += 4* (hash_table[key] // 2)
                    if hash_table[key] % 2 == 1:
                        same_odd_set.add(key)
                elif key[1] + key[0] in hash_table:
                    result += 4*min(hash_table[key], hash_table[key[1]+key[0]])
                    considered.add(key)
                    considered.add(key[1]+key[0])

        if same_odd_set:
            result += 2
        return result