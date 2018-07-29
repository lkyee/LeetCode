'''
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    lenth=len(nums)
    for i in range(lenth):
        num_find=target-nums[i]
        for j in range(i+1,lenth):
            if(nums[j]==num_find):
                return i,j
            else:
                continue



def main(argv=None):
    nums=[2,3,4,5,6]
    print(twoSum(nums,6))
    
    
    
    
    

if __name__ == '__main__':
    main()