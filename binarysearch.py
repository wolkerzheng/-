#encoding=utf8

def binarySearch(nums,val):

    start,end = 0,len(nums)-1

    while start <= end:

        mid = (start+end)/2

        if nums[mid] == val:
            return mid
        elif nums[mid]> val:
            end = mid-1
        else:
            start = mid+1
    return -1

if __name__ == '__main__':
    l = [1, 4, 12, 45, 66, 99, 120, 444]
    print binarySearch(l, 12)
    print binarySearch(l, 1)
    print binarySearch(l, 13)
    print binarySearch(l, 444)