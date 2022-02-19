from collections import defaultdict


class Solution:

    def groupAnagrams_sln1(self, strs: List[str]) -> List[List[str]]:
        '''
        time: o(n*k*logk) where N=number of words, K=size of longest word
        space: o(n*k)
        '''
        charset_to_word = defaultdict(list)

        for word in strs:
            charset = ''.join(sorted(word))
            charset_to_word[charset].append(word)

        return charset_to_word.values()

    def groupAnagrams(self, strs):
        '''
        time: o(n*k) where N=number of words, K=size of longest word
        space: o(n*k)
        '''
        bitmap_to_word = defaultdict(list)

        ALPHABET_SIZE = 26

        for word in strs:
            bitmap = [0] * ALPHABET_SIZE
            for char in word:
                bitmap[ord(char) - ord('a')] += 1
            bitmap_to_word[tuple(bitmap)].append(word)

        return bitmap_to_word.values()

