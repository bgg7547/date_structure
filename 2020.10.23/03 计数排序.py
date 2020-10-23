
def countSort(nums):
    countList = [0] * (max(nums)+ 1)
    for i in nums:
        countList[i] += 1
    res = []
    for j in range(len(countList)):
        res += [j] * countList[j]
    return res
print(countSort([9,3,5,4,9,1,2,7,8,1,3,6,5,3,4,0,10,9,7,9]))

