def calculate_sum(nums):
    #res = sum(nums)
    total = 0
    for i in range(len(nums)):
        total += nums[i] #15
    return total

#array:[1,1,3,4,5,5,6,3]
#output:1,3,5
'''
Use dictionary to store the frequency of each number
{1:2, 3:2, 4:1, 5:2, 6:1}

sort:[1,1,3,3,4,5,5,6]
for loop nums[n-1] == nums[n]
'''

