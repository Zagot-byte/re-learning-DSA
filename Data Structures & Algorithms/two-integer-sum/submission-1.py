class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        need=0
        for i in range(0,len(nums)):
            need=target-nums[i]
            if need in dic:
                return [dic[need],i]
            if need not in dic:
                dic[nums[i]]=i            
                
        
    
