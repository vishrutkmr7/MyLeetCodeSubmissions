class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], wanted: int, limit: int) -> int:
        if not values or not labels or not wanted or not limit:
            return 0

        items = sorted(zip(values, labels), reverse=True)
        label_count = {}
        total = 0

        for value, label in items:
            if wanted == 0:
                break

            if label_count.get(label, 0) < limit:
                total += value
                label_count[label] = label_count.get(label, 0) + 1
                wanted -= 1

        return total
