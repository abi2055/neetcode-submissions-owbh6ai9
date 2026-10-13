class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        h = [ -c for c in count.values() ]
        # heap contains the frequency count of each task
        heapq.heapify(h)
        # converted to a heap

        total_time = 0
        # the total time of all the operations
        q = deque()
        # queue containing the order when each task should be "deployed"

        while h or q:
            # if theyre both non empty
            total_time += 1
            # each loop is +1 time 
            if h:
                c = 1 + heapq.heappop(h)
                # since its negative in the heap, one use is gone
                if c != 0:
                    q.append([c, total_time + n])
                    # queue (count, time when use)
            if q and q[0][1] == total_time:
                heapq.heappush(h, q.popleft()[0])

        return total_time
            
