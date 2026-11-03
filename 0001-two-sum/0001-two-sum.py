class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(0, len(nums)):
            currSum = target - nums[i]
            if currSum in dict:
                return [dict[currSum], i]
            else:
                dict[nums[i]] = i