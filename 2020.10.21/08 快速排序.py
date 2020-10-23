# 快排
def swap(ilist,a,b):
    ilist[a], ilist[b] = ilist[b],ilist[a]
    # return ilist
def partition(ilist, start, end):
    poive = ilist[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and ilist[p] < poive:
            p += 1
        while p <= q and ilist[q] >= poive:
            q -= 1
        if p < q:
            swap(ilist, p, q)
    swap(ilist, start, q)
    return q
def quickSort(ilist,start,end):
    if start >= end:
        return
    mid = partition(ilist, start, end)
    quickSort(ilist, start, mid - 1)
    quickSort(ilist, mid + 1, end)
    return ilist
print(quickSort([3,5,2,1,5,6,8],0,6))





