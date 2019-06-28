class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        output = [0] * 26
        for i in tasks:
            output[ord(i) - ord('A')] = output[ord(i) - ord('A')] + 1

        count = 0
        len_o = 0
        max_o = max(output)
        for i in output:
            if i == max_o:
                count = count + 1

        return max(len(tasks), (max_o - 1) * (n + 1) + count)

if __name__ == '__main__':
    s=Solution()
    s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2)