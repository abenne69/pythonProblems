class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        P     I    N
        A   L S  I G
        Y A   H R     
        P     I
        """
        if(numRows == 1):
            return s

        allStrings = []
        for i in range(0,numRows):
            allStrings.append("")
        
        counter = 0
        isIncreasing = True
        for i in range(0,len(s)):
            allStrings[counter] += s[i]
            
            if isIncreasing:
                if counter == numRows-1:
                    isIncreasing = False
                    counter-=1
                else:
                    counter+=1
            else:
                if counter == 0:
                    isIncreasing = True
                    counter+=1
                else:
                    counter -= 1
                
        tempString = ""
        for i in range(0,len(allStrings)):
            tempString += allStrings[i]
        
        return tempString

def main():
    sol = Solution()
    print(sol.convert("ABA",1))

main()