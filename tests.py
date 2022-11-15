import unittest

import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    # TODO: Test all fuctions from logic.py!

    def test_other_player(self):
    
        player = '1'
        self.assertEqual(logic.other_player('0'), '1')

if __name__ == '__main__':
    unittest.main()