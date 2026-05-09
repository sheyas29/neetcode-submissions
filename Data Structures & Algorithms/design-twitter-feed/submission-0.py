import heapq
from collections import defaultdict

class Tweet:
    def __init__(self, tweetId, time):
        self.id = tweetId
        self.time = time
        self.next = None


class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = {}  # userId -> head of tweet list
        self.followMap = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.time += 1
        tweet = Tweet(tweetId, self.time)
        
        # insert at head (latest first)
        tweet.next = self.tweetMap.get(userId)
        self.tweetMap[userId] = tweet
        
        # ensure user follows themselves
        self.followMap[userId].add(userId)

    def getNewsFeed(self, userId):
        res = []
        heap = []

        followees = self.followMap[userId]
        followees.add(userId)

        # push latest tweet of each followee
        for user in followees:
            if user in self.tweetMap:
                tweet = self.tweetMap[user]
                heapq.heappush(heap, (-tweet.time, tweet))

        # get top 10
        while heap and len(res) < 10:
            time, tweet = heapq.heappop(heap)
            res.append(tweet.id)

            if tweet.next:
                heapq.heappush(heap, (-tweet.next.time, tweet.next))

        return res

    def follow(self, followerId, followeeId):
        self.followMap[followerId].add(followeeId)
        self.followMap[followerId].add(followerId)

    def unfollow(self, followerId, followeeId):
        if followeeId != followerId:
            self.followMap[followerId].discard(followeeId)