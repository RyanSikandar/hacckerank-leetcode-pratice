class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # If there's only one car, then it forms a fleet on its own.
        if len(position) == 1:
            return 1
        
        # Initialize an empty list to store the fleets
        answer = []
        
        # Create a list of lists where each sublist contains a car's position and speed
        pos_sp = [[p, s] for p, s in zip(position, speed)]
        
        # Sort the list of cars based on their positions
        pos_sp.sort()
        
        # Add the last car to the answer list
        answer += [pos_sp.pop()]
        
        # Iterate over the sorted list of cars in reverse order
        for p_s in reversed(pos_sp):
            # Calculate time taken for the car at position 'p_s[0]' to reach the target
            # and compare it with the time taken for the last car in 'answer' to reach the target
            if float(target - p_s[0]) / p_s[1] <= float(target - answer[-1][0]) / answer[-1][1]:
                # If the current car will take more time to reach the target than the last car in 'answer',
                # then skip this car as it will form a fleet with the car ahead of it
                continue
            else:
                # If the current car will reach the target faster than the last car in 'answer',
                # then add this car to 'answer' as it forms a new fleet
                answer += [p_s]
        
        # The length of 'answer' represents the number of fleets formed
        return len(answer)
