#encoding=utf8

import time
def selectGasStation(N,gas,cost):
    """
    :param n: 加油站个数
    :param gas: 每个加油站的汽油
    :param cost: 每个加油站到下站的耗油量
    :return:
    """
    rest = [0]*N    #初始化一个长度为N的0数组
    for i in xrange(N):
        rest[i] = gas[i]-cost[i]
    startStation = 0
    oil,total = 0,0
    for i in range(N):
        oil += rest[i]
        total += rest[i]
        if oil<0:
            startStation = i+1
            oil = 0
    return -1 if total<0 else startStation

N = 4
gas,cost = [1, 1, 3, 1],[2, 2, 1, 1]
print '选择的开始站点为：',selectGasStation(N,gas,cost)