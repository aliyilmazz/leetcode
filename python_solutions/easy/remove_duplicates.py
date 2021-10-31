class Solution(object):

    @staticmethod
    def shiftList(nums, start_index, shift_len):
        # list of 40 elements, start at 24, shift by 6

        def _yield_window_size():
            window_size = 0
            temp_start_index = start_index
            while temp_start_index<len(nums) and nums[temp_start_index]!='_':
                window_size +=1
                temp_start_index += 1
            return window_size

        window_size = _yield_window_size()
        #print("window size:%s" % window_size)
        start_point = start_index - shift_len
        #print("nums before fix:%s" % nums)
        shift_counter = 0
        temp_start_point = start_point
        #print("startpoint:%s" % start_point)
        while shift_counter<window_size:
            #print("tempsp:%s, tempsp+ws:%s" % (temp_start_point, temp_start_point+window_size))
            nums[temp_start_point] = nums[temp_start_point+shift_len]
            shift_counter+=1
            temp_start_point+=1
            #print("nums during fix:%s" % nums)
        #print("nums after fix:%s" % nums)
        array_garbage_collector_index = temp_start_point
        array_garbage_collector_counter = 0
        while array_garbage_collector_counter<shift_len:
            nums[array_garbage_collector_index] = '_'
            array_garbage_collector_index+=1
            array_garbage_collector_counter+=1

        return nums


    @staticmethod
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0

        if nums==[]:
            return 0
        if len(nums) == 1:
            return 1

        # iterate until end of array
        while i<len(nums)-1:
            #print("[index:%s] starting... array: %s" % (i, nums))

            # if you see underscore, it means we reach at the end of list.
            if nums[i] == '_':
                #print("[index:%s] TERMINATING_IF_CASE: this index has underscore, terminating with k=%s" % (i, i))
                return i

            current_number = nums[i]
            next_number = nums[i+1]

            #print("[index:%s] current number:%s, next_number:%s" % (i, current_number, next_number))

            # at this point, we have same numbers in `i` and `i+1`
            temp_number_of_duplicates = 0
            temp_duplicate_detector_index = i+1
            while nums[temp_duplicate_detector_index] == current_number:
                temp_duplicate_detector_index += 1
                temp_number_of_duplicates += 1
                if temp_duplicate_detector_index>=len(nums):
                    break

            #print("[index:%s] # of duplicates:%s" % (i, temp_number_of_duplicates))
            if temp_number_of_duplicates == 0:
                i+=1
                continue
            else:
                #print("[index:%s] reshaping the list..." % i)
                #print("start_index:%s, shiftlen:%s" % (i+temp_number_of_duplicates+1, temp_number_of_duplicates))
                Solution.shiftList(nums=nums, start_index=i+temp_number_of_duplicates+1, shift_len=temp_number_of_duplicates)
                # start_point = i+1
                # last_point = len(nums) - (1 + number_of_duplicates)
                # replacement_iterator = start_point
                # while replacement_iterator<last_point:
                #     #print("[index:%s] (%s->%s) old list: %s" % (i, replacement_iterator, replacement_iterator+temp_number_of_duplicates, nums))
                #     nums[replacement_iterator] = nums[replacement_iterator+temp_number_of_duplicates]
                #     print("[index:%s] (%s->%s) new list: %s" % (i, replacement_iterator, replacement_iterator+temp_number_of_duplicates, nums))
                #     replacement_iterator += 1
                # array_garbage_collector_index = last_point
                # array_garbage_collector_counter = 0
                # while array_garbage_collector_counter < temp_number_of_duplicates:
                #     print("[index:%s] old list: %s" % (i, nums))
                #     nums[array_garbage_collector_index] = '_'
                #     print("[index:%s] new list: %s" % (i, nums))
                #     array_garbage_collector_index+=1
                #     array_garbage_collector_counter+=1
                i+=1

        #print("OUT_OF_LOOP. returning with k=%s" % (clear_indices+1))
        if i<len(nums) and nums[i]!='_':
            i+=1
        return i


# --- test cases start ---
# assert Solution.shiftList([1,1,1,2], 3, 2) == [1, 2, '_', '_']
# assert Solution.shiftList([1,1,2], 2, 1) == [1, 2, '_']
# assert Solution.shiftList([1,1,2,2,2,2,3], 2, 1) == [1, 2, 2, 2, 2, 3, '_']
# nums_1 = [1,1,2]
# Solution.removeDuplicates(nums_1)
# assert nums_1 == [1, 2, '_']
# nums_2 = [0,0,1,1,1,2,2,3,3,4]
# Solution.removeDuplicates(nums_2)
# assert nums_2 == [0, 1, 2, 3, 4, '_', '_', '_', '_', '_']
# nums_3 = []
# Solution.removeDuplicates(nums_3)
# assert nums_3 == []
# --- test cases end ---



#nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,1]
print("input nums: %s" % nums)
k = Solution.removeDuplicates(nums)
print("new nums: %s" % nums)
print("k: %s" % k)
