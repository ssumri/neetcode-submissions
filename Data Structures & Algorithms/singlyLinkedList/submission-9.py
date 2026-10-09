class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        for i in range(index ):
            if curr is None:
                return -1
            curr = curr.next
        if curr is None:
            return -1
        # if index is out of bounds
        return curr.val

    def insertHead(self, val: int) -> None:
        head = ListNode(val) 
        if self.head is None:
            self.head = head
        else:
            head.next = self.head
            self.head = head

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = newNode

    def remove(self, index: int) -> bool:
        # if removing head
        if self.head == None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        prev = self.head
        temp = prev.next
        # if removing in the middle
        for i in range(index - 1): 
            if temp == None:
                return False
            prev = temp
            temp = temp.next
        
        # if removing last node
        if temp == None:
            return False
        
        prev.next = temp.next
        return True

    def getValues(self) -> List[int]:
        vals = []
        temp = self.head
        while temp is not None:
            vals.append(temp.val)
            temp = temp.next
        return vals
        