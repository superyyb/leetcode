class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        hash_a={}
        for num_1 in nums1:
            for num_2 in nums2:
                sum_1=num_1+num_2
                if sum_1 in hash_a:
                    hash_a[sum_1]+=1
                else:
                    hash_a[sum_1]=1
        count=0
        for num_3 in nums3:
            for num_4 in nums4:
                sum_2=num_3+num_4#取相反数
                if -sum_2 in hash_a:
                    count+=hash_a[-sum_2]
        return count

def main():
    sol=Solution()
    nums1 = [1, 2,1]
    nums2 = [-2, -1,-1]
    nums3 = [-1, 2,0]
    nums4 = [0, 2,1]
    print(sol.fourSumCount(nums1, nums2, nums3, nums4))

if __name__=="__main__":
    main()


