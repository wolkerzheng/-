#encoding=utf8
"""
01背包的状态转换方程 f[i,j] = Max{ f[i-1,j-Wi]+Pi( j >= Wi ),  f[i-1,j] }
f[i,j]表示在前i件物品中选择若干件放在承重为 j 的背包中，可以取得的最大价值。
Pi表示第i件物品的价值。
"""
def main(weights,vals,backpack):

	n = len(weights)	#背包数
	f = [[0 for _ in range(backpack+1)]for _ in range(n+1)]

	for i in range(1,n+1):

		for j in range(0,backpack+1):
			if j<weights[i-1]:
				f[i][j] = f[i-1][j]
			else:
				f[i][j] = max(f[i-1][j],f[i-1][j-weights[i-1]]+vals[i-1])

	print f
	print f[n][backpack]
	pass

if __name__ == '__main__':
	weights = [2, 1, 3, 2]
	vals = [3, 2, 4, 2]
	backpack = 4
	main(weights,vals,backpack)