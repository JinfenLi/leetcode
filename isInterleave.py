class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1)+len(s2)!=len(s3): return False
        dp=[[False for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        dp[0][0]=True
        for i in range(1,len(s1)+1):
            dp[i][0] = dp[i-1][0] and s3[i-1]==s1[i-1]
        for i in range(1,len(s2)+1):
            dp[0][i] = dp[0][i-1] and s3[i-1]==s2[i-1]
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        return dp[len(s1)][len(s2)]

    def isInterleave2(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        l = len(s3)
        if m + n != l:
            return False
        dp = [True for __ in range(m + 1)]
        for i in range(m):
            dp[i + 1] = dp[i] and s1[i] == s3[i]
        for j in range(n):
            dp[0] = dp[0] and s2[j] == s3[j]
            for i in range(m):
                dp[i + 1] = (dp[i] and s1[i] == s3[i + j + 1]) or (dp[i + 1] and s2[j] == s3[i + j + 1])
        return dp[m]