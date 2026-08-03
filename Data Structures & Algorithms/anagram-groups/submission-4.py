class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana={}
        for word in strs:
            s=""
            b={}
            for c in word:
                if c in b:
                    b[c]+=1
                else:
                    b[c]=1
            # print(b)
            for i in range(97,123):
                c=chr(i)
                if c in b:
                    s+=c*b[c]
            # print(word, s)
            if s in ana:
                ana[s].append(word)
            else:
                ana[s]=[word]
        return list(ana.values())
            

        