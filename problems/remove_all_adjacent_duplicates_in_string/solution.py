class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        return reduce(
            lambda stack, char: stack[:-1] if stack[-1:] == char else stack + char, s
        )