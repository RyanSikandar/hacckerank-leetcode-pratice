class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = self.isAlphanum(s)
        result = result.lower()
        p1=0
        p2=-1
        for x in range(len(result)//2):
            if result[p1]!=result[p2]:
                return False
            else:
                p1+=1
                p2-=1
        return True

    def isAlphanum(self,s):
        result = ":.,' @#_-\{\}[]\"\'?!;()`~"
        for token in result:
            s = s.replace(token, "")
        return s
