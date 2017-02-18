#encoding=utf8

import re

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        alphabet = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        resList = []
        for word in words:
            w = set(word.lower())
            if w.issubset(alphabet[0]) or w.issubset(alphabet[1])or w.issubset(alphabet[2]):
                resList.append(word)

        return  resList

    def findWords1(self, words):
        return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)

if __name__ == '__main__':

    s = Solution()

    reslist = s.findWords(["Hello", "Alaska", "Dad", "Peace"])

    for res in reslist:
        print res