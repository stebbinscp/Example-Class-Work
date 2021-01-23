# Problem 10
#
# Before you get busy typing, stop for a moment and think about the
# all the different ways you can solve the following problems. There are 
# some approaches that will take significantly less time and lines of code 
# to implement. 
# 
# Strive for code efficiency. You may disregard the time complexity when 
# choosing your solution. 

  
# A. 
# Complete the function below so that it removes duplicates from an 
# unsorted list.  
def remove_duplicates(unsorted_list):
    """Removes duplicates in a list"""
    for item in unsorted_list:
        unsorted_list = sorted(unsorted_list) # sorts as needed in the assertations
        if unsorted_list.count(item) > 1: # finds if something is a duplicate
            unsorted_list.remove(item) # remove anything found more than once
    return unsorted_list

# print(remove_duplicates([10, 12, 11, 11, 12, 11, 10]))

# Use the following assertions to test your implementation
assert [10, 11, 12] == remove_duplicates([10, 12, 11, 11, 12, 11, 10])
assert [1, 2] == remove_duplicates([1, 1, 2, 2])



# B.
# Complete the function below to find the common items shared between two 
# lists. After processing, the function should return a single list cotaining 
# all the common items.
# #
# list1 = [11, 21, 23, 5, 59]
# list2 = [5, 11, 27, 38, 59]

def find_common_items(list1, list2):
    """Finds common items in a list"""
    list3 = []
    for i in range(0,len(list1)):
        # print(item)
        if list1[i] in list2: # if there is a common item
            # print(item)
            list3.append(list1[i]) #append it to the list
    return list3 # unsorted to account for the assert statements

# print(find_common_items(list1,list2))

# # # Use the following assertions to test your implementation
assert [1, 2] == find_common_items([1,2,3], [1,2,4,5])
assert [11, 5, 59] == find_common_items([11, 21, 23, 5, 59], [5, 11, 27, 38, 59])
