class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phoneNumbers = {"1":"","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz","0":""}
        newArray = []
        isFirstDigit = True

        if(len(digits) == 0):
            return newArray
        
        for i in digits:
            prevIndex = 0
            tempString = phoneNumbers[i]
            tempArray = newArray[:]  
            for z in range(0,len(phoneNumbers[i])):
                tempString = phoneNumbers[i]
                if(isFirstDigit):
                    newArray.append(tempString[z])
                    tempArray = newArray[:]
                    
                elif(tempString != ""):
                    if(z != 0 & z < len(phoneNumbers[i])):
                        newArray.extend(tempArray)    
                    print prevIndex, " - ", len(newArray), " - ", len(tempArray)
                    for k in range(prevIndex,len(newArray)):
                        #print newArray[k]
                        newArray[k] += tempString[z] 
                    prevIndex = len(newArray)
            isFirstDigit = False
            print len(newArray)
        return newArray

""" 
            print "**********"
            if isFirstDigit:
                for z in range(0, len(tempString)):
                    newArray.append(tempString[z])
            elif(tempString != ""):
                letterCount = 0 
                tempSizeOfArrayExtended = len(newArray)-1
                for z in range(0, len(tempString)):
                    newArray.extend(newArray)
                    print len(newArray), " *"
                for x in range(0, len(newArray)):
                    print x, " - ", tempSizeOfArrayExtended 
                    if(x != 0 & x % tempSizeOfArrayExtended == 0):
                        print x % tempSizeOfArrayExtended
                        letterCount+=1
                    newArray[x] += tempString[letterCount]
            isFirstDigit = False
        return newArray
"""          


def main():
    import sys
    sol = Solution()

    solution = sol.letterCombinations("5678")
    val = {"list":5,"x":3}


main()