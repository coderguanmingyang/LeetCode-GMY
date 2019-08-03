# -*- coding:utf-8 -*-
'''
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

'''
## Solution
# 在一个线性概率来随机找到一个item，最简单的就是用一个list来把所有元素都存下来
# 这样就能按照个数为概率来select元素


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = dict()
        self.list = list()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool

        """
        self.list.append(val)
        if not self.dict.has_key(str(val)):
            self.dict[str(val)] = 1
            return True
        else:
            self.dict[str(val)] += 1
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.dict.has_key(str(val)):
            if self.dict[str(val)] == 1:
                del self.dict[str(val)]
            else:
                self.dict[str(val)] -= 1
            index = self.list.index(val)
            del self.list[index]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        #item = random.choice(self.dict)
        item = random.choice(self.list)
        return int(item)

if __name__ == "__main__":

    # Your RandomizedSet object will be instantiated and called as such:
    obj = RandomizedCollection()
    print obj.insert(1)
    print obj.insert(1)
    print obj.insert(2)
    print obj.getRandom()
    print obj.remove(1)
    print obj.getRandom()
