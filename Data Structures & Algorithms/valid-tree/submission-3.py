class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # another cycle detection problem 
        # if visited nodes does not equal the size of n than its not valid
        # if theres a cycle not valid
        # lets do a dfs

        # 1) build and adjacency list empty

        if not n:
            return False

        adj_list = { i:[] for i in range(n)}

        # 2) build list
        # undirected so both sides are connected to one another
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        # 3) visited set
        visited = set()

        # 4) recursive dfs calls
        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)

            for neighbor in adj_list[i]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, i):
                    return False
                # here we're checking if the recursive call is false
            
            return True
        
        return dfs(0, -1) and n == len(visited)

