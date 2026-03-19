class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hash={}
        for num in nums1:
            if num in hash:
                hash[num]+=1
            else:
                hash[num]=1#hash[key]=value   key为元素 value为出险次数
        set_num=set()
        for num_2 in nums2:
            if num_2 in hash:
                set_num.add(num_2)
        return list(set_num)

if __name__=="__main__":
    nums1 = [4,9,5]  #如果将nums1放入hash：{4: 1, 9: 1, 5: 1}
    nums2 = [9,4,9,8,4]  #如果将nums2放入hash：{9: 2, 4: 2, 8: 1}
    sol=Solution()
    result=sol.intersection(nums1,nums2)
    print(result)
