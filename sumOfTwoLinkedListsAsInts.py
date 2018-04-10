class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self):
        l1 = ListNode(1)
        l2 = ListNode(2)
        l1.next = ListNode(3)
        l1.next.next = ListNode(5)
        l2.next = ListNode(5)
        l2.next.next = ListNode(7)

        print l2.next.next.val

        l1Int = 0
        l2Int = 0

        multiplier = 10
        tempL1Node = l1
        tempL2Node = l2
        intIsCreated = False

        while(intIsCreated == False):
            l1Int = (l1Int*multiplier) + l1.val
            l2Int = (l2Int*multiplier) + l2.val
            
            print l1.val, "  -  ", l2.val

            if((l1.next is None) & (l2.next is None)):
                intIsCreated = True
            if(l1.next is not None):
                l1 = l1.next
            if(l2.next is not None):
                l2 = l2.next    
        return l1Int+l2Int

def main():
    import sys
    sol = Solution()

    solution = sol.addTwoNumbers()
    print solution


main()