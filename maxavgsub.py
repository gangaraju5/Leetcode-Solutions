"""You are given an integer array nums consisting of n elements, and an integer k.


 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000      """





class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=0
        for i in range(k):
            s+=nums[i]
        maxsum =s
        startindx=0
        endindx=k
        while(endindx < len(nums)):
            s-=nums[startindx]
            startindx+=1

            s+=nums[endindx]
            endindx+=1
            maxsum =max(maxsum,s)
        return maxsum/k




        



        
        