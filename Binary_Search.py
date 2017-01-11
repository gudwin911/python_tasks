#Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
#The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
#Use binary search.
#http://www.practicepython.org/exercise/2014/11/11/20-element-search.html
lst = [0,1,2,3,5,8,15,18,27,31,32,35,39,45,47,49,50,52,61,67,77,78,79,81,83,88,89,90,91,98,99]
num = int(input("Enter number to compare with the list: "))

#var1
def number_searcher(lst, num):
    if num in lst:
        return True
    else:
        return False

#print(number_searcher(lst, num))

#var2 (with binary search)
def binary_seacher(lst, num):
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

print(binary_seacher(lst, num))