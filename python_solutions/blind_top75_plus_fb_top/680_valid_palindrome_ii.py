class Solution(object):


    def _validPalindrome(self, s, can_delete_char):

        #rint("[%s] started" % s)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1

            else:  # we have encountered a mismatch
                if not can_delete_char:
                    return False  # we are out of options to exercise a char deletion
                else:  # and we have a right to delete a char
                    if left + 1 <= len(s)-1 and s[left+1] == s[right]:
                        if self._validPalindrome(s[left+1:right+1], can_delete_char=False):
                            return True
                    if right - 1 >= 0 and s[left] == s[right - 1]:
                        if self._validPalindrome(s[left:right], can_delete_char=False):
                            return True
                    # no match found, even if we shift either pointers
                    return False
        return True

    def validPalindrome(self, s):

        '''
            * initialize left and right pointers
            * until they meet each other, check if s[left] == s[right]
            * if there is a mismatch, try using our one-time right to delete a character. if no more trials left, skip.
            * return true if we can make it out of the loop
        '''

        return self._validPalindrome(s, can_delete_char=True)



if __name__ == '__main__':
    s = "aba"
    output = Solution().validPalindrome(s)
    print("Input: %s, Output: %s" % (s, output))

    s = "abca"
    output = Solution().validPalindrome(s)
    print("Input: %s, Output: %s" % (s, output))

    s = "abc"
    output = Solution().validPalindrome(s)
    print("Input: %s, Output: %s" % (s, output))

    s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    output = Solution().validPalindrome(s)
    print("Input: %s, Output: %s" % (s, output))