from deck import *
from hand import *
from card import *

def main():
  """Testing all current classes with a sample Poker game.
     For now - have two players (represented by two Hand objects) and deal Card
     objects to each Hand. Then assess the respective Hand objects and declare
     a winner.
     """

  d = Deck()
  d.shuffle()

  player1 = Hand()
  player2 = Hand()

  c = Card(0,2)
  player1.add_card(c)
  c = Card(1,2)
  player1.add_card(c)
  c = Card(2,2)
  player1.add_card(c)
  c = Card(3,2)
  player1.add_card(c)
  c = Card(3,7)
  player1.add_card(c)
  
  for i in range(0,5):
    # c = d.pop_card()
    # player1.add_card(c)
    c = d.pop_card()
    player2.add_card(c)

  print(player1)
  # print(player1.ranks_in_hand())
  # print(player1.has_4ofAKind())
  print(player1.hand_value())
  # print(player2)
  # print(player2.hand_value())

if __name__ == "__main__":
  main()
