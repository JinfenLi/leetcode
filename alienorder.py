from functools import cmp_to_key



class Solution:

    def alienOrder(self, words):
        result = {}
        samegroup = []
        for ww in range(1, len(words)):
            for i in range(min(len(words[ww]), len(words[ww - 1]))):
                if words[ww][i] != words[ww - 1][i]:

                    result[words[ww - 1][i]] = words[ww][i]
                    break
        print(result)
        for k,v in result.items():
            samegroup.append(k)
            if k in result.values()



s=Solution()
s.alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
])



