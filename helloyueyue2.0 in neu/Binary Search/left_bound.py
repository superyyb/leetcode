"""
给定一个包含重复元素的排序数组nums，请查找 target 在数组中的左边界：
arr=[1,2,3,3,3,4,6]，target=3，结果应该返回 2，如果不存在，请返回 −1
     0,1,2,3,4,5,6
"""

def left_bound(nums:[list],target:int)->int:
    l , r = 0, len(nums) - 1#[0,6]
    ans=-1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            ans=mid
            r = mid - 1#每遇到一个target更新一次ans，一直往左推直到遇到最后一个target
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return ans



#[]
#1 2 3 5 5 5 8 9
#0 1 2 3 4 5 6 7
#找到第一个>=5的元素
def left_bound(nums:[list],target:int)->int:
    l, r = 0 ,len(nums)-1 #[0,7]
    ans=-1
    while l <= r:
        mid = l + (r - l) // 2#[0,7] mid=3 nums[mid]=5
        if nums[mid] == target:
            ans=mid
            r = mid - 1#因为我已更新了符合的mid到ans中，因此下一次区间可以不包含mid
        elif nums[mid] < target:
            l = mid + 1#nums[mid]不等于target，因此下一次区间也不包含mid
        elif nums[mid] > target:
            r = mid - 1
    return ans

#1 2 3 5 5 5 8 9
#0 1 2 3 4 5 6 7
#找到最后一个<5的元素
def smaller_than_5(nums:[list],target:int)->int:
    l, r = 0 ,len(nums)-1 #[0,7]
    while l <= r:
        mid = l + (r - l) // 2  # [0,7] mid=3 nums[mid]=5
        if nums[mid] >= target:
            r = mid - 1#已经确定nums[mid]>=target，而我们要找<target，所以下一个区间不要包括mid
        elif nums[mid] < target:
            l = mid + 1#已经确定nums[mid]<target，但是题目要求找最后一个，因此还需要往右搜索
    #跳出循环时，l=r+1，l 指向的是第一个 “不满足” 条件的位置（ nums[l] ≥ target），
    #r指向的是最后一个 “满足” 条件的位置（nums[l] < target）
    return r

#1 2 3 5 5 5 8 9
#0 1 2 3 4 5 6 7
#找到第一个>5的元素
def smaller_than_5(nums:[list],target:int)->int:
    l, r = 0 ,len(nums)-1 #[0,7]
    while l <= r:
        mid = l + (r - l) // 2  # [0,7] mid=3 nums[mid]=5
        if nums[mid] < target:
            l = mid + 1#已经确定nums[mid] < target，mid不是我们要找的，下个区间不要包括mid
        elif nums[mid] > target:
            r = mid - 1#mid有可能是答案，但是要找>5中最小的，还要继续往左收敛，往左收敛需要挪r一直到r<l退出
            # 循环，在最后一次循环中，l=r=mid 此时答案在[l,r]中，但是退出循环后r=l-1,最终答案应该要返回l
        elif nums[mid] == target:
            l = mid + 1
        #跳出循环时，l=r+1，l指向第一个不满足 nums[mid] ≤ target 的位置，也就是第一个 nums[l] > target。
	#r 指向最后一个 nums[r] ≤ target 的位置r为满足条件的左区间中右边界，
    return l

#1 2 3 5 5 5 8 9
#0 1 2 3 4 5 6 7
#找到最后一个<=5的元素
# [0,7] mid=3 nums[mid]=5
# [4,7] mid=5 nums[mid]=5
# [6,7] mid=6 nums[mid]=8
# [6,6] mid=6 nums[mid]=8
# [6,5]
def smaller_than_5(nums:[list],target:int)->int:
    l, r = 0 ,len(nums)-1 #[0,7]
    while l <= r:
        mid = l + (r - l) // 2  # [0,7] mid=3 nums[mid]=5
        if nums[mid] <= target:
            l = mid + 1#可能是答案，但是不一定是最后一个，因此还需要向右收敛,一直挪l直到不符合，
            # 即nums[mid] > target，此时的l是第一个不符合的l
        if nums[mid] > target:
            r = mid - 1#mid肯定不是答案，需要向左收敛
    return r

if __name__ == "__main__":
    nums=[1,2,3,5,5,5,8,9]
    target=5
    print(smaller_than_5(nums,target))