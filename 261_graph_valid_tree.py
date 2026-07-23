class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid if no cycles, fully connected
        # track cycles via visited set
        # fully connected by counting length of visited set to the number of nodes

        # dfs
        # O(n+e) n = number nodes, e = number edges
        # number of edges should be n - 1
        if len(edges) != n - 1:
            return False

        # build adjacency list for undirected graph
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        # -1 is default prev value
        return dfs(0,-1) and len(visited) == n
    