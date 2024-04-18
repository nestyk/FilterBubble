from dataclasses import dataclass
from FilterBubble.Paths import Paths
import json
from FilterBubble.Users.UserClass import User
@dataclass
class Profiles(User):
    def __init__(self):
        pass
    def getProfile(self,username):
        with open(Paths().PROFILESPATH, 'r') as f:
            profiles = json.load(f)
            if username in profiles:
                return profiles[username]
            else:
                return None
    def addProfile(self,user):
        with open(Paths().PROFILESPATH, 'w') as f:
            likedPosts = dict(user.likedPosts)



            payload = {user.username:
                        {
                            "mostInterestingTopic":user.getMostInterestingTopic(),
                            "likedPosts":likedPosts
                        }
                    }

            json.dump(payload,f)
    def updateProfile(self,username = None, likedPosts = None):
        if likedPosts != None:
            self.likedPosts = likedPosts
            self.mostInterestingTopic = self.getMostInterestingTopic()
        if username != None:
            self.username = username

        with open(Paths().PROFILESPATH, 'w') as f:
            likedPosts = dict(self.likedPosts)
            payload = {self.username:
                {
                    "mostInterestingTopic": self.getMostInterestingTopic(),
                    "likedPosts": likedPosts
                }
            }

            json.dump(payload, f)

            



