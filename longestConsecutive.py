class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        result = 1
        final = 1
        i=1
        while i<len(nums):
            if nums[i] == nums[i - 1]:
                i += 1
            elif nums[i] == nums[i - 1] + 1:
                result = max(result, result + 1)
            else:
                result = 1
            final = max(final, result)

        return final
if __name__ == '__main__':
    s=Solution()
    s.longestConsecutive([0,-1])
