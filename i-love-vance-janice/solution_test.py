import solution
import unittest

class SolutionTest(unittest.TestCase):
    
    def test1(self):
        self.assertEqual("did you see last night's episode?",
                         solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))

    def test2(self):
        self.assertEqual("Yeah! I can't believe Lance lost his job at the colony!!",
                         solution.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))


if __name__ == '__main__':
    unittest.main()