class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        visited=set()
        def isValid(email):
            name,domain=email.split('@')
            newname=''
            for i in name:
                if i == '.':
                    continue
                elif i=='+':
                    break
                else:
                    newname+=i
            newemail=newname+'@'+domain
            if newemail in visited:
                return False
            else:
                visited.add(newemail)
                return True
        c=0
        for email in emails:
            if isValid(email):
                c+=1
        return c

            



            



        