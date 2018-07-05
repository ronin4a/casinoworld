from deck import *
from hand import *
from card import *
from table import *

_TESTING = False

def testing(d):
  if _TESTING:
    # Testing - straight flush doesn't seem to work?
    for i in range(0,9):
      if (i > 6):
        c = Card(1,i+3)
        d.add_card(c)
      c = Card(1,i+3)
      d.add_card(c)
  print(d)

def main():
  """Testing all current classes with a sample Poker game.
     For now - have two players (represented by two Hand objects) and deal Card
     objects to each Hand. Then assess the respective Hand objects and declare
     a winner.
     """

  # Initialize deck
  d = Deck()
  d.shuffle()
  t = Table()

  testing(d)

  # Initialize players
  player1 = Hand()
  player2 = Hand()

  # Deal pre-flop
  for i in range(0,2):
    c = d.pop_card()
    player1.add_card(c, True)
    c = d.pop_card()
    player2.add_card(c, True)
  print("*** PRE FLOP ***")
  print("On the table: %s" %(t))
  print()
  print("Player 1: %s" %(player1))
  print()
  print("Player 2: %s" %(player2))
  input()

  # Deal flop
  if not _TESTING:
    c = d.pop_card()
    t.add_burn_card(c)
  for i in range(0,3):
    c = d.pop_card()
    t.add_table_card(c)
    player1.add_card(c)
    player2.add_card(c)
  print("*** FLOP ***")
  print("On the table: %s" %(t))
  print()
  print("Player 1: %s" %(player1))
  print()
  print("Player 2: %s" %(player2))
  input()

  # Deal turn
  if not _TESTING:
    c = d.pop_card()
    t.add_burn_card(c)
  c = d.pop_card()
  t.add_table_card(c)
  player1.add_card(c)
  player2.add_card(c)
  print("*** TURN ***")
  print("On the table: %s" %(t))
  print()
  print("Player 1: %s" %(player1))

  print()
  print("Player 2: %s" %(player2))
  input()

  # Deal river
  if not _TESTING:
    c = d.pop_card()
    t.add_burn_card(c)
  c = d.pop_card()
  t.add_table_card(c)
  player1.add_card(c)
  player2.add_card(c)
  print("*** RIVER ***")
  print("On the table: %s" %(t))
  print()
  print("Player 1: %s" %(player1))
  print()
  print("Player 2: %s" %(player2))
  input()

  # Assess winner
  if (player1.hand_value() > player2.hand_value()):
    print("Player 1 won with %s." %(player1))
  elif (player1.hand_value() < player2.hand_value()):
    print("Player 2 won with %s." %(player2))
  else:
    print("Draw.")

if __name__ == "__main__":
  main()
