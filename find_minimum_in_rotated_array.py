class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lp, rp = 0, len(nums) - 1
        while lp < rp:
            mid = (lp + rp) // 2
            if nums[mid] > nums[rp]:
                lp = mid + 1
            else:
                rp = mid
        return nums[lp]
