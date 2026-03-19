#只存储key，并不关心对应的value是多少
class MyHashSet:
    def __init__(self):#define parameter
        self.capacity=1000
        self.hashset=[[] for _ in range(self.capacity)]

    def hash(self,key:int)->int:#define a hashtable
        return key%self.capacity#(value=key%capacity)
        #modulo 保证无论 key 的值多大，key%self.capacity的结果总是在0到self.capacity-1之间
    def add(self, key: int) -> None:
        hash_key=self.hash(key)
        if key in self.hashset[hash_key]:
            return
        self.hashset[hash_key].append(key)

    def remove(self, key: int) -> None:
        hash_key = self.hash(key)
        if key not in self.hashset[hash_key]:
            return
        self.hashset[hash_key].remove(key)

    def contains(self, key: int) -> bool:
        hash_key = self.hash(key)
        return key in self.hashset[hash_key]

    def __str__(self):
        hash_list=[]
        for hash in self.hashset:
            if hash: #不加上这句 会打印出1000个（对应capacity）个items
                hash_list.append(hash)
        return ", ".join(map(str, hash_list))

if __name__=="__main__":
    myHashSet=MyHashSet()
    myHashSet.add(1)
    myHashSet.add(2)
    print(myHashSet)
    print(myHashSet.contains(1))
    print(myHashSet.contains(3))
    myHashSet.remove(2)
    print(myHashSet.contains(2))

#既存储key，也存储value，可以用一个tuple(key,value)表示
class MyHashMap:
    def __init__(self):
        self.capacity=1000
        self.map=[[] for _ in range(self.capacity)]#定义map中每一个元素都是一个[]
    def _hash(self,key:int)->int:
        return key%self.capacity
    def put(self,key:int,value:int):
        h=self._hash(key)
        for i,(k,v) in enumerate(self.map[h]): # 遍历h中已有的条目，检查key是否已经存在
            if k==key:
                self.map[h][i]=(key,value)
            return
        self.map[h].append((key,value))

    def get(self,key:int):
        h = self._hash(key)
        for k,v in self.map[h]:
            if k==key:
                return v
        return -1

    def remove(self,key:int):
        h = self._hash(key)
        for i,(k,v) in enumerate(self.map[h]):
            if k==key:
                del self.map[h][i]
                return

    def __str__(self):
        hash_tuple=[]
        for item in self.map:
            for key, value in item:
                hash_tuple.append(f"{key}: {value}")
        return "{"+", ".join(hash_tuple)+"}"

if __name__ == "__main__":
    myMap = MyHashMap()
    myMap.put(1, 100)
    myMap.put(2, 200)
    print(myMap)
    print(myMap.get(1))
    print(myMap.get(3))
    myMap.put(2, 250)
    print(myMap.get(2))
    myMap.remove(1)
    print(myMap.get(1))