class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions) + 1) 
        for i in range(len(questions) - 1, -1, -1):
            points, jump = questions[i][0], questions[i][1]
            dp[i] = max(points + dp[min(jump + i + 1, len(questions))], dp[i + 1])
        return dp[0]