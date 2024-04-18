from dataclasses import dataclass
from os.path import exists
from os import mkdir
from Paths import Paths
import json

#User class, interactions and favourites topics
@dataclass
class User:
    username: str
    likedPosts: dict

    def __init__(self, username, likedPosts):
        if not exists("../Datas"):
            mkdir("../Datas")

        mostInterestingTopicValue = max(likedPosts.keys())
        self.likedPosts = likedPosts
        self.username = username
        self.mostInterestingTopic = likedPosts[mostInterestingTopicValue]
        self.save()


    def save(self):
        newDict = {
            self.username:
            {
            "mostInterestingTopic": self.mostInterestingTopic
            }
        }
        if not exists(Paths().PROFILESPATH):
            with open(Paths().PROFILESPATH, "w") as f:
                json.dump(newDict, f)
        else:
            with open(Paths().PROFILESPATH, "r") as file:
                fileLoaded = {}
                if file.read(1):
                    fileRead = file.read()
                    if not fileRead.startswith("{"):
                        fileRead = "{" + fileRead
                    fileLoaded = json.loads(fileRead)
                fileLoaded[self.username] = {
                    "mostInterestingTopic": self.mostInterestingTopic,
                    "likedPosts": self.likedPosts
                    }
            with open(Paths().PROFILESPATH, "w") as file:
                json.dump(fileLoaded, file)
