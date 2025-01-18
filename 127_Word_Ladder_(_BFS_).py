from string import ascii_lowercase
from collections import deque
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #Idea of BFS
        n = len(beginWord)
        wordList = set(wordList)
        if endWord not in wordList: return 0
        q = deque()
        q.append(beginWord)
        res = set([beginWord])
        # level count numbers of transformation.
        level = 1
        while q:
            nextWords = []
            # Take out all words of next transformation.
            while q:
                nextWords.append(list(q.popleft()))
            level += 1
            for word in nextWords:
                for i in range(n):
                    tmp = word[:]
                    # Replace each position of word by 'a' -> 'z'.
                    for c in ascii_lowercase:
                        tmp[i] = c
                        newWord = ''.join(tmp)
                        if newWord == endWord: return level
                        elif newWord not in res and newWord in wordList:
                            res.add(newWord)
                            q.append(newWord)
        return 0