class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = True
        i = len(nums) - 2
        while i > 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            for j in reversed(range(i, len(nums))):
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                    nums[i + 1:] = sorted(nums[i + 1:])
                    flag = False
                    break
        if flag:
            nums.sort()





