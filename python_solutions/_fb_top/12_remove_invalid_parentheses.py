'''
a:0, b:1, c:2, d:3, ...

strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
convert = [(0,1,2),(1,2,3),(0,2,5,6),...]
shifted =          (0,1,2)
1. convert each string into a number (a=0, b=1, ...z=25)
2. shift each string so that it starts from 0
3. add into dictionary (key: number pattern (0,1,2), value: list of the original string)
4. output result

'''

from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        converted_strings = []
        for string in strings:
            shift = ord(string[0]) - ord('a')
            converted_string = [(ord(char) - ord('a') - shift) % 26 for char in string]
            print("string: %s, converted: %s" % (string, converted_string))
            converted_strings.append(tuple(converted_string))

        words_dict = defaultdict(list)
        for i, converted_string in enumerate(converted_strings):
            original_string = strings[i]
            words_dict[converted_string].append(original_string)

        return list(list(value) for value in words_dict.values())