# given a binary tree, write a function that returns whether or not it is a valid BST

           5
        /      \
    4              12
  /   \          
 1      6   
    
    
    
class Solution():
    def __init_ Solution(self,root):
        self.max = root.value
        self.min = root.value
    def isValidTree(self,root):
        if root.left == None & root.right == None:
            return True
        else:
            if(root.left != None):
                bool1 = recursiveCall(root.value, root.left, True)
            if(root.right != None):
                bool2 = recursiveCall(root.value, root.right, False)
            if bool1 & bool2:
                return True
            else:
                return False
            
    def recursiveCall(self, val, node, isLeft):
        truthValue = False
        if(isLeft):
            if node.value <= val & node.value < self.min:
                    self.min = node.value
                    tempValue = determineNumberOfBranches(node)
                    truthValue = True
                    if(tempValue == -1):
                        truthValue = recursiveCall(node.val,node.left,True)
                    elif(tempValue == 1):
                        truthValue = recursiveCall(node.val,node.right,False)
                    elif(tempValue == 0):
                        truthValue = recursiveCall(node.val,node.left,True) #5,1N,True
                        truthValue = truthValue & recursiveCall(node.val,node.right,False) #5, 6N, False
            else:
                return truthValue
        else:
            if node.value >= val & node.value > self.max:
                self.max = node.value
                truthValue = True
                tempValue = determineNumberOfBranches(node)
                if(tempValue == -1):
                    truthValue = recursiveCall(node.val,node.left,True)
                elif(tempValue == 1):
                    truthValue = recursiveCall(node.val,node.right,False)
                elif(tempValue == 0):
                    truthValue = recursiveCall(node.val,node.left,True) #5,1N,True
                    truthValue = truthValue & recursiveCall(node.val,node.right,False) #5, 6N, False
            else:
                return truthValue
        return truthValue
            
    def determineNumberOfBranches(self, node):
        if(node.left != None & node.right == None):
            return -1
        elif(node.right != None & node.left == None):
            return 1
        else:
            return 0
        return 2
    
def main():
    sol = Solution()
    sol.isValidTree()
main()