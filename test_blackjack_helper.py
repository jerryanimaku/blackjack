from blackjack_helper import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """


  def test_print_card_name(self):
    self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
    self.assertEqual(get_print(print_card_name, 8), "Drew an 8\n")
    self.assertEqual(get_print(print_card_name, 13), "Drew a King\n")

  def test_draw_card(self):
    self.assertEqual(mock_random([5], draw_card), 5)
    self.assertEqual(mock_random([1], draw_card), 11)
    self.assertEqual(mock_random([12], draw_card), 10)

  def test_print_header(self):
    self.assertEqual(get_print(print_header, "Jeremiah"), "-----------\nJeremiah\n-----------\n")
    self.assertEqual(get_print(print_header, "DEALER"), "-----------\nDEALER\n-----------\n")
    self.assertEqual(get_print(print_header, "YOUR"), "-----------\nYOUR\n-----------\n")

  def test_draw_starting_hand(self):
    output = mock_random([12, 5], draw_starting_hand, "DEALER")
    self.assertEqual(output, 15)
    output_1 = mock_random([4, 9], draw_starting_hand, "DEALER")
    self.assertEqual(output_1, 13)
    output_2 = mock_random([1, 3], draw_starting_hand, "DEALER")
    self.assertEqual(output_2, 14)

  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_turn_status, 16), "Final hand: 16.\n")
    self.assertEqual(get_print(print_end_turn_status, 21), "Final hand: 21.\nBLACKJACK!\n")
    self.assertEqual(get_print(print_end_turn_status, 24), "Final hand: 24.\nBUST.\n")

  def test_print_end_game_status(self):
    expected_output = "-----------\nGAME RESULT\n-----------\nYou win!\n"
    self.assertEqual(get_print(print_end_game_status, 19, 22), expected_output)
    expected_output_1 = "-----------\nGAME RESULT\n-----------\nDealer wins!\n"
    self.assertEqual(get_print(print_end_game_status, 18, 20), expected_output_1)
    expected_output_2 = "-----------\nGAME RESULT\n-----------\nPush.\n"
    self.assertEqual(get_print(print_end_game_status, 19, 19), expected_output_2)

if __name__ == '__main__':
    unittest.main()