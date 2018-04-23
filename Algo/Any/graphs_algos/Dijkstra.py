from heapq import heappush, heappop #Prim Spanning Tree

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        adj_list = self.create_adj_list(A, B)

        start_node = 1  ## doesn't matter actually, because all nodes should be connected
                        ## so 1 must also be connected
        return self.total_cost(adj_list, start_node)

    def create_adj_list(self, nodes_num, bridges):
        adj_list = [[] for _ in range(nodes_num + 1)]

        for source, dest, cost in bridges:
            adj_list[source] += [(dest, cost)]
            adj_list[dest] += [(source, cost)]

        return adj_list

    def total_cost(self, adj_list, start_node):
        visited = set()
        ans = []
        pq = [(0, start_node)]
        total_cost = 0

        while len(pq) > 0:
            cost, cur_node = heappop(pq)

            if cur_node in visited: continue

            for neighbor, neighbor_cost in adj_list[cur_node]:
                heappush(pq, (neighbor_cost + cost, neighbor))

            visited.add(cur_node)
            ans.append((cur_node, cost))

        return ans



A = 5
B = [
  [1, 2, 3],
  [2, 3, 4],
  [3, 4, 5],
  [4, 5, 6],
  [5, 1, 2],
  [2, 4, 3],
  [2, 5, 5],
  [1, 3, 2]
]

sol = Solution()
print(sol.solve(A, B))