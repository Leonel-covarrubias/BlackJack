
class Card:

  def __init__(self, valueArg):
    self.CardName = valueArg

    if (valueArg == "King" or valueArg == "Jack" or valueArg == "Queen"):
      self.value = 10
    elif valueArg == "Ace":
      self.value = 11
    else:
      self.value = valueArg

  def AddCards(self, arr):
    self.total = 0
    for i in range(len(arr)):
      self.total += arr[i].value

    return self.total

  def BustCheck(self, arr):
    if arr[0].AddCards(arr) > 21:
      return 1

    return 0
