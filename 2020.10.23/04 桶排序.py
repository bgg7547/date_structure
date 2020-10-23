
def bucketSort(nums):
    max_value = max(nums)
    min_value = min(nums)
    d = max_value - min_value

    # 初始化桶
    bucketcount = len(nums)  #桶个数
    count_list = []          #最外面的桶
    for i in range(bucketcount):
        count_list.append([])

    # 定位元素
    for i in range(len(nums)):
        num = int((nums[i] - min_value ) / d * (bucketcount - 1))
        bucket = count_list[num]
        bucket.append(nums[i])

    # 桶内部排序
    for i in count_list:
        i.sort()

    # 输出
    res = []
    for i in count_list:
        for j in i:
            res.append(j)
    return res
print(bucketSort([3,2,8,6,4,1]))


