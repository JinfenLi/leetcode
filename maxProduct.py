class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxPro=nums[0]
        prevMax,prevMin=nums[0],nums[0]
        for i in range(1,len(nums)):
            curMax=max(nums[i],nums[i]*prevMax,prevMin*nums[i])
            curMin = min(nums[i],nums[i]*prevMax,prevMin*nums[i])
            prevMin,prevMax=curMin,curMax
            maxPro=max(maxPro,curMax)
        return maxPro
