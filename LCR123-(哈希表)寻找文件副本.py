#yy思路：用集合查重？重复的单独放在一个集合里，输出该集合里的任一项
class Solution:
    def findRepeatDocument(self, documents: list[int]) -> int:
        set_1=set()
        set_2=set()
        for doc in documents:
            if doc not in set_1:
                set_1.add(doc)
            else:
                set_2.add(doc)
        for doc in set_2:
            return min(set_2)

#简化版：不需要把所有重复的都列出来，只要发现一个重复的就立刻return
class Solution:
    def findRepeatDocument(self, documents: list[int]) -> int:
        set_1=set()
        for doc in documents:
            if doc in set_1:
                return doc
            set_1.add(doc)
