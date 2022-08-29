class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        count_dic = {}
        num_answers = len(answers)
        for i in range(num_answers):
            if answers[i] not in count_dic:
                count_dic[answers[i]] = 1
            else:
                count_dic[answers[i]] += 1
        res = 0
        for key, val in count_dic.items():
            if key == 0:
                res += val
            elif val <= key + 1:
                res += key + 1
            elif val % (key + 1) == 0:
                res += val // (key + 1) * (key + 1)
            elif val % (key + 1) > 0:
                res += (val // (key + 1) + 1) * (key + 1)
        return res
