from chip import *

class Bank(object):
  """ Bank holds all the known Chips in the entire casino; at least, the total
      # of Chips available for a card game.

      It has a balance, represented by the # of denominated Chip objects.

      Naive actions:
        - issue = distribute chips to players
        - deposit = receives deposits of chips from players

      Future actions:
        - accounts = has an account for each player (like a real Bank)
        - authentication by player

      """

  # Initialize Bank w/ default bankroll of $1M
  # Use solutions to knapsack problem to split up denominations.
  # Ref: https://en.wikipedia.org/wiki/Knapsack_problem
  # Note: Denoms is a dict, with key = denomination ($5, $50, etc.) and value =
  #       number of denominations
  def __init__(self, bankroll=1000000):
    self.balance = bankroll
    self.denoms = {} #TODO code knapsack problem

  def __str__(self):
    for denomination, num in self.denoms.items():
      print("$%s chips:\tx%s" %(denomination, num))
    return("Bank currently has $%s in total bankroll." %(self.balance))

  # Issues $amt to player; uses knapsack problem to issue optimal # of chips
  #TODO testing
  def issue(self, player, amt):

    to_issue = amt
    self.balance = bankroll - to_issue
    denominations = {}

    denominations = self.knapsack(

    player.withdraw(to_issue) #TODO code player


class Pot(Bank):
  """ Pot keeps track of the betting pool for each round of poker.

      Initialized to $0, with a dict with keys = all chips denoms, values = 0

      - Player objects bet into Pot
      - Pot closes out once Round is done

      """

  def __init__(self):
    self.pot_size = 0
    self.denoms = {}

class Stack(Bank):

  def __init__(self
