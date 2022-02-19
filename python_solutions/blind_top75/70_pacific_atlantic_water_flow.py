import heapq
from collections import Counter


class Solution:
    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        '''
        occurency dict o(n)
        iterate dict o(n)
        add to minheap
        '''

        counter = Counter(nums)
        occurrence_heap = []
        heapq.heapify(occurrence_heap)
        for num in counter.keys():
            # insert: logn
            heapq.heappush(occurrence_heap, (counter[num] * -1, num))
        # overall: nlogn

        results = []
        for _ in range(k):
            results.append(heapq.heappop(occurrence_heap)[1])

        return results

    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        keys = list(counter.keys())
        n = len(keys)

        def partition(left, right, pivot_index):
            pivot_frequency = counter[keys[pivot_index]]
            keys[pivot_index], keys[right] = keys[right], keys[pivot_index]

            store_index = left
            for i in range(left, right + 1):
                element_frequency = counter[keys[i]]
                if element_frequency < pivot_frequency:
                    keys[store_index], keys[i] = keys[i], keys[store_index]
                    store_index += 1

            keys[store_index], keys[right] = keys[right], keys[store_index]
            return store_index

        def quickselect(left, right, k):
            '''
            sort a list within left..right 
            until Kth less requent element takes its place
            '''

            # base case
            if left == right:
                return

            pivot_index = random.randint(left, right)

            #  find pivot index in sorted list
            pivot_index = partition(left, right, pivot_index)

            if pivot_index == k:
                return

            elif pivot_index < k:
                quickselect(pivot_index + 1, right, k)

            else:
                quickselect(left, pivot_index - 1, k)

        quickselect(0, n - 1, n - k)
        return keys[n - k:]
