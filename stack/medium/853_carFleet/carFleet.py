# There are n cars going to the same destination along a 
# one-lane road.  The destination is target miles away.
# You are given two integer arrays position and speed,
# both of length n, where position[i] is the position of
# the ith car and speed[i] is the speed of the ith car
# (in miles per hour). A car can never pass another car
# ahead of it, but it can catch up to it, and drive bumper
# to bumper at the same speed. The distance between these
# two cars is ignored - they are assumed to have the same
# position. A car fleet is some non-empty set of cars
# driving at the same position and same speed. Note that a
# single car is also a car fleet. If a car catches up to a
# car fleet right at the destination point, it will still
# be considered as one car fleet.
# Return the number of car fleets that will arrive at the
# destination.

# Constraints:
# n == position.length == speed.length
# 1 <= n <= 10^5
# 0 < target <= 10^6
# 0 <= position[i] < target
# All the values of position are unique.
# 0 < speed[i] <= 10^6

# Example:
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3

# The cars cannot pass each other, but they can catch up.
# Then any car behind a slower car will catch up to the 
# slower car, forming a car fleet. We can use a stack
# to keep track of the cars that are behind a slower car,
# but we will have to sort the cars by position first.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # If there is only one car, it is a car fleet
        if len(position) == 1:
            return 1

        # Sort the cars by position
        cars = sorted(zip(position, speed), reverse=True)

        # Keep track of the cars that are behind a slower car
        stack = []

        # Iterate through the cars
        for car in cars:
            # Add the current time of arrival to the stack
            stack.append((target - car[0]) / car[1])

            # If there at least two cars in the stack and the
            # current car is faster than the car in front of it,
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # Remove the faster car from the stack
                stack.pop()

        # Return the number of cars in the stack
        return len(stack)
    # We pass through the n cars in linear time, but are 
    # limited by the sorting algorithm. The stack is at
    # most n cars, so Time: O(n log n), Space: O(n)