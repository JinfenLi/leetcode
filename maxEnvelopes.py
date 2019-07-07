class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        if not envelopes:
            return 0

        n = len(envelopes)
        envelopes.sort(key = lambda x:(x[0], -x[1]))
        dp = [envelopes[0][1]]
        for _, h in envelopes[1:]:
            if h > dp[-1]:
                dp.append(h)
            else:
                pos = self.helper(dp, h)
                dp[pos] = h
        return len(dp)

    def helper(self, arr, target):
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l + r) >> 1
            if arr[mid] < target:
                l = mid + 1
            else:
                if mid > 0 and arr[mid-1] >= target:
                    r = mid - 1
                else:
                    return mid


if __name__ == '__main__':
    s=Solution()
    s.maxEnvelopes([[3,4],[12,2],[12,15],[30,50]])