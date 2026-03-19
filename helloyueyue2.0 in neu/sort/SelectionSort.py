def SelectionSort(nums:[int])->[int]:
    for i in range(len(nums)-1):#[3,5,1,4,6,0]
        min_i=i#set the index of minimum
        print(min_i)
        for j in range(i+1,len(nums)):#search for minimum in unsorted part
            if nums[j]<nums[min_i]:
                nums[j],nums[min_i]=nums[min_i],nums[j]#exchange
                print(nums)
    return nums

if __name__=="__main__":
    print(SelectionSort([3,7,1,4,12,5]))


