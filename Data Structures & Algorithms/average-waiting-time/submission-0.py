class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curtime=customers[0][0]
        s=0
        for i in range(len(customers)):
            arrival=customers[i][0]
            prep=customers[i][1]
            if arrival<curtime:
                curtime+=prep
                s+=curtime-arrival
            else:
                s+=prep
                curtime=arrival+prep
        
        return s/len(customers)
            


        