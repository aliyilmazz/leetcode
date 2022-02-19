class Solution:

    def customSortString(self, order: str, s: str) -> str:
        char_score = defaultdict(int)
        n = len(order)

        for precedence, char in enumerate(order):
            char_score[char] = -(n - precedence - 1)

        s = sorted(s, key=lambda x: char_score[x])
        return ''.join(s)


class Solution_naive:
    def customSortString_naive(self, order: str, s: str) -> str:
        counter = Counter(s)
        ordered_string = []

        # print("counter:%s" % counter)
        for char in order:
            if char in counter:
                # print("char %s found in counter! adding %s times" % (char, counter[char]))
                [ordered_string.append(char) for _ in range(counter[char])]
                del counter[char]

        for char, occurrence in counter.items():
            [ordered_string.append(char) for _ in range(occurrence)]

        return ''.join(ordered_string)