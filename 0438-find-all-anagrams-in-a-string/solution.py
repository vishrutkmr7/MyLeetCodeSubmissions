class Solution:
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        hashMap = defaultdict(int)
        if len(p) > len(s):
            return []
        for char in p:
            hashMap[char] += 1
        
        for i in range(len(p) - 1):
            if s[i] in hashMap:
                hashMap[s[i]] -= 1
        
        for i in range(-1, len(s) - len(p) + 1):
            if i > -1 and s[i] in hashMap:
                hashMap[s[i]] += 1
            if i + len(p) < len(s) and s[i + len(p)] in hashMap: 
                hashMap[s[i + len(p)]] -= 1
                
            if not any(hashMap.values()): 
                result.append(i + 1)
            
        return result
        
