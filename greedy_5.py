#encoding=utf8

def Solution(n,weight):
    """
    :param n:
    :param weight:
    :return:
    """
    weightQueue = sorted(weight)
    while len(weightQueue)>1:
        stone1 = weightQueue.pop(0)
        stone2 = weightQueue.pop(0)
        weightQueue.append(stone1+stone2)
        weightQueue = sorted(weightQueue)

    print weightQueue[0]
    return weightQueue[0]
n= 10
weight = []
Solution(n,weight)