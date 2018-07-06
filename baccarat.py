from game import *

def join_game(h, num=2):
  """num players join the game; default = 2 (essentially two brainless default
     players)."""

  for i in range(0, num):
    p = Hand()
    h.add_player(p)

def play_game(h):
  h.deal()
  print(h)

  h.clear_table()

def main():

  h = Baccarat()
  _PLAY_GAME = True

  while (_PLAY_GAME == True):
    join_game(h, 2)
    play_game(h)
    continue_playing = input("Do you want to keep playing (Y/N)? ")
    if (continue_playing.lower() == "y"):
      _PLAY_GAME = True
    else:
      _PLAY_GAME = False

  print("Thanks for playing at CasinoWorld.")

if __name__=="__main__":
  main()
