#coding=utf-8
import math
"""

"""
def solution(string,start,end):
	# start = 0
	# end = len(string)
	mid = int(math.floor((start + end)/2.0))  
	# print 'mid is ',mid
	# print string[start:end+1]
	if start>= end:
		return 1
		# print string[start]
	else:
		res= 0
		if string[mid:mid+2]<='26' :
			# print string[mid:mid+1]
			res = solution(string,start,mid-1)*solution(string,mid+2,end)
		# print string[mid:mid+1]
		return solution(string,start,mid)*solution(string,mid+1,end)+res
string ="234"
start = 0
end = len(string)-1
print solution(string,start,end)