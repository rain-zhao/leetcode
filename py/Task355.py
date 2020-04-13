# 设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

# postTweet(userId, tweetId): 创建一条新的推文
# getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
# follow(followerId, followeeId): 关注一个用户
# unfollow(followerId, followeeId): 取消关注一个用户
# 示例:

# Twitter twitter = new Twitter();

# // 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
# twitter.postTweet(1, 5);

# // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
# twitter.getNewsFeed(1);

# // 用户1关注了用户2.
# twitter.follow(1, 2);

# // 用户2发送了一个新推文 (推文id = 6).
# twitter.postTweet(2, 6);

# // 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
# // 推文id6应当在推文id5之前，因为它是在5之后发送的.
# twitter.getNewsFeed(1);

# // 用户1取消关注了用户2.
# twitter.unfollow(1, 2);

# // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
# // 因为用户1已经不再关注用户2.
# twitter.getNewsFeed(1);

from typing import List
from collections import deque
from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follows = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.num = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].append((tweetId, self.num))
        self.num += 1
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """

        self.follows[userId].add(userId)
        res = []
        candidate = []
        # using heap to get the newest tweets
        for followeeId in self.follows[userId]:
            if followeeId not in self.tweets:
                continue
            tweets = self.tweets[followeeId]
            idx = len(tweets)-1
            tweetId, tweetNum = tweets[-1]
            candidate.append((-tweetNum, tweetId, followeeId, idx))
        heapq.heapify(candidate)

        while len(res) < 10 and candidate:
            tweetNum, tweetId, userId, idx = candidate[0]
            res.append(tweetId)
            if idx > 0:
                tweets = self.tweets[userId]
                tweetId, tweetNum = tweets[idx-1]
                heapq.heapreplace(candidate,(-tweetNum, tweetId, userId, idx-1))
            else:
                heapq.heappop(candidate)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follows[followerId].add(followerId)
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId or followerId not in self.follows:
            return
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(1, 5)
# print(obj.getNewsFeed(1))
# obj.follow(1, 2)
# obj.postTweet(2, 6)
# print(obj.getNewsFeed(1))
# obj.unfollow(1, 2)
# print(obj.getNewsFeed(1))
obj = Twitter()
obj.postTweet(1, 5)
obj.postTweet(1, 3)
print(obj.getNewsFeed(1))
