class Solution:
    def coinChange(self, coins, amount: int) -> int:
        ans = [amount + 1] * (amount + 1)
        ans[0] = 0

        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if (coins[j] <= i):
                    ans[i] = min(ans[i - coins[j]] + 1, ans[i])
        print(ans)
        return -1 if ans[amount]>amount else ans[amount]
if __name__ == '__main__':
    s=Solution()
    s.coinChange([2],3)