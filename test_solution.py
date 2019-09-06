import solution
import unittest


class Test_TestSolution(unittest.TestCase):
    def setUp(self):
        self.sut = solution.Solution()

    def test_countBits(self):
        self.assertEqual(
            self.sut.countBits(1),
            [0, 1])

        self.assertEqual(
            self.sut.countBits(2),
            [0, 1, 1])

        self.assertEqual(
            self.sut.countBits(5),
            [0, 1, 1, 2, 1, 2])


if __name__ == '__main__':
    unittest.main()
