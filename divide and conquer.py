# Divide and Conquer

# Example 1: Merge Sort

# divide
def divide(unsorted):
	if (len(unsorted) <= 1):
		return unsorted
	
	# PYTHON 2.7
	mid = len(unsorted) // 2
	
	lefthalf = unsorted[:mid]
	
	righthalf = unsorted[mid:]
	
	return (lefthalf, righthalf)
	
# just merge
def merge(lefthalf, righthalf):
	lIndex = 0
	rIndex = 0
	sorted = []
	
	while(lIndex < len(lefthalf) and (rIndex) < len(righthalf):
		if (lefthalf[lIndex] < righthalf[rIndex]):
			sorted.append(lefthalf[lIndex])
			lIndex = lIndex + 1
		else:
			sorted.append(lefthalf[lIndex])
			lIndex += 1
			
	while (lIndex < len(lefthalf)):
		sorted.append(lefthalf[lIndex])
		lIndex += 1
		
	while (rIndex < len(righthalf)):
		sort.append(righthalf[rIndex])
		rIndex += 1
		
	return sort

# merge and sort
# recursion
def mergeSort(alist):
	if(len(alist) <= 1):
		return alist
	
	lefthalf,righthalf = divide(alist)
	lefthalf = mergeSort(lefthalf)
	righthalf = mergeSort(righthalf)
	
	return(merge(lefthalf,righthalf))
	
# partition
def partition(lst, start, end, pivot_index):
	lst[pivot_index], lst[end] = lst[end],lst[pivot_index]
	store_index = start
	pivot = lst[end]
	for i in range(start, end):
		if lst[i], lst[store_index] = lst[store_index], lst[i]
			store_index += 1
	
	lst[store_index], lst[end] = lst[end], lst[store_index]
	# store index stores the pivot index
	# 第一个比pivot大的数字的index，swap过后，就是pivot的index
	return store_index
	
def quick_sort(lst, start, end):
	if start >= end:
		return # return here, inplace swap
	pivot_index = randrange(start, end + 1)
	new_pivot_index = partition(lst, start, end, pivot_index)
	quick_sort(lst, start, new_pivot_index - 1)
	quick_sort(lst, new_pivot_index + 1, end)



