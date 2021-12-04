#1.两数之和
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        new_nums = {}
        for k,v in enumerate(nums):
            new_nums[k] = v

        for i in new_nums.keys():
            for j in range(i+1,len(nums)):
                if new_nums[i] + new_nums[j] == target:
                    return i,j
        -----
        for idx, leftv in enumerate(nums):
            for idx2,rightv in enumerate(nums[idx+1:]):
                if leftv + rightv == target:
                    return idx,idx2+idx+1
        '''
        new_nums = {nums[0]: 0}
        for k,v in enumerate(nums[1:]):
            v2 = target - v
            idx2 = new_nums.get(v2, None)
            if idx2 != None:
                return k+1, idx2
            else:
                new_nums[v] = k+1