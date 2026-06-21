class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        temp=[]
        for i in range(0,len(nums)):
            left=i+1
            right=len(nums)-1
            while left < right:            
                som=nums[left] + nums[i] + nums[right]
                if som == 0:
                    if ([nums[left],nums[i],nums[right]]) not in temp:
                        temp.append([nums[left],nums[i],nums[right]])
                    left+=1
                    right-=1
                elif som < 0:
                    left+=1
                elif som > 0:
                    right -=1
        return temp
                