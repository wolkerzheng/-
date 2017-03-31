#encoding=utf8


def func(n):
	if n <=1:
		return 1
	else:
		return func(n-1)+func(n-2)
print func(3)


def climbStairs(n):
	if n<0:
		return 0
	dp = [ 1 for _ in range(n+1)]
	dp[1],dp[2] = 1,2
	for i in range(3,n+1):
		dp[i] = dp[i-1]+dp[i-2]
	return dp[n]


print climbStairs(10)