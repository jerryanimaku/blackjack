from unittest import TestCase, main
from unittest.mock import patch
from test_helper_2 import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_one(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win(self, input_mock, randint_mock):
        '''
        The dealer receives cards that end up with a hand less than 21.
        The user receives cards that end up with a hand equal to 21.
        The user wins by having a Blackjack and a higher hand than the dealer.

        '''
        output = run_test([1, 7, 3], ['y'], [4, 9, 5], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 7\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 9\n" \
                   "Dealer has 13.\n" \
                   "Drew a 5\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)  



    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win_one(self, input_mock, randint_mock):
        '''
        The dealer receives cards that end up with a hand greater than 21.
        The user receives cards that end up with a hand less than 21.
        The user wins because the dealer busts.

        '''
        output = run_test([3, 4, 1], ['y', 'n'], [12, 6, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 4\n" \
                   "You have 7. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 6\n" \
                   "Dealer has 16.\n" \
                   "Drew a 9\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)   



    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win_two(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The user wins by having a higher hand value than the dealer.

        '''
        output = run_test([9, 10], ['n'], [5, 7, 6], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 10\n" \
                   "You have 19. Hit (y/n)? n\n" \
                   "Final hand: 19.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 7\n" \
                   "Dealer has 12.\n" \
                   "Drew a 6\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)  


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_win_three(self, input_mock, randint_mock):
        '''
        The dealer receives cards that end up with a hand less than 21.
        The user receives cards that end up with a hand equal to 21.
        The user wins by having a Blackjack and a higher hand than the dealer.

        '''
        output = run_test([11, 5, 6], ['x', 'y', 'n'], [9, 2, 4, 3], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Jack\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? x\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 2\n" \
                   "Dealer has 11.\n" \
                   "Drew a 4\n" \
                   "Dealer has 15.\n" \
                   "Drew a 3\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)  



    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        '''
        output = run_test([7, 9], ['n'], [5, 6, 13], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 9\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 5\n" \
                   "Drew a 6\n" \
                   "Dealer has 11.\n" \
                   "Drew a King\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)  



    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_one(self, input_mock, randint_mock):
        '''
        The dealer receives cards that end up with a hand less than 21.
        The user receives cards that end up with a hand greater than 21.
        The dealer wins because the user busts.

        '''
        output = run_test([8, 1, 6], ['y'], [6, 10, 4], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an 8\n" \
                   "Drew an Ace\n" \
                   "You have 19. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 10\n" \
                   "Dealer has 16.\n" \
                   "Drew a 4\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)  


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_two(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand greater than 21.
        The dealer wins by having a higher hand than the user.

        '''
        output = run_test([4, 7, 5, 3, 6], ['y', 'y', 'y'], [13, 6, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 7\n" \
                   "You have 11. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 19. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a 6\n" \
                   "Dealer has 16.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 27.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)  
 
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_win_three(self, input_mock, randint_mock):
        '''
        The user receives cards that end up with a hand less than 21.
        The dealer receives cards that end up with a hand equal to 21.
        The dealer wins by having a Blackjack and a higher hand than the user.

        '''
        output = run_test([1, 5, 3, 3], ['y', 'x', 'y'], [2, 13, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew an Ace\n" \
                   "Drew a 5\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "You have 19. Hit (y/n)? x\n" \
                   "Sorry I didn't get that.\n" \
                   "You have 19. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a King\n" \
                   "Dealer has 12.\n" \
                   "Drew a 9\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected) 

        
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_push_one(self, input_mock, randint_mock):
        '''
        Both the dealer and user end up with the same hand values less than 21.
        The game ends in a Push.

        '''
        output = run_test([9, 5, 6], ['y', 'n'], [2, 5, 2, 4, 3, 4], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 5\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 5\n" \
                   "Dealer has 7.\n" \
                   "Drew a 2\n" \
                   "Dealer has 9.\n" \
                   "Drew a 4\n" \
                   "Dealer has 13.\n" \
                   "Drew a 3\n" \
                   "Dealer has 16.\n" \
                   "Drew a 4\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)  


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_equal_bust(self, input_mock, randint_mock):
        '''
        Both the dealer and user end up with the same hand values greater than 21.
        The dealer wins because the user busts. 
        Even though the dealer busts also.

        '''
        output = run_test([6, 10, 1], ['y'], [9, 7, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 10\n" \
                   "You have 16. Hit (y/n)? y\n" \
                   "Drew an Ace\n" \
                   "Final hand: 27.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 7\n" \
                   "Dealer has 16.\n" \
                   "Drew an Ace\n" \
                   "Final hand: 27.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected) 


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_bust_one(self, input_mock, randint_mock):
        '''
        The dealer receives cards that end up with a hand greater than 21.
        The user receives cards that end up with a hand less than 21.
        The dealer wins because the user busts.

        '''
        output = run_test([3, 4, 1], ['y', 'n'], [12, 6, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                "YOUR TURN\n" \
                "-----------\n" \
                "Drew a 3\n" \
                "Drew a 4\n" \
                "You have 7. Hit (y/n)? y\n" \
                "Drew an Ace\n" \
                "You have 18. Hit (y/n)? n\n" \
                "Final hand: 18.\n" \
                "-----------\n" \
                "DEALER TURN\n" \
                "-----------\n" \
                "Drew a Queen\n" \
                "Drew a 6\n" \
                "Dealer has 16.\n" \
                "Drew a 9\n" \
                "Final hand: 25.\n" \
                "BUST.\n" \
                "-----------\n" \
                "GAME RESULT\n" \
                "-----------\n" \
                "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_bust_two(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand greater than 21.
        The dealer wins because the user busts.

        '''
        output = run_test([4, 7, 5, 3, 6], ['y', 'y', 'y'], [13, 6, 1], randint_mock, input_mock)
        expected = "-----------\n" \
                "YOUR TURN\n" \
                "-----------\n" \
                "Drew a 4\n" \
                "Drew a 7\n" \
                "You have 11. Hit (y/n)? y\n" \
                "Drew a 5\n" \
                "You have 16. Hit (y/n)? y\n" \
                "Drew a 3\n" \
                "You have 19. Hit (y/n)? y\n" \
                "Drew a 6\n" \
                "Final hand: 25.\n" \
                "BUST.\n" \
                "-----------\n" \
                "DEALER TURN\n" \
                "-----------\n" \
                "Drew a King\n" \
                "Drew a 6\n" \
                "Dealer has 16.\n" \
                "Drew an Ace\n" \
                "Final hand: 27.\n" \
                "BUST.\n" \
                "-----------\n" \
                "GAME RESULT\n" \
                "-----------\n" \
                "Dealer wins!\n"
        self.assertEqual(output, expected)
 
 
if __name__ == '__main__':
    main()