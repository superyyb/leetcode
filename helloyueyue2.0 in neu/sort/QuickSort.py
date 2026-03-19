import random
def QuickSort(nums:[int],low:int,high:int)->[int]:
    i=random.randint(low,high)#choose an index of pivot randomly

def partition(nums:[int],low:int,high:int)->[int]:#use two pointers to partite
    pivot=nums[low]
    while low<high:
        while nums[high]>=pivot:
            high-=1
        while nums[low]<=pivot:
            low+=1



