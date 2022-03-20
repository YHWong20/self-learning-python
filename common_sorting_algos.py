# Common Sorting Algorithms

# Mergesort
def merge_sort(lst):
# Logic:
# 1) Recursively split list into single lists
# 2) Merge single lists together

    midpoint = len(lst) // 2
    if len(lst) <= 1:
        return lst
    
    L = merge_sort(lst[:midpoint])
    R = merge_sort(lst[midpoint:])

    sorted_arr = []
    while L and R:
        if L[0] > R[0]:
            sorted_arr.append(R.pop(0))
        else:
            sorted_arr.append(L.pop(0))
    sorted_arr.extend(R)
    sorted_arr.extend(L)

    return sorted_arr


# Selection Sort
def selection_sort(lst):
# Logic: Select smallest value, pop it and append to new array

    new_arr = []
    while lst:
        smallest = 0
        for i in range(smallest + 1, len(lst)):
            if lst[smallest] > lst[i]:
                smallest = i
        new_arr.append(lst.pop(smallest))
        smallest += 1
    return new_arr

def selection_sort_ip(lst):
# In-place, Space O(1)

    for i in range(len(lst)):
        smallest = i
        for j in range(i + 1, len(lst)):
            if lst[smallest] > lst[j]:
                smallest = j
        lst[i], lst[smallest] = lst[smallest], lst[i]
    return lst


# Insertion Sort(?) - Not sure how correct the first 2 ones are
def insertion_sort(lst):
    new_arr = [lst.pop(0)]
    while lst:
        for i in range(len(new_arr)):
            if not lst:
                break
            if lst[0] < new_arr[i]:
                new_arr.insert(i, lst.pop(0))
            if i == len(new_arr) - 1:
                new_arr.append(lst.pop(0))
    return new_arr

def insertion_sort_ip(lst):
    for i in range(1, len(lst)):
        for j in range(len(lst[:i])):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

def insertion_sort_ref(lst):
# Logic: Inserting elements in the correct indexes, first element assumed to be sorted

    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst  
            

# Bubble Sort
def bubble_sort_ip(lst):
# Logic: Pushes largest value to the end of the array
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


# Tree Sort





    
#TREE sort too, using binary tree)

# Also include searching algorithms
