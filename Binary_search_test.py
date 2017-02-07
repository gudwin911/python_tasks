from Binary_Search import binary_searcher

lst = [0, 1 , 2, 3, 5, 8, 15, 18, 27, 31, 32, 35, 39, 45, 47,49,50,52,61,67,77,78,79,81,83,88,89,90,91,98,99]

class TestClass:
    def test_one(self):
        assert binary_searcher(lst, 5)

    def test_two(self):
        assert not binary_searcher(lst, 4)

    def test_three(self):
        assert not binary_searcher(lst, -1)

    def test_four(self):
        assert not binary_searcher(lst, 100)

    def test_five(self):
        assert binary_searcher(lst, 0)
