from typing import List




class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = [log for log in logs if not log.split(" ")[1].isdigit()]
        letter_logs.sort(key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))

        digit_logs = [log for log in logs if log.split(" ")[1].isdigit()]
        #digit_logs.sort(key=lambda x: x.split(" ")[0])

        return letter_logs + digit_logs




if __name__ == '__main__':
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    output = Solution().reorderLogFiles(logs)
    print("Logs:%s\nOutput:%s" % (logs, output))

    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    output = Solution().reorderLogFiles(logs)
    print("Logs:%s\nOutput:%s" % (logs, output))

    logs = ["1 n u", "r 527", "j 893", "6 14", "6 82"]
    output = Solution().reorderLogFiles(logs)
    print("Logs:%s\nOutput:%s" % (logs, output))

    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
    output = Solution().reorderLogFiles(logs)
    print("Logs:%s\nOutput:%s" % (logs, output))

