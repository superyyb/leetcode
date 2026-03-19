def bubblesort(nums:[int])->[int]:#O(n2)
    for i in range(len(nums)-1):#loop i controls the number of cycles
        flag=False#note whether exchange happens in loop j
        for j in range(len(nums)-i-1):#loop j controls the exchange of two elements
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                flag=True
        if not flag:
            break
    return nums

if __name__=="__main__":
    print(bubblesort([11,2,7,6,5,1]))



