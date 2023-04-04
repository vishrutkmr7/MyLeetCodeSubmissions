class Solution:
    def angleClock(self, hours: int, minutes: int) -> float:
        hour_angle = (hours % 12 + minutes / 60) * 30
        minute_angle = minutes * 6
        angle = abs(hour_angle - minute_angle)
        return min(angle, 360 - angle)