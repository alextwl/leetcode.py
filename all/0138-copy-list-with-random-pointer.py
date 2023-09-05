'''
2023/09/05 daily challenge

interweaving approach
'''

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        node = head
        
        '''
        interweave the old & new nodes.
        
        A -> a -> B -> b -> C -> c -> ...
        '''
        while(node):
            new_node = Node(node.val, node.next, node.random)
            old_node = node
            node = node.next
            old_node.next = new_node
        
        '''
        shift the random node pointers from old one to new one.

        e.g. from

        A -> a -> B -> b -> C -> c -> ...
        ^         |    |
        |         |    |
        +---------+----+
        
        to

             +---------+
             |         |
             v         |
        A -> a -> B -> b -> C -> c -> ...
        ^         |
        |         |
        +---------+
        '''
        node = head.next
        while(node):
            if node.random:
                node.random = node.random.next
            
            if not node.next:
                break
            node = node.next.next

        '''
        untangle the new part
        '''
        node = new_head = head.next
        while(node):
            if node.next:
                node.next = node.next.next
                node = node.next
            else:
                break

        return new_head

