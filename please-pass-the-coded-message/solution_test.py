import solution
import unittest

class SolutionTest(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(4311, solution.solution([3, 1, 4, 1]))
    
    def test2(self):
        self.assertEqual(94311, solution.solution([3, 1, 4, 1, 5, 9]))


if __name__ == '__main__':
    unittest.main()