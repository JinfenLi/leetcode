# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n:
        :rtype: int
        """
        rows = len(n)
        columns=len(n[0])
        degree={}
        for r in range(rows):
            for c in range(columns):
                if r!=c:
                    degree[r]=degree.get(r,0)+n[r][c]
        print(degree)
if __name__ == '__main__':
    s=Solution()
    s.findCelebrity([
  [1,1,0],
  [0,1,0],
  [1,1,1]
])
