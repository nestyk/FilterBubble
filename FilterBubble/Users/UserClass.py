from dataclasses import dataclass


#User class, interactions and favourites topics
@dataclass
class User:
    def __init__(self,username,likedPosts):
        self.username = username
        self.likedPosts = likedPosts

    def getMostInterestingTopic(self):
        mostInterestingTopicValue = max(self.likedPosts.keys())
        self.mostInterestingTopic = self.likedPosts[mostInterestingTopicValue]
        return self.mostInterestingTopic



