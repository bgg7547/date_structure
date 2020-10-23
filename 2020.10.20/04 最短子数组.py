#  209
def T209(nums,s):
    l,sums,res = 0,0,float("inf")
    for r in range(len(nums)):
        sums += nums[r]
        while sums >= s:
            if r - l + 1 < res:
                res = r -l + 1
            sums -= nums[l]
            l += 1

    return 0 if res == float("inf") else res
