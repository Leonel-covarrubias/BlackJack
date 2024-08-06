import unittest
from Card import Card
from Blackjack import Blackjack


class TestBlackJack(unittest.TestCase):

  #unit test

  def test_AddCards(self):
    arrCards = []
    card = Card(1)
    arrCards.append(card)
    self.assertEqual(1, arrCards[0].AddCards(arrCards))

#unit test

  def test_test_BustCheck(self):
    arrCards = []
    card = Card(24)
    arrCards.append(card)
    self.assertTrue(arrCards[0].BustCheck(arrCards))

#unit test

  def test_BustCheck_false(self):
    arrCards = []
    card = Card(20)
    arrCards.append(card)
    self.assertFalse(arrCards[0].BustCheck(arrCards))


#Integration test

  def test_finsh_Push(self):
    game = Blackjack()
    userCards = []
    card = Card(20)
    userCards.append(card)
    dealerCards = []
    dealerCards.append(card)
    self.assertEqual(0, game.finish(dealerCards, userCards))

  #Integration test

  def test_finsh_UserWin(self):
    userCards = []
    game = Blackjack()
    card = Card(20)
    userCards.append(card)
    dealerCards = []
    card2 = Card(19)
    dealerCards.append(card2)
    self.assertEqual(1, game.finish(userCards, dealerCards))

  #Integration test

  def test_finsh_dealerWin(self):
    game = Blackjack()
    userCards = []
    card = Card(19)
    userCards.append(card)
    dealerCards = []
    card2 = Card(20)
    dealerCards.append(card2)
    self.assertEqual(2, game.finish(userCards, dealerCards))

  #Integration test

  def test_finsh_dealer_Win_if_User_busted(self):
    game = Blackjack()
    userCards = []
    card = Card(22)
    userCards.append(card)
    dealerCards = []
    card2 = Card(20)
    dealerCards.append(card2)
    self.assertEqual(2, game.finish(userCards, dealerCards))

  #Integration test

  def test_finsh_User_Win_if_dealer_busted(self):
    game = Blackjack()
    userCards = []
    card = Card(20)
    userCards.append(card)
    dealerCards = []
    card2 = Card(22)
    dealerCards.append(card2)
    self.assertEqual(1, game.finish(userCards, dealerCards))
