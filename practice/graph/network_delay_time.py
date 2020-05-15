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

    def _bfs(self, N, src):

        destination_distance = {node:float('inf') for node in range(1, N+1)}
        destination_distance[src] = 0

        queue = [src]

        while queue:

            u = queue.pop()
            for v,w in self.graph[u]:
                if destination_distance[u] + w < destination_distance[v]:
                    destination_distance[v] = min(
                        destination_distance[u] + w, destination_distance[v]
                    )
                    queue.append(v)

        ans = max(destination_distance.values())
        if ans<float(inf):
            return ans
        return -1

    def _dijkstra(self, N, src):

        pq = [(0, src)]

        destination_distance = {}

        while pq:

            w,u = heapq.heappop(pq)

            if u in destination_distance:
                continue

            destination_distance[u] = w

            for v,w in self.graph[u]:
                if v not in destination_distance:
                    heapq.heappush(pq, (destination_distance[u]+w, v))
        # print(destination_distance.values())
        if len(destination_distance.values()) == N:
            return max(destination_distance.values())
        return -1


    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        if not times:
            return -1

        self._init_graph(times)

        if K not in self.graph:
            return -1

        return self._dijkstra(N, K)
