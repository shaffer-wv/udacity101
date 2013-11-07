# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

def deep_reverse(alist):
    reverse_list = []
    pos = -1
    while pos >= -(len(alist)):
        if is_list(alist[pos]):
            reverse_list.append(deep_reverse(alist[pos]))
        else:
            reverse_list.append(alist[pos])
        pos -= 1
    return reverse_list
		
# answered used below to count through the list backwards instead of my
# while loop
# for i in range(len(alist)-1, -1, -1)
# starts at last element of list
# goes until it stops at 0
# and counts backwards