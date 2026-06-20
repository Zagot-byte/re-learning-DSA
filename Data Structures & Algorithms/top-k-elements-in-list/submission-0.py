class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in range(0,len(nums)):
            if nums[i] in dict:
                dict[nums[i]]=dict[nums[i]]+1
            else:
                dict[nums[i]]=1
        pairs=list(dict.items())
        sor = sorted(pairs, key=lambda pair: pair[1], reverse=True)
        result=[]
        for i in range(0,k):
            result.append(sor[i][0])
        return result