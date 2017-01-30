lst = [0,1,2,3,5,8,15,18,27,31,32,35,39,45,47,49,50,52,61,67,77,78,79,81,83,88,89,90,91,98,99]

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

class TestClass:
    def test_one(self):
        assert binary_searcher(lst, 5) == True

    def test_two(self):
        assert binary_searcher(lst, 4) == False

    def test_three(self):
        assert binary_searcher(lst, -1) == False

    def test_four(self):
        assert binary_searcher(lst, 100) == False

    def test_five(self):
        assert binary_searcher(lst, 0) == True

