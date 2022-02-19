from typing import List


def executeQuery(query, boolean_array):
    if query[0] == 1:
        # SET routine
        to_be_modified_index = query[1] - 1  # the array is 1-indexed
        boolean_array[to_be_modified_index] = True
        # (Q: do we return anything for SET operations?)
        return None  # just to be explicit. by default, it already returns None
    elif query[0] == 2:
        # GET routine
        starting_index = query[1]
        get_query_result = -1
        for i in range(starting_index, len(boolean_array)):
            if boolean_array[i]:
                get_query_result = i+1
        return get_query_result


def answerQueries(queries: List[List[int]], boolean_array_length) -> List[int]:

    '''
    prepare a solution array.
    prepare boolean array, initially all set to false.

    (starting from left to right?) execute queries, populate solution array
    return solution array
    '''

    boolean_array = [False] * boolean_array_length
    results = []

    for query in queries:
        # list is mutable (array of pointers), so no problem passing it by reference
        result = executeQuery(query, boolean_array)
        if result:  # ignoring NULL responses (AFAICS, SET queries are not returning anything)
            print("result: %s" % result)
            results.append(result)

    return results


if __name__ == '__main__':
    output = answerQueries([[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]], boolean_array_length=5)
    print("output: %s" % output)
    assert output == [-1, 2, -1, 2]
