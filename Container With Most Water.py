class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lp,rp,maximum=0,len(height)-1,0
        while lp<rp:
            minimum = min(height[lp],height[rp])
            if maximum < (rp-lp) * minimum:
                maximum =(rp-lp) * minimum
            if minimum == height[lp]:
                lp+=1
            else:
                rp-=1
        return maximum
            
