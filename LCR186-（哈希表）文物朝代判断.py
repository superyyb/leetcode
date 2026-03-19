#yy思路：除0以外编号不能有重复的，且最大编号-最小编号≤5
class Solution:
    def checkDynasty(self, places: list[int]) -> bool:
        repeat=set() #用于存储出现过的编号
        ma,mi=0,14
        for place in places:
            if place==0:continue
            ma=max(ma,place)
            mi=min(mi,place)
            if place in repeat:
                return False
            repeat.add(place)
        return ma-mi<5

        places.sort()
        del_places=[num for num in places if num!=0]
        for i in range(len(del_places)):
            if del_places[i+1]-del_places[i]==1:
                return True

