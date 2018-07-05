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

    for i in range(0, num_cards*len(self.players)):
      for player in self.players:
        __card = self.deck.pop()
        self.players[player].add_card(__card, True)

    return

class HoldEm(Game):

  def __init__(self):
    """Inherit generic Game.

       Diffs:
        - Table = required because there are publicly shared cards

       """
    #TODO make sure that each player_id only has one unique Hand
    super().__init__()
    self.table = Table()

  def __str__(self):
    print(super().__str__())
    return("%s" %(self.players))

  def add_player_to_game(self, p, name=""):
    """Add player p (represented by Class Hand) to current game."""
    if name=="":
      default_name = "Player" + str(len(self.players) + 1)
      self.players[default_name] = p
    elif name in self.players:
      self.players[name] = p
    else:
      print("Player %s already has a hand...whaddya tryin' to pull here?" \
             %(name))

  def deal(self):
    """Deal two cards to each player."""
    super().deal(self, 2)
