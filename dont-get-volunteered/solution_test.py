import solution
import unittest

class SolutionTest(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(3, solution.solution(0, 1))

    def test2(self):
        self.assertEqual(1, solution.solution(19, 36))


if __name__ == '__main__':
    unittest.main()