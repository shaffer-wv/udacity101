# quick sort implementation for udacity cs101
# using minimal built in methods as possible. Also
# starts pivot at postion 0 which is not ideal

def quick_sort(alist):
	    if len(alist) <= 1:
	        return alist
	    else:
	        pivot = alist[0]
	        lesser = []
	        greater = []
	        for num in alist[1:]:
	            if num < pivot:
	                lesser.append(num)
	            else:
	                greater.append(num)
	        return quick_sort(lesser) + [pivot] + quick_sort(greater)
					
