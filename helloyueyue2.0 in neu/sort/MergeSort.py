'''
Merge Sort:Divide and Conquer
1.Split
2.Sort recursively
3.Merge
'''

def merge_sort(lst:list)->list:
    print(f"split list:{lst}")
    if len(lst)<=1:#Recursive termination condition
        print(f"recursion terminate:{lst}")
        return lst
    mid=len(lst)//2
    first_lst=merge_sort(lst[:mid])#DFS,
    # first solves all sub problems in the left half until the baseline condition is reached.
    sec_list=merge_sort(lst[mid:])
    merged=merge_sorted_list(first_lst,sec_list)
    print(f"merge{first_lst} and {sec_list} to {merged}")
    return merged
def merge_sorted_list(first_lst,sec_list):
    merged=[]
    i,j=0,0
    while i<len(first_lst) and j<len(sec_list):
        if first_lst[i]<sec_list[j]:
            merged.append(first_lst[i])
            i+=1
        else:
            merged.append(sec_list[j])
            j+=1
    merged+=first_lst[i:]
    merged+=sec_list[j:]
    return merged

if __name__=="__main__":
    lst=[4,2,1,3]
    print(merge_sort(lst))

