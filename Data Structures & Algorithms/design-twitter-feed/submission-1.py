class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)    # userId -> list of [time, tweetId]
        self.followers = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1  # negative so min-heap pops newest first

    def getNewsFeed(self, userId: int) -> List[int]:
        results = []
        heap = []

        for followeeId in self.followers[userId] | {userId}:
            if self.tweets[followeeId]:
                index = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][index]
                heap.append([time, tweetId, followeeId, index - 1])

        heapq.heapify(heap)

        while heap and len(results) < 10:
            time, tweetId, followeeId, index = heapq.heappop(heap)
            results.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweets[followeeId][index]
                heapq.heappush(heap, [time, tweetId, followeeId, index - 1])

        return results

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)