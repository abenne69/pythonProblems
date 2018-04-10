class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if(len(strs) == 1):
            return strs[0]
        elif(len(strs) == 0):
            return ""
        else:
            if(len(strs[0]) > 0):
                return self.recursiveCall(strs,0)    
            else:
                return ""
    
    def recursiveCall(self,strs,partition):
        compareStr = ""

        for i in range(0, len(strs)):
            tempStr = strs[i]
            if(len(tempStr) < 1):
                return ""
            if(partition > len(tempStr)-1):
                return tempStr[:partition+1]
            if(i == 0):
                compareStr = tempStr[partition]
            if(compareStr != tempStr[partition]):
                print compareStr, " - ", tempStr
                if(partition == 0):
                    return ""
                else:
                    return tempStr[0:partition]
            elif(i == len(strs)-1):
                if(len(tempStr) > partition+1):
                    return self.recursiveCall(strs,partition+1)
                else:
                    if(partition > 0):
                        return tempStr[0:partition+1]
                    else:
                        return tempStr[0]
            
def main():
    import sys
    sol = Solution()

    solution = sol.longestCommonPrefix(["aaa","aa","aaa"])

    print solution, "*"


main()