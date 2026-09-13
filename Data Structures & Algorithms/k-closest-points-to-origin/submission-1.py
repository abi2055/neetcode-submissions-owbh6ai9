class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # you have a fixed point
        # you would just need to calculate each of the points
        # distances in a for loop and push to a heap
        # then just output the minimum distance in a min heap

        minimum_distances = []
        results = []

        def calculate_distance(x, y):
            return math.sqrt(((x - 0)**2) + ((y - 0)**2))

        for point in points:
            dist = [calculate_distance(point[0], point[1]), point]
            heapq.heappush(minimum_distances, dist)

        for _ in range(k):
            results.append(heapq.heappop(minimum_distances)[1])

        return results


        