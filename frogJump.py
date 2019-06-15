class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """

        if stones[1] != 1:
            return False

        last_jump_units = {s: set() for s in stones}
        last_jump_units[1].add(1)
        for s in stones[:-1]:
            for j in last_jump_units[s]:
                for k in (j - 1, j, j + 1):
                    if k > 0 and s + k in last_jump_units:
                        last_jump_units[s + k].add(k)
        return bool(last_jump_units[stones[-1]])

if __name__ == '__main__':
    s=Solution()
    s.canCross([0,1,3,5,6,8,12,17])
