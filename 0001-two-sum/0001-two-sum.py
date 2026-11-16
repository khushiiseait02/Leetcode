class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(0,len(nums)):
            currsum=target-nums[i]
            if currsum in dict:
                return [dict[currsum],i]
            else:
                dict[nums[i]]=i