#!/usr/bin/python
# encoding=utf8

import random as rd
import time
import math
import copy
import matplotlib.pyplot  as plt


class Graph(object):

    def __init__(self, nodenum, weight=False,weightNum=30):

        self.__nodenum = nodenum
        self.__weight = weight
        self.__adjmat = self.__rdCreateGraph()
        self.__weightNum = weightNum

    def __rdCreateGraph(self):
        adjMat = [[0 for _ in xrange(self.__nodenum)] for _ in xrange(self.__nodenum)]
        if not self.__weight:

            # print '随机无向图的邻接矩阵表示'
            N = self.__nodenum *(self.__nodenum-1) / 2
            # 无向连通图至少需要n-1条边
            Linksnum = rd.randint(self.__nodenum, N)
            print '图中节点数：', self.__nodenum
            print '图中边数：', Linksnum
            n = 0
            while n < Linksnum:
                x = rd.randint(0,self.__nodenum-1)
                y = rd.randint(0,self.__nodenum-1)
                if x == y:
                    continue
                if adjMat[x][y] == 0:
                    adjMat[x][y],adjMat[y][x] = 1,1
                    n += 1
            print '随机生成无权无向图：'
            for i in xrange(self.__nodenum):
                for j in xrange(self.__nodenum):
                    print adjMat[i][j],
                print
        else:
            adjMat = [[rd.randint(1,self.__weightNum ) for _ in range(self.__nodenum)] for _ in range(self.__nodenum)]
            for j in range(self.__nodenum):
                adjMat[j][j] = float('inf')
        return adjMat

    def getAdjMat(self):

        return self.__adjmat


class pathNode:
    """
    搜索队列存储的节点信息
    """
    #记录节点路径

    def __init__(self,idx=-1,pathway=None):
        self.idx = idx
        self.pathway = pathway

def isPath(n, pathway):
    """
    是否为一条路径
    :param n:
    :param pathway:
    :return:
    """
    # print 'pathway:',pathway
    for i in range(n):
        if i not in pathway:
            return False
    return True

def isNotVisit(cur,j):
    """
    判断是否访问过该节点j
    :param adjMat: 邻接矩阵
    :param cur:
    :param j:
    :return:
    """

    pw = cur.pathway
    if cur.idx not in pw:
        # print '....'
        return True
    return False

def BFS(root,adjMat,n):
    """
    广度优先遍历
    :param root:
    :param adjMat:
    :param n:
    :return:
    """
    queue = []
    #根节点入队
    queue.append(root)
    while queue:
        cur = queue.pop(0)      #出队列
        # print cur.pathway

        if root.idx == cur.idx and isPath(n, cur.pathway):
            print '广度优先搜索生成路径：',cur.pathway
            return True

        for j in xrange(n):
            if adjMat[cur.idx][j] == 1 and isNotVisit(cur,j) == True:
                way = copy.deepcopy(cur.pathway)
                way.append(cur.idx)
                t = pathNode(j,way)
                queue.append(t)
                # print way

    print 'BFS否'
    return False


def DFS(root,adjMat,n):
    """

    :param root:
    :param adjMat:
    :param n:
    :return:
    """
    stack = []
    stack.append(root)
    while stack!=[]:
        cur = stack.pop(-1)
        if cur.idx == root.idx and isPath(n,cur.pathway):
            print '深度优先搜索生成路径：',cur.pathway
            return True
        for i in xrange(n-1,-1,-1):
            if adjMat[cur.idx][i] == 1 and isNotVisit( cur, i) == True:
                way = copy.deepcopy(cur.pathway)
                way.append(cur.idx)
                tmpNode = pathNode(i, way)
                stack.append(tmpNode)
    print 'DFS否'
    return False

def clibm(start,adjMat,n):

    stack = []
    stack.append(start)

    while stack:
        cur = stack.pop(-1)




    pass

def testH1(n):

    for i in xrange(len(n)):
        g = Graph(n[i])
        adjMat = g.getAdjMat()


        root = pathNode(0,[])
        # print root.idx,root.pathway
        # print '深度优先搜索'
        s1 = time.clock()
        DFS(root,adjMat,n[i])
        s2 = time.clock()
        # print '广度优先搜索：'
        BFS(root,adjMat,n[i])
        s3 = time.clock()
        print 'BFS',s3-s2
        print 'DFS', s2 - s1
        pass


if __name__ == '__main__':
    n = [8, 10, 12, 14, 16, 18, 20]
    # n = [8,8,8,10]
    testH1(n)