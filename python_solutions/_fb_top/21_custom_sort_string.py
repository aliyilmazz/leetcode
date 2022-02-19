class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        m, n = len(matrix), len(matrix[0])

        groups = defaultdict(list)

        for i in range(m):
            for j in range(n):
                groups[i - j].append(matrix[i][j])

        # for group in groups.values():
        #    print("group: %s" % group)

        return all([len(set(group)) == 1 for group in groups.values()])