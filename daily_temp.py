class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        prevdays = [] #consists of all the prev warm days that are less that the current day
        for curday, curtemp in enumerate(temperatures):
            #iterate while the stack is not empty and also while the current temperature is warmer than the one at the top of the stack
            while prevdays and curtemp > temperatures[prevdays[-1]]:
                index = prevdays.pop()
                result[index] = curday - index
            prevdays.append(curday)
        return result
