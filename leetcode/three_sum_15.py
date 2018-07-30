'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
import two_sum


def threeSum(nums):
    result=[]
    nums.sort()
    for i in range(len(nums)):
        if nums[i]==nums[i-1] and i>0:
            continue
        target=-nums[i]
        start=i+1
        end=len(nums)-1
        while(start<end):
            if nums[start]+nums[end]>target:
                end=end-1
            elif nums[start]+nums[end]<target:
                start=start+1
            else:
                result.append([nums[i],nums[start],nums[end]])
                start=start+1
                end=end-1
                while(start<end and nums[end]==nums[end+1]):
                    end=end-1
    return result



#版本V1.0：超时
'''
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result=[]
    result_final=[]
    nums_sort=sorted(nums)
    for i in range(len(nums_sort)):
        a1=nums_sort[i]
        num_target_1=-a1
        for j in range(i+1,len(nums_sort)):
            a2=nums_sort[j]
            num_target_2=-a1-a2
            for k in range(j+1,len(nums_sort)):
                if nums_sort[k]==num_target_2:
                    result.append([nums_sort[i],nums_sort[j],nums_sort[k]])
                    break
                else:
                    continue
    if result[0]!=None:
        result_final.append(result[0])
    for i in range(1,len(result)):
        if result_final.count(result[i])==1:
            continue
        else:
            result_final.append(result[i])
    return result_final
'''



def main(argv=None):
    nums = [0,0,0]
    print(threeSum(nums))


if __name__ == '__main__':
    main()