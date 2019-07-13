class Solution:
    def maxSubarraySumCircular(self, A):
        ans1 = cur = A[0]
        for x in A[1:]:
            cur = x + max(cur, 0)
            ans1 = max(ans1, cur)

        # ans2: answer for two-interval subarray, interior in A[1:]
        ans2 = cur = float('inf')
        for i in range(1, len(A)):
            cur = A[i] + min(cur, 0)
            ans2 = min(ans2, cur)
        ans2 = sum(A) - ans2

        return max(ans1, ans2)
if __name__ == '__main__':
    s=Solution()
    s.maxSubarraySumCircular([5,-3,5])