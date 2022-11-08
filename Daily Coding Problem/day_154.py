''' Implementation of heaped list in HeapedList '''

import heapq

class HeapedList:
    ''' Heapified list object '''

    def __init__(self, starter_list: list) -> None:
        heapq.heapify(starter_list)
        self.class_list = starter_list
        self.recent_added = None

    def push(self, item) -> None:
        ''' Adds a nwe key to the heap '''
        self.class_list.append(item)

    def pop(self):
        ''' Rmeoves and returns the max valkue of the heap '''
        return self.class_list.pop()


a = HeapedList([1,2,3,4,5,6,7,8])

a.push(46)
b = a.pop()

print(b)
print(a)
