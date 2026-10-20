# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        auxArray1 = []
        auxArray2 = []
        
        while(list1 != None):
            auxArray1.append(list1.val)
            list1 = list1.next
         
        while(list2 != None):
            auxArray2.append(list2.val)
            list2 = list2.next
        
        junctionArray = auxArray1 + auxArray2
        junctionArray.sort()

        headNode = None
        lastNode = None
        for idx, number in enumerate(junctionArray):
            if idx == 0:
                headNode = ListNode(number)
                lastNode = headNode
            else:
                newNode = ListNode(number)
                lastNode.next = newNode
                lastNode = newNode
        
        return headNode