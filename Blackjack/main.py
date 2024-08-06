
from Blackjack import Blackjack

def main():
  run = "0"
  game = Blackjack()
  while run:
    run = input("BLACKJACK!!\n1.) Deal Hand \n2.) Exit\n")
    if run == "2":
      return
    result = game.DealHand()
    if result == 1:
      print("\n USER WINS!\n")
    if result == 2:
      print("\n DEALER WINS\n")
    if result == 0:
      print("\n PUSH \n")


if __name__ == "__main__":
  main()
