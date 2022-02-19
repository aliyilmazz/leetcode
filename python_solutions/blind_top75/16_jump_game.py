from typing import List


class Solution:
    def spiralOrder_selfsoln(self, matrix: List[List[int]]) -> List[int]:

        visited_coords = set()

        m = len(matrix)  # col length (row count)
        n = len(matrix[0])  # row length

        traverser_x = 0
        traverser_y = 0

        elements = []

        while tuple([traverser_x, traverser_y]) not in visited_coords \
                and 0 <= traverser_x < m and 0 <= traverser_y < n:
            print("beginning of loop!")
            while tuple([traverser_x, traverser_y]) not in visited_coords \
                    and 0 <= traverser_x < m and 0 <= traverser_y < n:

                elements.append(matrix[traverser_x][traverser_y])
                visited_coords.add(tuple([traverser_x, traverser_y]))
                print("adding x y [%s, %s]" % (traverser_x, traverser_y))
                traverser_y += 1

            traverser_y -= 1
            traverser_x += 1

            while tuple([traverser_x, traverser_y]) not in visited_coords \
                    and 0 <= traverser_x < m and 0 <= traverser_y < n:

                elements.append(matrix[traverser_x][traverser_y])
                visited_coords.add(tuple([traverser_x, traverser_y]))
                print("adding x y [%s, %s]" % (traverser_x, traverser_y))
                traverser_x += 1

            traverser_x -= 1
            traverser_y -= 1

            while tuple([traverser_x, traverser_y]) not in visited_coords \
                    and 0 <= traverser_x < m and 0 <= traverser_y < n:

                elements.append(matrix[traverser_x][traverser_y])
                visited_coords.add(tuple([traverser_x, traverser_y]))
                print("adding x y [%s, %s]" % (traverser_x, traverser_y))
                traverser_y -= 1

            traverser_y += 1
            traverser_x -= 1

            while tuple([traverser_x, traverser_y]) not in visited_coords \
                    and 0 <= traverser_x < m and 0 <= traverser_y < n:

                elements.append(matrix[traverser_x][traverser_y])
                visited_coords.add(tuple([traverser_x, traverser_y]))
                print("adding x y [%s, %s]" % (traverser_x, traverser_y))
                traverser_x -= 1

            traverser_x += 1
            traverser_y += 1

        return elements


    def spiralOrder_boundaries(self, matrix: List[List[int]]) -> List[int]:
        elements = []

        def populate():
            m, n = len(matrix), len(matrix[0])
            up_index = 0
            left_index = 0
            right_index = n - 1
            down_index = m - 1

            visited_coords = set()

            while len(elements) < m*n:
                # left to right
                for col in range(left_index, right_index+1):
                    print("right: x y [%s %s]" % (up_index, col))
                    if tuple([up_index, col]) in visited_coords:
                        print("tuple already exists!")
                        return
                    visited_coords.add(tuple([up_index, col]))
                    elements.append(matrix[up_index][col])

                up_index += 1
                # top to bottom
                for row in range(up_index, down_index+1):
                    print("down: x y [%s %s]" % (row, right_index))
                    if tuple([row, right_index]) in visited_coords:
                        print("tuple already exists!")
                        return
                    visited_coords.add(tuple([row, right_index]))
                    elements.append(matrix[row][right_index])

                right_index -= 1
                for col in range(right_index, left_index-1, -1):
                    print("left: x y [%s %s]" % (down_index, col))
                    if tuple([down_index, col]) in visited_coords:
                        print("tuple already exists!")
                        return
                    visited_coords.add(tuple([down_index, col]))
                    elements.append(matrix[down_index][col])

                down_index -= 1
                for row in range(down_index, up_index-1, -1):
                    print("up: x y [%s %s]" % (row, left_index))
                    if tuple([row, left_index]) in visited_coords:
                        print("tuple already exists!")
                        return
                    visited_coords.add(tuple([row, left_index]))
                    elements.append(matrix[row][left_index])

                left_index += 1

        populate()
        return elements


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        VISITED = 101
        m = len(matrix)
        n = len(matrix[0])

        # four directions that we will move
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_direction_index = 0

        # number of times we change direction
        change_direction_count = 0

        row_index = col_index = 0

        elements = [matrix[0][0]]
        matrix[0][0] = VISITED

        while change_direction_count < 2:

            while True:
                next_row = row_index + directions[current_direction_index][0]
                next_col = col_index + directions[current_direction_index][1]

                if not ((0 <= next_row < m) and (0 <= next_col < n)):
                    break

                print("row col: %s %s" % (next_row, next_col))
                if matrix[next_row][next_col] == VISITED:
                    break

                change_direction_count = 0

                row_index, col_index = next_row, next_col
                elements.append(matrix[row_index][col_index])
                matrix[row_index][col_index] = VISITED

            # change direction
            current_direction_index += 1
            current_direction_index %= 4

            change_direction_count += 1

        return elements

if __name__ == '__main__':
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    #matrix = [[1]]
    elements = Solution().spiralOrder(matrix)
    print("elements: %s" % elements)