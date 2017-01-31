from python_tasks.Binary_Search import binary_searcher, lst

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

