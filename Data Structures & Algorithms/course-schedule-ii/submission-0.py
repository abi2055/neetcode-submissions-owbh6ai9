class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # use khans algo for cycle detection and directed graph
        # 1) build the amount of edges pointing to that node
        # 2) build an adjacency list
        indegree = [0] * numCourses
        adjacency_list = [[] for i in range(numCourses)]
        for destination, source in prerequisites:
            indegree[destination] += 1
            adjacency_list[source].append(destination)

        q = collections.deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        finish = 0
        output = []

        while q:
            node = q.popleft()
            finish += 1
            output.append(node)
            for neighbor in adjacency_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if finish == numCourses:
            return output
        else:
            return []


        
