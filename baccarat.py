from game import *

_HEADER_ = "------------------------------"
_TESTING_ = True
_TEST_CONDITION_ = 5
_TEST_SUBCONDITION_ = 5

def join_game(h, num=2):
  """num players join the game; default = 2 (essentially two brainless default
     players)."""

  for i in range(0, num):
    p = Hand()
    h.add_player(p)

def play_game(h):

  if _TESTING_ is True:
    """case _TEST_CONDITION_:
	1: player draws (score < 6)
	2: player stands (score >= 6)
	3: banker draws (score < 3)
	4: banker stands (score >= 7)
	5: banker might draw (score between 4,6 inclusive)
	   case _TEST_SUBCONDITION_:
	   1: player did not draw,
	      then draw
	   2: player draw 0 (face card) or 1 (ace)
	      then no draw
	   3: banker score = 4 and player drew between 2 - 7 (inclusive)
	      then draw
	   4: banker score = 5 and player drew between 4 - 7 (inclusive)
	      then draw
	   5: banker score = 6 and player drew between 6 - 7 (inclusive)
	      then draw
	   6: all other cases
	      no draw
	      
      """
    for i in range (0,4):
      if _TEST_CONDITION_ == 5:
        break
      if _TEST_CONDITION_ == 1:
        c = Card(2,2)
      if _TEST_CONDITION_ == 2:
        c = Card(2,3)
      if _TEST_CONDITION_ == 3:
        c = Card(2,14)
      if _TEST_CONDITION_ == 4:
        c = Card(2,4)
      h.deck.add_card(c)

    if _TEST_CONDITION_ == 5:
      # Player's draw card
      c = Card(3,5)
      h.deck.add_card(c)
      if _TEST_SUBCONDITION_ == 1:
        # Player
        c = Card(3,4)
        h.deck.add_card(c)
        # Bank
        c = Card(3,2)
        h.deck.add_card(c)
        # Player
        c = Card(3,4)
        h.deck.add_card(c)
        # Bank
        c = Card(3,2)
        h.deck.add_card(c)
      elif _TEST_SUBCONDITION_ == 2:
        # Player
        c = Card(3,3)
        h.deck.add_card(c)
        # Bank
        c = Card(3,2)
        h.deck.add_card(c)
        # Player
        c = Card(3,2)
        h.deck.add_card(c)
        # Bank
        c = Card(3,2)
        h.deck.add_card(c)
      elif _TEST_SUBCONDITION_ == 3:
        # Player
        c = Card(3,4)
        h.deck.add_card(c)
        # Bank
        c = Card(3,2)
        h.deck.add_card(c)
        # Player
        c = Card(3,1)
        h.deck.add_card(c)
        # Bank
        c = Card(3,2)
        h.deck.add_card(c)
      elif _TEST_SUBCONDITION_ == 4:
        # Player
        c = Card(3,3)
        h.deck.add_card(c)
        # Bank
        c = Card(3,2)
        h.deck.add_card(c)
        # Player
        c = Card(3,2)
        h.deck.add_card(c)
        # Bank
        c = Card(3,3)
        h.deck.add_card(c)
      elif _TEST_SUBCONDITION_ == 5:
        # Player
        c = Card(3,3)
        h.deck.add_card(c)
        # Bank
        c = Card(3,2)
        h.deck.add_card(c)
        # Player
        c = Card(3,2)
        h.deck.add_card(c)
        # Bank
        c = Card(3,4)
        h.deck.add_card(c)
      elif _TEST_SUBCONDITION_ == 6:
        # Player
        c = Card(3,2)
        h.deck.add_card(c)
        # Bank
        c = Card(3,2)
        h.deck.add_card(c)
        # Player
        c = Card(3,3)
        h.deck.add_card(c)
        # Bank
        c = Card(3,2)
        h.deck.add_card(c)


  h.deal(2)
  print(h)
  input()
  print("Does player get 3rd card? %s" %(h.does_player_get_3rd_card()))
  if h.does_player_get_3rd_card() is True:
    h.deal_to("Player")
    input()
  print("Does banker get 3rd card? %s" %(h.does_bank_get_3rd_card()))
  if h.does_bank_get_3rd_card() is True:
    h.deal_to("Bank")
    input()
  print(h)
  input()
  h.clear_table()

def main():

  h = Baccarat()
  _PLAY_GAME = True

  while (_PLAY_GAME == True):
    # join_game(h, 2)
    play_game(h)
    continue_playing = input("Do you want to keep playing (Y/N)? ")
    if (continue_playing.lower() == "y"):
      _PLAY_GAME = True
    else:
      _PLAY_GAME = False

  print("Thanks for playing at CasinoWorld.")

if __name__=="__main__":
  main()
