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

       """

    self.deck = Deck()
    self.deck.shuffle()
    self.players = {}


  def __str__(self):
    """Print the game's current deck."""
    return("%s" %(self.deck))


  def deal(self, num_cards=1):
    """Generic deal mechanism. In general, deal cards from self.deck to each
       player in self.players."""

    for i in range(0, num_cards):
      for player in self.players:
        __card = self.deck.pop_card()
        self.players[player].add_card(__card, True)

    return

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


  def add_player_to_game(self, p, name=""):
    """Add player p (represented by Class Hand) to current game."""
    if name=="":
      name = "Player" + str(len(self.players) + 1)
      self.players[name] = p
    elif name in self.players:
      self.players[name] = p
    else:
      print("Player %s already has a hand...whaddya tryin' to pull here?" \
             %(name))

    return("Player %s added." %(name))


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

    return


  def flop(self):
    """Deal the flop :=
       - 1 card to burn
       - 3 cards to table
       """
    self.deal_holdem(3)
    return "Flop dealt."


  def turn(self):
    """Deal the turn :=
       - 1 card to burn
       - 1 cards to table
       """
    self.deal_holdem(1)
    return "Turn dealt."


  def river(self):
    """Deal the river :=
       - 1 card to burn
       - 1 cards to table
       """
    self.deal_holdem(1)
    return "River dealt."


  """End of game mechanics."""


  def find_winners(self):
    """Calculate the winning score and return a list of winning players with
       that score."""
    winning_players = []
    max_hand_value = 0

    # Calculate highest hand value
    for player in self.players:
      current_player_value = self.players[player].hand_value()
      if current_player_value >= max_hand_value:
        max_hand_value = current_player_value

    for player in self.players:
      current_player_value = self.players[player].hand_value()
      if current_player_value = max_hand_value:
        winning_players.append(self.players[player])

    return winning_players

