class Twitter:

    def __init__(self):
        self.tweets={}
        self.follows={}
        self.count=-1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append([self.count,tweetId])
            self.count-=1
        else:
            self.tweets[userId]=[[self.count,tweetId]]
            self.count-=1
        
        if userId not in self.follows:
            self.follows[userId]=set([userId])

        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.follows:
            return
        arr=[]
        for user in self.follows[userId]:
            if user not in self.tweets:
                continue
            for tweet in self.tweets[user]:
                heapq.heappush(arr,tweet)
        l=[]
        for i in range(min(10,len(arr))):
            a=heapq.heappop(arr)
            l.append(a[1])
        return l
                    

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId==followeeId:
            return
        if followerId in self.follows:
            if followeeId in self.follows[followerId]:
                return
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId]=set([followerId, followeeId])



        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId==followeeId:
            return
        
        if followerId in self.follows:
            if followeeId in self.follows[followerId]:
                self.follows[followerId].remove(followeeId)



        
