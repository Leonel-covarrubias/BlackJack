from Card import Card
import random


class Blackjack(Card):

  def __init__(self):
    pass

  def drawCard(self):
    cards = ("Ace", 2, 3, 4, 5, 6, 7, 8, 9, "Jack", "Queen", "King")
    element = random.randrange(0, len(cards))
    card = Card(cards[element])
    return card

  def DealHand(self):
    userChoice = 0
    DealerCards = []
    UserCards = []
    DealerCards.append(self.drawCard())
    DealerCards.append(self.drawCard())
    UserCards.append(self.drawCard())
    UserCards.append(self.drawCard())
    print("\nDealer has:", DealerCards[0].CardName, ", *hidden*")
    print("User has:", UserCards[0].CardName, ",", UserCards[1].CardName)
    check, BlackJackType = self.BlackJackCheck(DealerCards, UserCards)
    if check == 1:
      print(BlackJackType)
      return
    while (True):
      userChoice = input("1.) Stand \n2.) Hit\n")
      if userChoice == "1":
        print("User has", UserCards[0].AddCards(UserCards))
        if (UserCards[1].BustCheck(UserCards)):
          print("Bust")
          break
        break
      if userChoice == "2":
        UserCards.append(self.drawCard())
        print("User has", UserCards[0].AddCards(UserCards))
        if (UserCards[1].BustCheck(UserCards)):
          print("Bust")
          break
    return self.finish(UserCards, DealerCards)

  def BlackJackCheck(self, dealer, user):
    if dealer[0].value + dealer[1].value == 21:
      return 1, "Dealer BlackJack"
    if user[0].value + user[1].value == 21:
      return 1, "User BlackJack"
    if (dealer[0].value + dealer[1].value
        == 21) and (user[0].value + user[1].value == 21):
      return 1, "Push"
    return 0, ""

  def finish(self, user, dealer):
    while dealer[0].AddCards(dealer) < 17 and dealer[0].BustCheck(dealer) == 0:
      dealer.append(self.drawCard())
    print("Dealer has", dealer[0].AddCards(dealer))

    if (user[0].BustCheck(user) == 0 and dealer[0].BustCheck(dealer) == 0):
      if user[0].AddCards(user) > dealer[0].AddCards(dealer):
        return 1
      if user[0].AddCards(user) < dealer[0].AddCards(dealer):
        return 2
      if user[0].AddCards(user) == dealer[0].AddCards(dealer):
        return 0
    if (user[0].BustCheck(user) == 0 and dealer[0].BustCheck(dealer) == 1):
      return 1
    if (user[0].BustCheck(user) == 1 and dealer[0].BustCheck(dealer) == 0):
      return 2
