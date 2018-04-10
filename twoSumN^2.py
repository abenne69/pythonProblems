class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if(len(nums) < 2):
            return False
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i,j]

def main():
    import sys
    sol = Solution()

    #solution = sol.letterCombinations("5678")
    haystack = "a"
    needle = ""

    print len(needle), " - ", len(haystack)

main()