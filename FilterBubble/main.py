from FilterBubble.Users.UserClass import User
from FilterBubble.Users.ProfilesClass import Profiles
from FilterBubble.Posts.PostsClass import Posts
u1 = User("test",{"9":"Cucina"})

for a in range(10):
    Posts().createNewPost("TEST_CUCINA" + str(a),"Cucina")
Profiles().addProfile(u1)
Posts().showPosts(u1)