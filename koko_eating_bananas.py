class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        lp,rp=1,max(piles)
        result = rp
        while lp<=rp:
            k = (lp+rp)//2
            hours = 0
            for i in piles:
                hours += (i+k-1) // k
            if hours <= h:
                result = min(result,k)
                rp = k-1
            else:
                lp = k+1
        return result  
        
