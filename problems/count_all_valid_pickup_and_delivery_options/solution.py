class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9 + 7
        pickup = math.factorial(n) % mod
        delivery = reduce(operator.mul, range(1, 2 * n, 2), 1) % mod
        return pickup * delivery % mod
        