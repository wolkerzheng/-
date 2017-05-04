#encoding=utf8
"""
dynamic programing:

"""
x = 'aab'
y = 'adgabsdf'

def LSC(x,y):
	"""

	largest common sub sequence

	"""
	l1 = len(x)
	l2 = len(y)
	if l1==0 or l2 == 0:
		return 0
	else:
		if x[-1] == y[-1]:
			return LSC(x[:-1],y[:-1])+1

		else:
			left = LSC(x[:-1],y)
			right = LSC(x,y[:-1])
			return max(left,right)
def lcs(x,y):
	m = len(x)
	n = len(y)
	print m,n
	# store the length of  largest common sub sequence
	c = [[0 for _ in range(n+1)] for _ in range(m+1)]
	# 1 represent: xieduijiao; 2 : xiangshang; 3:xiangzuo;
	B = [[0 for _ in range(n+1)] for _ in range(m+1)]
	for i in range(1,m+1):
		for j in range(1,n+1):
			if  x[i-1] == y[j-1]:
				c[i][j] = c[i-1][j-1]+1
				B[i][j] = 1
			elif c[i-1][j]>c[i][j-1]:
				c[i][j] = c[i-1][j]
				B[i][j] = 2
			else:
				c[i][j] = c[i][j-1]
				B[i][j] = 3
	return B,c
def printB(B,x,i,j):

	if i==0 or j==0:
		return ""
	if B[i][j] ==1:
		printB(B,x,i-1,j-1)
		print x[i-1]
	elif B[i][j] == 2:
		printB(B,x,i-1,j)
	else:
		printB(B,x,i,j-1)
	

def largestCommonSubString(x,y):
	"""

	"""
	m,n = len(x), len(y)
	c = [[0 for  _ in range(n+1)] for _ in range(m+1)]
	for i in range(1,m+1):
		for j in range(1,n+1):
			if x[i-1] ==y[j-1]:
				c[i][j] = c[i-1][j-1] + 1
	return c
m = raw_input()
print m
b,c = lcs(x,y)
print 'common sub sequence:'
printB(b,x,len(x),len(y))
print 'largest common sub sequense is:',c[len(x)][len(y)]

largestCommonSubString(x,y)