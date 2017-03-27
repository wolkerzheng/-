#encoding=utf8

from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        使用队列进行计算
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # wordList.append(endWord)
        wordQueue= deque([[beginWord,1]])
        while wordQueue:
            tmpWord,length = wordQueue.popleft()
            if tmpWord == endWord:
                return length
            else:
                for i in range(len(tmpWord)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = tmpWord[:i]+c+tmpWord[i+1:]
                        if newWord in wordList:
                            wordQueue.append([newWord,length+1])
                            wordList.remove(newWord)
        return 0


if __name__ == '__main__':

    s = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    print s.ladderLength(beginWord, endWord, wordList)