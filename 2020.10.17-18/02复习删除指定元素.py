def remove(nums,data):
    s = 0
    f = 0    #如果s，f都指向data， f去找不等于data的元素
    while f < len(nums):
        if nums[f] == data:
            f += 1
        else:
            nums[s] = nums[f]
            s += 1
            f += 1
    return s,nums
print(remove([1,2,3,4,5],3))



