class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build a graph as you check prereqs
        # if the flow of the nodes conflict
        # return false
        # if not return true
        # build a directional graph by identifying neighbors
        # khanns algo is more intuitive here
        # by calculating indegree you can get to a solution

        indegree = [0] * numCourses
        adjacency_list = [[] for i in range(numCourses)]
        for source, destination in prerequisites:
            indegree[destination] += 1
            # so for example, if destination = 2, index 2 is +1
            adjacency_list[source].append(destination)

        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for neighbor in adjacency_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if finish == numCourses:
            return True
        
        return False


        

