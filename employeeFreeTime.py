class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[List[int]]]
        :rtype: List[List[int]]
        """
        schedule = [y for x in schedule for y in x]
        schedule.sort()
        result = []
        rightmost = schedule[0][1]
        leftmost = schedule[0][0]
        for i in range(1, len(schedule)):
            if schedule[i][0] > rightmost and rightmost > leftmost:
                result.append([rightmost, schedule[i][0]])
                leftmost = schedule[i][0]
                rightmost = schedule[i][1]

            else:
                rightmost = max(rightmost, schedule[i][1])

        return result
if __name__ == '__main__':
    s=Solution()
    s.employeeFreeTime([[[7,24],[29,33],[45,57],[66,69],[94,99]],[[6,24],[43,49],[56,59],[61,75],[80,81]],[[5,16],[18,26],[33,36],[39,57],[65,74]],[[9,16],[27,35],[40,55],[68,71],[78,81]],[[0,25],[29,31],[40,47],[57,87],[91,94]]])