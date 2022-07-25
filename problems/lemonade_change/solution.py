class Solution:
    def lemonadeChange(self, customers: List[int]) -> bool:
        if not customers:
            return True

        # Initialize the popsicle stand with the first customer
        popsicle_stand = {5: 0, 10: 0, 20: 0}
        if customers[0] != 5:
            return False
        popsicle_stand[customers[0]] += 1

        for customer in customers[1:]:
            if customer == 5:
                popsicle_stand[5] += 1
            elif customer == 10:
                if popsicle_stand[5] <= 0:
                    return False
                popsicle_stand[5] -= 1
                popsicle_stand[10] += 1
            elif customer == 20:
                if popsicle_stand[10] > 0 and popsicle_stand[5] > 0:
                    popsicle_stand[10] -= 1
                    popsicle_stand[5] -= 1
                elif popsicle_stand[5] >= 3:
                    popsicle_stand[5] -= 3
                else:
                    return False

        return True