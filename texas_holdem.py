from game import *

def join_game(h, num=2):
  """num players join the game; default = 2 (essentially two brainless default
     players)."""

  for i in range(0, num):
    p = Hand()
    h.add_player(p)

def main():

  h = HoldEm()
  join_game(h, 2)
  h.deal()
  print(h)

  h.flop()
  print(h)
  input()

  h.turn()
  print(h)
  input()

  h.river()
  print(h)
  input()

  h.find_winners()

if __name__=="__main__":
  main()
