class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = len)
        check = strs[0]
        
        for i in range(1, len(strs)):
            flag = True
            
            while flag:
                if check in strs[i][:len(check)]:
                    flag = False
                elif len(check) == 0:
                    flag = False
                else:
                    check = check[: len(check) - 1]
            if len(check) == 0:
                break
        return check
        
