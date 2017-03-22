#encoding=utf8

nums = [−2, −5, 6, −2, −3, 1, 5, −6]


def getLargeCrossSum(nums,start,end):

	if start == end :

		return nums[start]
	mid = (start+end)/2
	lsum = 0
	for i in range(mid,start-1,-1):
		lsum += nums[i]
		if lsum >
