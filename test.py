import unittest
from main import rabin_karp


class RabinKarpTest(unittest.TestCase):

    def test_string_matching(self):
        self.assertEqual(rabin_karp("mny", "rmyujkhtnurjehtmny", 1011), ['Pattern mny found at index 15-17'])

    def test_string_matching2(self):
        self.assertEqual(rabin_karp("47", "431476325475265", 1011, 10), ['Pattern 47 found at index 3-4',
                                                                     'Pattern 47 found at index 9-10'])

    def test_string_matching3(self):
        self.assertEqual(rabin_karp("a", "1389462046", 10111101111011110111101111011110111, 10), [])

    def test_string_matching1(self):
        self.assertEqual(rabin_karp("a", "aaaaaaa", 101), ['Pattern a found at index 0-0',
                                                           'Pattern a found at index 1-1',
                                                           'Pattern a found at index 2-2',
                                                           'Pattern a found at index 3-3',
                                                           'Pattern a found at index 4-4',
                                                           'Pattern a found at index 5-5',
                                                           'Pattern a found at index 6-6'])


if __name__ == '__main__':
    unittest.main()
