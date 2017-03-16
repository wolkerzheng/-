#encoding=utf8


def qsort(nums):
    """
    快速排序,从小到大排序
    :param nums:
    :return:
    """
    if nums == []:
        return []
    else:
        pivot = nums[0]
        smaller = qsort([x for x in nums[1:] if x<pivot])
        larger = qsort([x for x in nums[1:] if x >= pivot])

        return smaller+[pivot]+larger


if __name__ == '__main__':

    nums = [5,6,78,9,0,-1,2,3,-65,12]
    print qsort(nums)

