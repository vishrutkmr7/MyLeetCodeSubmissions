class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)
        salary.pop(0)
        salary.pop()
        return sum(salary)/len(salary)