class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            max_area = max(
                max_area, min(heights[left], heights[right]) * (right - left)
            )
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area
        