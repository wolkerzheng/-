#encoding=utf8

def maxWater(n,Heigth):
    """
    :param n: 木板数
    :param Heigth: 木板的高度
    :return: 盛水量最大数
    """
    if Heigth==None:
        return 0
    start,end = 0,n-1
    result = 0
    while start<end:
        area = min(Heigth[start],Heigth[end])*(end-start) #计算当前构成的面积
        result = max(area,result)       #取当前构成的面积和原有最大面积的最大值
        if Heigth[start]>Heigth[end]:   
            end = end -1
        else:
            start = start + 1
    return result



