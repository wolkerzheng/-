#encoding=utf8
import sys

n = int(sys.stdin.readline().strip())
# ans = 0
values = []
for i in range(n):
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values.append(line.strip())

print values