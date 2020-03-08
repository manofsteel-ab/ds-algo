class Solution:

    def __init__(self):
        self.graph = {}
        self.isCycle = False
        self.topologicalOrder = []

    def _initGraph(self, edges):
        for edge in edges:
            if edge[0] not in self.graph:
                self.graph[edge[0]] = []
            if edge[1] not in self.graph[edge[0]]:
                self.graph[edge[0]].append(edge[1])

    def _dfs(self, visited, v):
        if visited[v] == 'visited':
            return
        if visited[v] == 'marked':
            self.isCycle = True
            return
        visited[v] = 'marked'

        for reachable_node in self.graph.get(v, []):
            self._dfs(visited, reachable_node)
        self.topologicalOrder.append(v)
        visited[v] = 'visited'

    def canFinish(self, numCourses: int, prerequisites):
        self._initGraph(prerequisites)
        visited = ["unvisited"] * numCourses
        for v in range(numCourses):
            self._dfs(visited, v)
        if self.isCycle:
            return False
        return len(self.topologicalOrder) == numCourses

