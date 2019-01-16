'''
Simulates python array built-in functions

list.append(x)
Add an item to the end of the list; equivalent to a[len(a):] = [x].

list.extend(L)
Extend the list by appending all the items in the given list; equivalent to a[len(a):] = L.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is x. It is an error if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.index(x)
Return the index in the list of the first item whose value is x. It is an error if there is no such item.

list.count(x)
Return the number of times x appears in the list.

list.sort(cmp=None, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list, in place.
'''

class Array(object):
    def __init__(self):
        self.index = 0
        self.size = 10
        self.array = [0] * self.size
    
    def values(self):
        return self.array[:self.index]
        
    def resize(self, multiplier=2):
        self.size *= multiplier
        arr = [0] * self.size
        for i in range(self.size / multiplier):
            arr[i] = self.array[i]
        self.array = arr

    def append(self, x):
        if self.index >= self.size: self.resize()
        self.array[self.index] = x
        self.index += 1
    
    def extend(self, L):
        if self.index + len(L) >= self.size:
            multiplier = (self.index + len(L)) / self.size * 2
            self.resize(multiplier)
        for element in L:
            self.array[self.index] = element
            self.index += 1

    def insert(self, i, x):
        if self.index >= self.size: self.resize() 
        if i >= self.index: 
            self.append(x)
        else:
            for index in range(self.index, i, -1):
                self.array[index] = self.array[index-1]
            self.array[i] = x
            self.index += 1

    def find(self, x):
        found = -1
        for i in range(self.index):
            if self.array[i] == x:
                found = i
                break
        return found

    def remove(self, x):
        found = self.find(x)
        if found != -1:
            for i in range(found, self.index):
                self.array[i] = self.array[i+1]
            self.index -= 1


    def pop(self, i=None):
        self.index -= 1
        res = self.array[i]
        for _i in range(i, self.index):
            self.array[_i] = self.array[_i+1]
        return res

    def count(self):
        return self.index

    def reverse(self):
        for i in range(self.index / 2):
            self.array[i], self.array[self.index-1-i] = self.array[self.index-1-i], self.array[i] 

    def sort(self):
        pass



'''
a = Array()
for i in range(20):
    a.append(i)
l = range(20)
print a.array
b = [[5]] * 10
a.extend(b)
l.extend(b)
print a.array
print l
b[0].append(6)
print b
print a.array
print l
a = Array()
for i in range(20):
    a.insert(i, i)
print a.array
for i in range(20):
    a.insert(i*2, i*5)
print a.array
a.insert(5, 1000)
print a.values()
a.append(20)
print a.values()
print a.array
a.remove(0)
a.remove(30)
a.remove(19)
a.remove(500)
print a.values()
a.pop(0)
a.pop(3)
print a.values()
a.reverse()
print a.values()
'''