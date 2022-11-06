'''
learnt from official approach 5:
merge + divide & conquer
'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        K = len(lists)
        interval = 1
        
        '''
        e.g. 6 lists
        
        interval = 1, range(0, 6-1=5, 1*2=2) == [0,2,4]
        lists[0]=lists[0]+lists[1]
        lists[2]=lists[2]+lists[3]
        lists[4]=lists[4]+lists[5]
        
        interval = 2, range(0, 6-2=4, 2*2=4) == [0]
        lists[0]=lists[0]+lists[2]
        
        interval = 4, range(0, 6-4=2, 4*2=8) == [0]
        lists[0]=lists[0]+lists[4]
        
        interval = 8
        result=lists[0]
        '''
        while interval < K:
            for i in range(0, K - interval, interval*2):
                lists[i] = self.merge2sortedlists(lists[i], lists[i+interval])
            interval *= 2
        
        return lists[0] if K > 0 else None
    
    def merge2sortedlists(self, l1, l2):
        head = point = ListNode(0)  # dummy head node
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        
        if not l1:
            point.next = l2
        else:
            point.next = l1
        
        return head.next


'''
official approach 3: Priority Queue
'''
from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)


class Solution3:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = point = ListNode(0)  # dummy head node
        
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put(PrioritizedItem(node.val, node))
        
        while not q.empty():
            item = q.get()  # retrieve smallest node
            val, node = item.item.val, item.item
            point.next = node
            point = point.next
            node = node.next
            if node:
                q.put(PrioritizedItem(node.val, node))
        
        return head.next
