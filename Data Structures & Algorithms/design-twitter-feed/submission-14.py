class Twitter:
    from collections import defaultdict
    def __init__(self):
        self.user_network = defaultdict(set) #user :[users list] kind based on follow, everyone to everyone
        self.tweets = defaultdict(list) #user: [usertweets]; usertweet is tuple (num,tweetid)
        self.total_tweets = 0
        
    def ensure_self_follow(self,userId):
        if userId not in self.user_network:
            print("self follow")
            self.user_network[userId].add(userId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        #this is from where the process starts, when a tweet is posted, a user should get added if does not exists
        #a tweet should also get added to that users list of tweets
        self.ensure_self_follow(userId)
        self.total_tweets+=1
        self.tweets[userId].append((self.total_tweets, tweetId))
        #if new user add it to its own network
        # if userId not in self.user_network:
        #     self.user_network[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        #bruteforce way is to seel all users in network including itself O(1)
        #get all tweets for all users in the network O(numfollwer), sort them as per time O(nlogn) and return recent 10
        # print(users_in_network)
        self.ensure_self_follow(userId)
        users_in_network = self.user_network.get(userId, [])
        print(users_in_network)
        tweets = [] 
        for user in users_in_network:
            tweets.extend(self.tweets[user])
        tweets.sort(key=lambda x: x[0], reverse=True)
        #return recent ten
        return [tweet[1] for tweet in tweets[:10]]
        #since this is going to be freq ops, we should do something better
        #we can keep the tweets on a heap (tweet num, tweet), heappush for tweets
        #we pop from heap till heap or 10 tweets for

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.ensure_self_follow(followerId)
        #simply add to users network
        self.user_network[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #remove from network
        self.ensure_self_follow(followerId)
        if followeeId != followerId:
            self.user_network[followerId].discard(followeeId)
        
