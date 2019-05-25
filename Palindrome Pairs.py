# 利用字典wmap保存单词 -> 下标的键值对
# 遍历单词列表words，记当前单词为word，下标为idx：
# 1).若当前单词word本身为回文，且words中存在空串，则将空串下标bidx与idx加入答案
# 2).若当前单词的逆序串在words中，则将逆序串下标ridx与idx加入答案
# 3).将当前单词word拆分为左右两半left，right。
# 3.1) 若left为回文，并且right的逆序串在words中，则将right的逆序串下标rridx与idx加入答案
# 3.2) 若right为回文，并且left的逆序串在words中，则将left的逆序串下标idx与rlidx加入答案
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        wmap = {w:i for i,w in enumerate(words)}

        def isPalindrome(word):
            length = len(word)
            for i in range(length//2):
                if word[i]!=word[length-1-i]:
                    return False
            return True
        res = set()
        for idx, word in enumerate(words):
            if word and isPalindrome(word) and "" in wmap:
                nidx = wmap[""]
                res.add((idx,nidx))
                res.add((nidx,idx))
            rword = word[::-1]
            if word and rword in wmap:
                nidx = wmap[rword]
                if idx != nidx:
                    res.add((idx, nidx))
                    res.add((nidx, idx))
            for x in range(1,len(word)):
                left,right =word[:x],word[x:]
                rleft, rright = left[::-1], right[::-1]
                if isPalindrome(left) and rright in wmap:
                    res.add((wmap[rright], idx))
                if isPalindrome(right) and rleft in wmap:
                    res.add((idx, wmap[rleft]))
        return list(res)

