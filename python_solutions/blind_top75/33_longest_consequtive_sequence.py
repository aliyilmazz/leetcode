class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1

        while left < right:
            left_char, right_char = s[left], s[right]
            while not left_char.isalnum() and left < right:
                left += 1
                left_char = s[left]

            while not right_char.isalnum() and left < right:
                right -= 1
                right_char = s[right]

            if not left < right:
                return True

            #print("leftchar, rightchar: %s %s" % (left_char, right_char))
            if left_char.lower() != right_char.lower():
                return False

            left += 1
            right -= 1

        return True



if __name__ == '__main__':
    text = "A man, a plan, a canal: Panama"
    output = Solution().isPalindrome(text)
    print("output: %s" % output)