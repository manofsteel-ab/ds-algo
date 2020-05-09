class Solution:

    def __init__(self):
        self.graph = collections.defaultdict(list)

    def _clear_graph(self):
        self.graph = collections.defaultdict(list)

    def _init_graph(self, weighted_matrix):

        print(weighted_matrix)
        self._clear_graph()

        for u,v,w in weighted_matrix:
            self.graph[u].append((v,w))

    def _dfs(self, src, destination_distance: dict):
        pass

    def _bfs(self, src, destination_distance: dict):

        queue = [src]

        while queue:

            u = queue.pop()
            for v,w in self.graph[u]:
                if destination_distance[u] + w < destination_distance[v]:
                    destination_distance[v] = min(
                        destination_distance[u] + w, destination_distance[v]
                    )
                    queue.append(v)


    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        if not times:
            return -1

        self._init_graph(times)

        if K not in self.graph:
            return -1

        destination_distance = {node:float('inf') for node in range(1, N+1)}
        destination_distance[K] = 0

        self._bfs(K, destination_distance)

        ans = max(destination_distance.values())
        if ans<float(inf):
            return ans
        return -1
