class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        # Compute net profit for every person.
        personNetProfit = {}
        for lender, borrower, amount in transactions:
            personNetProfit[lender] = personNetProfit.get(lender, 0) - amount
            personNetProfit[borrower] = personNetProfit.get(borrower, 0) + amount
        netProfit = [amount for amount in personNetProfit.values() if amount != 0]
        return self.traverse(netProfit, 0, 0)

    def traverse(self, netProfit, startIdx, numTrans):
        # Skip settled people.
        while startIdx < len(netProfit) and netProfit[startIdx] == 0:
            startIdx += 1
        if startIdx + 1 >= len(netProfit):
            return numTrans
        for i in range(startIdx + 1, len(netProfit)):
            # Greedy condition.
            if netProfit[startIdx] + netProfit[i] == 0:
                netProfit[i] += netProfit[startIdx]
                minNumTrans = self.traverse(netProfit, startIdx + 1, numTrans + 1)
                netProfit[i] -= netProfit[startIdx]
                return minNumTrans

        minNumTrans = float("inf")
        for i in range(startIdx + 1, len(netProfit)):
            # Non-greedy condition for possible closing out in the future.
            if netProfit[startIdx] * netProfit[i] < 0:
                netProfit[i] += netProfit[startIdx]
                minNumTrans = min(
                    minNumTrans,
                    self.traverse(netProfit, startIdx + 1, numTrans + 1),
                )
                netProfit[i] -= netProfit[startIdx]
        return minNumTrans
