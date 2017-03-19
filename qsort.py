#encoding=utf8

import gensim, logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
def qsort(nums):
    """
    快速排序,从小到大排序
    :param nums:
    :return:
    """
    if nums == []:
        return []
    else:
        pivot = nums[0]
        smaller = qsort([x for x in nums[1:] if x<pivot])
        larger = qsort([x for x in nums[1:] if x >= pivot])

        return smaller+[pivot]+larger


def qsort1(nums):
    if len(nums) <=1:
        return  nums
    else:
        pivot = nums[0]
        s = qsort1([x for x in nums if x < pivot])
        m = qsort1([x for x in nums if x ==pivot])
        l = qsort1([x for x in nums[1:] if x > pivot])
        return s+m+l

if __name__ == '__main__':

    nums = [5,6,78,9,0,-1,2,3,-65,12]
    print qsort1(nums)



    sentences = [['first', 'sentence'], ['second', 'sentence']]
    # train word2vec on the two sentences
    model = gensim.models.Word2Vec(sentences, min_count=1)
    print model