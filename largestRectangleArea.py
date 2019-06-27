#stack store the  index of height smaller than the height of current index
# 使用一个单调递增栈来维护已经出现了的矩形高度，如果后面新来的元素高度比栈里最后的元素高，那么需要入栈，因为面积最大的元素会出现在后面。
# 如果后面新来的元素高度比栈里的最后的元素小，那么需要弹出栈里的元素，并且，每次弹出的时候都要对计算目前的宽度，相乘得到面积。
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = list()
        res = 0
        heights.append(0)
        N = len(heights)
        for i in range(N):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    h = heights[stack[-1]]
                    stack.pop()
                    w = i if not stack else i - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(i)
        return res

