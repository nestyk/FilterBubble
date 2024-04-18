from dataclasses import dataclass
from FilterBubble.Paths import Paths
import json


@dataclass
class Posts:
    def __init__(self):
        self.loadPosts()
    def loadPosts(self):
        with open(Paths().POSTSPATH, "r") as file:
            try:
                self.posts = json.load(file)
            except:
                self.posts = {}
    def updateFile(self):
        with open(Paths().POSTSPATH, "w") as file:
            json.dump(self.posts, file)

    def createNewPost(self, content, topic):
        if len(self.posts) == 0:
            self.posts[1] = {"topic": topic, "content": content}
            self.updateFile()
        else:
            newID = int(max(self.posts.keys())) + 1
            self.posts[newID] = {"topic": topic, "content": content}
            self.updateFile()

    def getPostsByTopic(self, topic):
        postsIdByTopic = []
        for key, value in self.posts.items():
            if value["topic"] == topic:
                postsIdByTopic.append(key)
        return postsIdByTopic
    def showPosts(self, user):
        postsIdByTopic = self.getPostsByTopic(user.mostInterestingTopic)
        print("Showing Posts")
        for ID in postsIdByTopic:
            print("[ - ] Post ID: " + str(ID))
            print("[ - ] Content: " + self.posts[ID]["content"])



        