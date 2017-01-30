"""
Things to Remember
Inherit directly from Python¡¯s container types (like list or dict) for simple use cases.
Beware of the large number of methods required to implement custom container types correctly.
Have your custom container types inherit from the interfaces defined in collections.abc to ensure that your classes match required interfaces
and behaviors.
"""

class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)
    
    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1
        return counts
    
class BinaryNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#To make the BinaryNode class act like a sequence, you can provide a custom implementation of __getitem__
class IndexableNode(BinaryNode):
    def _search(self, count, index):
        # ...
        # Returns (found, count)
        pass
    def __getitem__(self, index):
        found, _ = self._search(0, index)
        if not found:
            raise IndexError('Index out of range')
        return found.value
    
class SequenceNode(IndexableNode):
    def __len__(self):
        _, count = self._search(0, None)
        return count

tree = IndexableNode(
                    10,
                    left=IndexableNode(
                                    5,
                                    left=IndexableNode(2),
                                    right=IndexableNode(
                                                   6, right=IndexableNode(7))),
                    right=IndexableNode(
                                    15, left=IndexableNode(11)))

print('LRR =', tree.left.right.right.value)
print('Index 0 =', tree[0])
print('Index 1 =', tree[1])
print('11 in the tree?', 11 in tree)
print('17 in the tree?', 17 in tree)
print('Tree is', list(tree))

#Defining your own container types is much harder than it looks.
#To avoid this difficulty throughout the Python universe, the built-in collections.abc module defines a set of abstract base classes that provide all of the typical methods for each container type.
from collections.abc import Sequence
class BetterNode(SequenceNode, Sequence):
    pass