class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap = {'}':'{',']':'[',')':'('}
        stack = []
        if len(s) <=1:
            return False
        for c in s:
            if c == '[' or c=='(' or c == '{':
                stack.append(c)
            else:
                if not stack or stack[-1]!=hashmap[c]:
                    return False
                else:
                    stack.pop()

        return len(stack)==0
            
        
        
