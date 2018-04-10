class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        index = 0
        
        for keys in dic:
            if(s.find(keys) > -1):
                index = s.find(keys)
                highestRankRoman = keys
        
        value = 0
        
        if (index == 0 or highestRankRoman == "I"):
            value = dic[highestRankRoman]
            return self.calculateRemaining(value,index+1,s)
        else:
            for i in range(0,index):
                if(i == index):
                    value = dic[s[i]] - value
                    return self.calculateRemaining(value,index+1,s)
                else:
                    value += dic[s[i]]
                    
    def calculateRemaining(self, value, index, s):
        for i in range(index,len(s)-1):
            value += dic[s[i]]
        
        return value

def main():
    import sys
    sol = Solution()

    solution = sol.longestCommonPrefix(["aaa","aa","aaa"])

    print solution, "*"

main()