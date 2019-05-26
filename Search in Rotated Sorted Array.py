class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        pivot = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                pivot = i
        if target > nums[-1]:
            for i in range(pivot):
                if nums[i] == target:
                    return i
                return -1
        else:
            for i in range(pivot, len(nums)):
                if nums[i] == target:
                    return i
                return -1
if __name__ == '__main__':
    s=Solution()
    s.search([1],2)