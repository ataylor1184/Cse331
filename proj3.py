def merge_sort(unsorted, threshold, reverse):
    """
        Conducts a merge sort on a unsorted list, uses insertion sort if list
        size is below threshold value
        :return: returns the unsorted list as base case, recursively calls
        itself with smaller lists otherwise
    """
    temp= len(unsorted)
    if temp< threshold:
        return insertion_sort(unsorted, False)
    elif temp< 2:
        return unsorted #list is already sorted
    mid = temp//2
    left = unsorted[0:mid]
    right = unsorted[mid:temp]
    if reverse == False:
        left = merge_sort(left, threshold, reverse)
        right = merge_sort(right, threshold, reverse)
    if reverse == True:
        left = merge_sort(left, threshold, False)
        right = merge_sort(right, threshold, False)
    return merge(left ,right, reverse)

def merge(first, second, reverse):
    """
        Merges two lists together either in ascending order if reverse is True,
        or descending order if reverse is False
        :return: returns the merged list
    """
    merge_list = []
    if reverse == False:
        j = 0
        i = 0
        while i != len(first) and j != len(second):
            if first[i] < second[j]: #merging the bulk of the 2 lists
                merge_list.append(first[i])
                i +=1
            else:
                merge_list.append(second[j])
                j += 1
        while i == len(first) and j != len(second):
            merge_list.append(second[j]) #appends rest of first if all of second is added
            j += 1
        while i != len(first) and j == len(second):
            merge_list.append(first[i]) #appends rest of second if all of first is added
            i += 1
    else:
        j = len(second) - 1
        i = len(first) - 1
        while i != -1 and j != -1:
            if first[i] > second[j]: #merging the bulk of the 2 lists
                merge_list.append(first[i])
                i -= 1
            else:
                merge_list.append(second[j])
                j -= 1
        while i == -1 and j != -1:
            merge_list.append(second[j]) #appends rest of first if all of second is added
            j -= 1
        while i != -1 and j == -1:
            merge_list.append(first[i]) #appends rest of second if all of first is added
            i -= 1
    return merge_list

def insertion_sort(unsorted, reverse):
    """
        Conducts a insertion sort on a unsorted list. Ascending order if reverse
        is True, descending otherwise.
        :return: returns a sorted list
    """
    if reverse == False:
        for i in range(1,len(unsorted)):
            temp = unsorted[i]
            j = i-1
            while j >=0 and temp< unsorted[j]:
                unsorted[j+1] = unsorted[j]
                j -= 1
            unsorted[j+1] = temp
    else:
        for i in range(1,len(unsorted)):
            temp = unsorted[i]
            j = i-1
            while j >=0 and temp> unsorted[j]:
                unsorted[j+1] = unsorted[j]
                j -= 1
            unsorted[j+1] = temp
        
    return unsorted
