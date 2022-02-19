class Solution(object):

    def _isPalindrome(self, s, start_index, end_index):
        if self.dp[start_index][end_index] != -1:
            return self.dp[start_index][end_index]

        if not start_index <= end_index:
            return True

        if s[start_index] != s[end_index]:
            self.dp[start_index][end_index] = False
            return False

        result = self._isPalindrome(s, start_index+1, end_index-1)

        self.dp[start_index][end_index] = result
        return result

    def longestPalindrome(self, s):
        """
        :type s: str  --- Input string
        :rtype: str   --- Longest palindrome substring
        """

        '''
        logic:
            * two pointers: start, end
            * if s[start] == s[end] narrow down problem into s[start+1], s[end+1] with help of DP.
            * record longest palindrome starting point & length. 
        '''

        n = len(s)
        #self.dp = [[-1] * n] * n
        self.dp = [[-1] * n for _ in range(n)]


        for i in range(n):
            self.dp[i][i] = True

        longest_palindrome_length = 1
        longest_palindrome_start = 0
        for start_index in range(0, n):
            for end_index in range(n-1, start_index-1, -1):  # end goes backwards until start_index (exclusive)
                #print("StartIndex: %s, EndIndex: %s" % (start_index, end_index))
                #print("DP: \n%s\n" % self.dp)
                if self._isPalindrome(s, start_index, end_index):
                    #print("[ISPALINDROME!] StartIndex: %s, EndIndex: %s" % (start_index, end_index))
                    palindrome_length = (end_index - start_index) + 1
                    if palindrome_length > longest_palindrome_length:
                        longest_palindrome_length = palindrome_length
                        longest_palindrome_start = start_index

        #print("LongestStart: %s, LongestLength: %s" % (longest_palindrome_start, longest_palindrome_length))
        return s[longest_palindrome_start:(longest_palindrome_start+longest_palindrome_length)]


if __name__ == '__main__':
    s = 'aba'
    print("Input: %s, Output: %s" % (s, Solution().longestPalindrome(s)))

    s = 'babad'
    print("Input: %s, Output: %s" % (s, Solution().longestPalindrome(s)))

    s = ''
    print("Input: %s, Output: %s" % (s, Solution().longestPalindrome(s)))

    s = 'cbbd'
    print("Input: %s, Output: %s" % (s, Solution().longestPalindrome(s)))