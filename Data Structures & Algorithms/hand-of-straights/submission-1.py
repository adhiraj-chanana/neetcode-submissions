class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False

        c={}
        for i in hand:
            if i in c:
                c[i]+=1
            else:
                c[i]=1

        hand.sort(reverse=True)
        i=0
        total=0
        # print(hand)
        # print(c)
        # print('......')
        while i<len(hand):
            if c[hand[i]]:
                for j in range(groupSize):
                    # print(j, print(hand[i]-j))
                    if (hand[i]-j) in c and c[hand[i]-j]:
                        c[hand[i]-j]-=1
                        total+=1
                    else:
                        return False
            i+=1
        if total==len(hand):
            return True
        else:
            return False







