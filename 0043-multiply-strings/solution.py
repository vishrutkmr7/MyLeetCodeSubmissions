class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0] * (len(num1) + len(num2))
        
        for j in range(len(num2)-1, -1, -1):
            carry = 0
            pos = 0
            for i in range(len(num1)-1, -1, -1):
                pos = i + j + 1
                temp_prod = res[i + j + 1] + int(num2[j]) * int(num1[i]) + carry
                
                res[i + j + 1] = temp_prod % 10
                carry = temp_prod // 10
            if carry:
                res[pos - 1] = carry
        ans = ''

        if res[0] == 0:
            del res[0]
        ans = ''.join(str(num) for num in res)
        return ans
