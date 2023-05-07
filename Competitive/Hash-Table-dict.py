class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        found = False
        for idx, element in enumerate(self.arr[h]):
            # If length of element is 2
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
        if not found:
            self.arr[h].append((key, value))

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print(f'Deleting element at index {index}')
                del self.arr[arr_index][index]

t = HashTable()

# Collision will happen as hashing of both "march 6" and "march 17" are 9
print(t.get_hash("march 6"))
print(t.get_hash("march 17"))

t["march 6"] = 120
t["march 8"] = 67
t["march 9"] = 4
t["march 17"] = 459

# If we print "march 6" it'll print 459 not 120 as hashing if both "march 6" and "march 17" are 9
print(t["march 6"])
print(t.arr)
del t["march 17"]
print(t.arr)
