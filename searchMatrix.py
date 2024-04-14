class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        top_r, bott_r = 0, len(matrix)-1

        while top_r<=bott_r:
            curr_row = (top_r + bott_r)//2
            if target > matrix[curr_row][-1]:
                top_r = curr_row+1
            elif target < matrix[curr_row][0]:
                bott_r = curr_row-1
            else:
                break
        
        if not (top_r<=bott_r):
            return False
        
        current = (top_r + bott_r)//2
        lp,rp = 0,len(matrix[0])

        while lp<=rp:
            mid = (lp+rp)//2
            if target > matrix[current][mid]:
                lp = mid+1
            elif target < matrix[current][mid]:
                rp = mid-1
            else:
                return True
        return False
        
