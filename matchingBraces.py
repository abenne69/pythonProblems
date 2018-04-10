class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        matchParens = {"{":"}", "(":")", "[":"]"}
        
        for i in range(0,len(s)):
            if(s[i] == "(" or s[i] == "{" or s[i] == "["):
                stack.append(s[i])
            elif(len(stack) > 0): #know it is a closing type
                tempVal = stack.pop()
                if(s[i] != matchParens[tempVal]):
                    return False
            else:
                return False
        
        if(len(stack) == 0):
            return True
        else:
            return False
def main():
    import sys
    sol = Solution()

    solution = sol.longestCommonPrefix(["aaa","aa","aaa"])

    print solution, "*"

main()