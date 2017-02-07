# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
# Use binary search.
# http://www.practicepython.org/exercise/2014/11/11/20-element-search.html
# num = int(input("Enter number to compare with the list: "))

# var1
def number_searcher(lst, num):
    if num in lst:
        return True
    else:
        return False

# var2 (with binary search)
def binary_searcher(lst, num):
    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = int((first + last) / 2)
        if num == lst[mid]:
            return True
        else:
            if num > lst[mid]:
                first = mid+1
            else:
                last = mid-1
    return False
