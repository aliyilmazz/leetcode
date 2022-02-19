class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:

        scores = defaultdict(int)
        n = len(order)
        for precedence, char in enumerate(order):
            scores[char] = (n - precedence)  # higher score = more precedence

        def compare_strings(str1, str2):
            ptr_1, ptr_2 = 0, 0
            while 0 <= ptr_1 < len(str1) and 0 <= ptr_2 < len(str2) and str1[ptr_1] == str2[ptr_2]:
                ptr_1 += 1
                ptr_2 += 1

            if ptr_1 >= len(str1) or ptr_2 >= len(str2):
                if ptr_1 < len(str1) and ptr_2 >= len(str2):
                    return False
                return True

            return scores[str1[ptr_1]] > scores[str2[ptr_2]]

        for str1, str2 in zip(words[:-1], words[1:]):
            print("%s %s" % (str1, str2))
            if not compare_strings(str1, str2):
                print("%s %s not ordered. returning false" % (str1, str2))
                return False
            else:
                print("%s %s ordered" % (str1, str2))

        return True