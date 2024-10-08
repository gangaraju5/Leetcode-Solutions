from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if len(nums) != 3:
            return "none"
        
        a, b, c = nums[0], nums[1], nums[2]
        
        # Check if the sides form a valid triangle
        if not (a + b > c and a + c > b and b + c > a):
            return "none"
        
        # Determine the type of triangle
        if a == b == c:
            return "equilateral"
        elif a != b and b != c and a != c:
            return "scalene"
        else:
            return "isosceles"

        