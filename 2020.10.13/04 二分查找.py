def erfen(nums,target):
    slow = -1
    fast = len(nums)
    while slow <= fast:
        mid = (slow + fast) // 2
        # if target < nums[mid]:
        #     fast  = mid
        # elif target > nums[mid]:
        #     slow = mid
        # else:
        #     return mid

print(erfen([-1,0,3,9,12],12))

