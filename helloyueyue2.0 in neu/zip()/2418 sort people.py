class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # ❌用dic储存映射，无法处理重复人名
        # dic = {}
        # for name, height in zip(names, heights):
        #     dic[name] = height
        # return sorted(dic.keys(), key = lambda x: dic[x], reverse = True)
        people = list(zip(names, heights))  # 必须加list才能print出可读的列表
        print(people)  # [('Mary', 180), ('John', 165), ('Emma', 170)]
        people.sort(key=lambda x: x[1], reverse=True)
        return [name for name, height in people]  # 一行列表one line

    """
    等价于：
    res = []
    for name, height in people:
        res.append(name)
    return res
    """