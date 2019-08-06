# 8/5/2019
# detect loop in a LL
# Given a linked list, check if LL has loop or not

## use hashing by traversing the list one by one and keep putting the 
## node addresses in a Hash Table
##

class Solution(object):
    def checkCycle(self, head):
        """
        input:  ListNode head
        return: boolean
        """
        # write the code here
        