from deck import *
from hand import *
from card import *
from table import *

class Game(object):

  """Basic functions."""


  def __init__(self):
    """Iniitalize a game. All card games should include:
 
      - a shuffled deck

       Dict of players:
        - key = player_id (for now, use a String name)
        - values = list of Hand objects
       Note that there should be NO players initialized in an instance of
       a Game. They have to be explicitly added.

       This is an instance of ONLY one round of a given game. Players are
       allowed to come in and out of a game.

       """

    self.deck = Deck()
    self.deck.shuffle()
    self.players = {}


  def __str__(self):
    """Print the game's current deck."""
    return("%s" %(self.deck))


  def add_player(self, p, name=""):
    """Add player p (represented by Class Hand) to current game. Check to
       make sure player name is unique."""
    if name=="":
      name = "Player" + str(len(self.players) + 1)
      self.players[name] = p
    elif name not in self.players:
      self.players[name] = p
    else:
      print("Player %s already has a hand...whaddya tryin' to pull here?" \
             %(name))

    return("Player %s added." %(name))


  def deal(self, num_cards=1):
    """Generic deal mechanism. In general, deal cards from self.deck to each
       player in self.players."""

    for i in range(0, num_cards):
      for player in self.players:
        __card = self.deck.pop_card()
        self.players[player].add_card(__card, True)

    return

  def deal_to(self, player, num_cards=1):
    """Deal to a single player.

       Args:
        - player = player key in self.players dict
        - num_cards = number of cards to deal
       """
    __card = self.deck.pop_card()
    self.players[player].add_card(__card, True)


  def clear_table(self):
    """Settle all bets, clear players from the game."""
    self.players.clear()
    return("Game ended.")


class HoldEm(Game):


  """Initializing functions."""


  def __init__(self):
    """Inherit generic Game.

       Diffs:
        - Table = required because there are publicly shared cards

       """
    #TODO make sure that each player_id only has one unique Hand
    super().__init__()
    self.table = Table()


  def __str__(self):
    print("\n-------------------------------------------------------")
    print("%s" %(self.table))
    if (len(self.players) != 0):
      for player in self.players:
        print("\n%s:\n%s" %(player, self.players[player]))
    return("-------------------------------------------------------\n")


  """Player mechanics."""


  def fold_player(self, player):
    """Player folds :=> player is removed from the HoldEm game."""
    try:
      self.players.pop(player)
    except KeyError as e:
      print("No player found; error %s" %(e))

    return("Player %s folds." %(player))


  """Basic game mechanics."""


  def deal(self):
    """Deal two cards to each player."""
    super().deal(2)
    return "Cards dealt."


  def deal_holdem(self, num=1):
    """Generic function to deal cards to the table.
       - Take 1 card off self.deck, deal to burn
       - Take num  card off self.deck, deal to table
       """

    c = self.deck.pop_card()
    self.table.add_burn_card(c)

    for i in range(0, num):
      c = self.deck.pop_card()
      self.table.add_table_card(c)
      for player in self.players:
        self.players[player].add_card(c)

    return("Cards dealt.")


  def flop(self):
    """Deal the flop :=
       - 1 card to burn
       - 3 cards to table
       """
    self.deal_holdem(3)
    return("Flop dealt.")


  def turn(self):
    """Deal the turn :=
       - 1 card to burn
       - 1 cards to table
       """
    self.deal_holdem(1)
    return("Turn dealt.")


  def river(self):
    """Deal the river :=
       - 1 card to burn
       - 1 cards to table
       """
    self.deal_holdem(1)
    return("River dealt.")


  """End of game mechanics."""


  def find_winners(self):
    """Calculate the winning score and return a list of winning players with
       that score."""
    ranked_players = {}
    hand_values = []

    for player in self.players:
      hand_values.append(self.players[player].hand_value())
      ranked_players[self.players[player].hand_value()] = player

    hand_values.sort(reverse=True)
    winning_player = ranked_players[hand_values[0]]

    # check for a tie
    try:
      if (hand_values[0] == hand_values[1]):
        print("Draw")
        return("Draw")
    except IndexError as e:
      return("There is only one hand? Critical error %s; investigate." %(e))

    print("\n-------------------------------------------------------")
    print("Final scores and cards:")
    for player in self.players:
      score, card = self.players[player].hand_value()
      print("%s has score %s; kicker %s" %(player, score, card))
    print("-------------------------------------------------------\n")

    print("\n-------------------------------------------------------")
    print("The winner is %s" %(winning_player))
    print("-------------------------------------------------------\n")

    return winning_player


class Baccarat(Game):


  """Initializing functions."""


  def __init__(self):
    """Inherit generic Game.

       Diffs:
        - always two players = Bank and Player
        - always init with two dealt cards to each

       """
    #TODO make sure that each player_id only has one unique Hand
    super().__init__()

    banker = BaccaratHand()
    player = BaccaratHand()
    if (len(self.players) != 0):
      for player in self.players:
        print("\n%s:\n%s" %(player, self.players[player]))
    super().add_player(banker, "Bank")
    super().add_player(player, "Player")


  def __str__(self):
    print("\n-------------------------------------------------------")
    if (len(self.players) != 0):
      for player in self.players:
        print("\n%s:\n%s\n%s\n" %(player, self.players[player], \
				  self.players[player].hand_value()))
    return("-------------------------------------------------------\n")


  """Basic game mechanics."""


  def does_player_get_3rd_card(self):
    """Check for Player getting a 3rd card. The Player gets a 3rd card if:
	- only has 2 cards
	- the value of those cards is between 0 - 5 (inclusive)
	"""
    player = self.players["Player"]
    if player.hand_value() <= 5:
      return True
    return False


  def does_bank_get_3rd_card(self):
    """Check for Bank getting a 3rd card. The Player gets a 3rd card if:
        - only has 2 cards
        - the value of those cards is between 0 - 5 (inclusive)
        """
    bank = self.players["Bank"]

    if (bank.hand_value() < 3):
      return True
    elif (bank.hand_value() >= 7):
      return False
    elif (self.players["Player"].hand_value() == 6) \
      or (self.players["Player"].hand_value() == 7):
      return True
    else:
      if (self.does_player_get_3rd_card() is False):
        if (self.players["Player"].hand_value() > 7):
          return False
        elif (bank.hand_value == 6) or (bank.hand_value == 5):
          return True
      """Else player drew; draw/no draw depends on player draw card."""
      player_3rd_card = self.players["Player"].return_3rd_card().rank
      if (player_3rd_card > 8): # Face card or Ace, 8 or 9
        return False
      # player_3rd_card should always be below 8
      elif (bank.hand_value() == 4) and (player_3rd_card >= 2):
        return True
      elif (bank.hand_value() == 5) and (player_3rd_card >= 4):
        return True
      elif (bank.hand_value() == 6) and (player_3rd_card >= 6):
        return True
      else:
        return False


  def find_winners(self):
    """Calculate the winner. If tie, return False."""
    final_bank_score = self.players["Bank"].hand_value()
    final_player_score = self.players["Player"].hand_value()

    if final_bank_score > final_player_score:
      return "Bank", self.players["Bank"]
    elif final_bank_score < final_player_score:
      return "Player", self.players["Player"]
    else:
      return "Tie", False

