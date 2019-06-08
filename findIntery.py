import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)
        for frm, to in tickets:
            graph[frm].append(to)
        for frm, tos in graph.items():
            tos.sort(reverse=True)
        res = []
        self.dfs(graph, "JFK", res)
        return res[::-1]

    def dfs(self, graph, source, res):
        while graph[source]:
            v = graph[source].pop()
            self.dfs(graph, v, res)
        res.append(source)
if __name__ == '__main__':
    s=Solution()
    s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])