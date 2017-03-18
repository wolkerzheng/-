#encoding=utf8
__author__ = 'ZGD'

#encoding=utf8
import sys
def main():
    """
    集福卡：10001
    :return:
    """
    str = sys.stdin.readline().strip()
    tdict = {}
    # print dict
    while str!=None:
        if len(str)!=5: break
        for i in range(len(str)):
            tdict[i] = tdict.get(i,0) + int(str[i])
        str = sys.stdin.readline().strip()
    sortedDict = sorted(tdict.items(),key=lambda item:item[1])
    # print sortedDict
    print sortedDict[0][1]


def postfixCalc(str):
    """
    后缀表达式
    :param str:
    :return:
    """
    ops = ['+','-','*']
    numDict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    # print numDict
    # calstack = []
    # for s in str:
    #     if s not in ops:
    #         calstack.append(numDict[s])
    #     else:
    #         m = calstack.pop()
    #         n = calstack.pop()
    #         if s == '+':
    #             calstack.append(m+n)
    #         elif s == '-':
    #             calstack.append(m-n)
    #         else:
    #             calstack.append(m*n)
    # return calstack.pop()
    claStack = [numDict[s.strip()] for s in str if s.strip() not in ops]
    opsStack = [s.strip() for s in str if s.strip() in ops]
    while opsStack!=[]:
        op = opsStack.pop(-1)
        n = claStack.pop(-1)
        m = claStack.pop(-1)
        if op == '+':
            claStack.append(m+n)
        elif op == '-':
            claStack.append(m-n)
        else:
            claStack.append(m*n)
    return claStack.pop()
def Main():
    """
    求能够构造的最大数组
    :return:
    """
    nums = raw_input()

    num = nums.strip().split(' ')
    for i in range(len(num)):
        tmp = num[i][::-1]
            # print tmp
        if long(tmp)>long(num[i]):
            num[i] = tmp
    num = sorted(num)
        # print num
    while len(num)> 1:
           n1 = num.pop()
           n2 = num.pop()
           if (n1+n2) > (n2+n1):
               num.append(n1+n2)
           else:
               num.append(n2+n1)

    sys.stdout.write(num[0])
Main()
# str = sys.stdin.readline().strip()
# print postfixCalc(str)