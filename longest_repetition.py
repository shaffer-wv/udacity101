# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(alist):
    if alist == []:
        return None
    else:
        repeat_element = alist[0]
        current_element = alist[0]
        current_repeats = 0
        long_repeat = 0
        for element in alist:
            if element == current_element:
                current_repeats += 1
            else:
                if current_repeats > long_repeat:
                    long_repeat = current_repeats
                    repeat_element = current_element
                current_element = element
                current_repeats = 1
        if current_repeats > long_repeat:
                    long_repeat = current_repeats
                    repeat_element = current_element
        return repeat_element