class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lp = 0
        rp = len(numbers)-1
        sum =0
        while(lp<rp):
            sum = numbers[lp]+numbers[rp]
            if(sum==target):
                return [lp+1,rp+1]
            if(sum>target):
                rp-=1
            else:
                lp+=1
                
        return []

        
