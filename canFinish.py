import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degrees = [0] * numCourses
        childs = [[] for x in range(numCourses)]
        for pair in prerequisites:
            degrees[pair[0]] += 1
            childs[pair[1]].append(pair[0])
        courses = set(range(numCourses))
        flag = True
        while flag and len(courses):
            flag = False
            removeList = []
            for x in courses:
                if degrees[x] == 0:
                    for child in childs[x]:
                        degrees[child] -= 1
                    removeList.append(x)
                    # flag means if there is degree==0
                    flag = True
            for x in removeList:
                courses.remove(x)
        print(courses)
        return len(courses) == 0

    # 方法是每次选择入度为0的节点，作为序列的下一个节点，然后移除该节点和以从节点出发的所有边。
    # 那这个方法比较简单粗暴了：要循环N次，这个循环次数并不是遍历节点的意思，而是我们如果正常取点的话，N次就能把所有的节点都取完了，
    # 如果N次操作结束还没判断出来，那么就不是DAG.在这N次中，每次都找一个入度为0的点，并把它的入度变为 - 1，作为已经取过的点不再使用，
    # 同时把从这个点指向的点的入度都 - 1.
    # 这个过程中，如果找不到入度为0的点，那么说明存在环。如果N次操作，每次都操作成功的去除了一个入度为0的点，那么说明这个图是DAG.

    def canFinish2(self, N, prerequisites):
        """
        :type N,: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for u, v in prerequisites:
            graph[v].append(u)
            indegrees[u] += 1
        for i in range(N):
            zeroDegree = False
            for j in range(N):
                if indegrees[j] == 0:
                    zeroDegree = True
                    break
            if not zeroDegree: return False
            indegrees[j] = -1
            for node in graph[j]:
                indegrees[node] -= 1
        return True

    def canFinish3(self, N, prerequisites):
        """
        :type N,: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
        # 0 = Unknown, 1 = visiting, 2 = visited
        visited = [0] * N
        for i in range(N):
            if not self.dfs(graph, visited, i):
                return False
        return True

    # Can we add node i to visited successfully?
    def dfs(self, graph, visited, i):
        # 访问到的点正在访问，有环
        if visited[i] == 1: return False
        if visited[i] == 2: return True
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        visited[i] = 2
        return True





if __name__ == '__main__':
    s=Solution()
    s.canFinish3(4,[[0,2],[2,3],[1,0],[2,1]])