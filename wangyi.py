#encoding=utf8
import sys

n = int(sys.stdin.readline().strip())
x = (map(int, sys.stdin.readline().strip().split()))
y = (map(int, sys.stdin.readline().strip().split()))
g = map(int, sys.stdin.readline().strip().split())
time = map(int, sys.stdin.readline().strip().split())
gx = g[0]
gy = g[1]
walkTime = time[0]
taxiTime = time[1]
minTime = walkTime*abs(gx)+walkTime*abs(gy)
for i in range(n):
    xi = x[i]
    yi = y[i]
    Timei = abs(0-xi)*walkTime + abs(0-yi)*walkTime
    Timei += abs(gx-xi)*taxiTime + abs(gy-yi)*taxiTime
    if Timei<minTime:
        minTime = Timei
print minTime