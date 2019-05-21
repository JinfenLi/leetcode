import copy
class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        all_nums = []
        for i in range(len(nums)):
            newnums = copy.copy(nums)
            newnums.remove(newnums[i])
            if self.twoSum(newnums, -nums[i])!=None:
                l, r = self.twoSum(newnums, -nums[i])
                all_nums.append(sorted([l, r, nums[i]]))
        new_all =[]
        for an in all_nums:
            if an not in new_all:
                new_all.append(an)
        return new_all

    def twoSum(self, nums, target):
        left = 0
        right = len(nums) - 1

        for i in range(len(nums)):

            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                return nums[left], nums[right]
        if left>=right or nums[left]+nums[right]!= target:
            return None
        return nums[left], nums[right]
if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))