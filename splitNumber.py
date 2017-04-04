#encoding=utf8
"""
g(i,j) = g(i,j-1)+g(i-j,j)

苹果分盘子问题。把M个同样的苹果放在N个同样的盘子里，
允许有的盘子空着不放，问共有多少种不同的分法？

2.整数
i=1:g(i,j) = 1
j = 1,g(i,j) = 1
"""


def splitNum(num,m):
	"""

	"""
	g = [[0 for _ in range(m+1)] for _ in range(num+1)]

	for i in range(num+1):
		# g[i][0] = 0
		g[i][1] = 1
	for i in range(1,m+1):
		g[1][i] = 1
		# g[0][i] = 0

	for i in range(1,num+1):

		for j in range(1,m+1):
			if i>=j:
				g[i][j] = g[i-j][j]+g[i][j-1]
			else:
				g[i][j] = g[i][i]+1		#j>i,表示i
				break
	# print g
	return g[num][m]

num = 7
m = 3
print splitNum(num,m)