class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        transform input into groups
        iterate groups, take min for each pair
        """

        if not s:
            return 0

        groups = []
        mode = s[0]
        streak = 1
        for _char in s[1:]:
            if _char == mode:
                streak += 1
            else:
                groups.append(streak)
                streak = 1
                mode = _char

        groups.append(streak)
        print("groups: %s" % groups)

        #---- groups formed ----#

        count = 0
        for _index in range(len(groups)-1):
            count += min(groups[_index], groups[_index+1])

        return count






if __name__ == '__main__':
    input = "00110011"
    output = Solution().countBinarySubstrings(input)
    print("Input:%s\nOutput:%s" % (input, output))



