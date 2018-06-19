""" Basic Card Object definition.

    A card can be anything in classic 52-deck card deck.

    This class assumes we are only dealing with ONE deck; hence only __lt__
    and __gt__ are defined.

    """

class Card(object):
  """ Represents a standard playing card.
      """

  # Class attributes
  suits = {0: "Diamonds",
           1: "Clubs",
           2: "Hearts",
           3: "Spades"}

  # Note that 0 and 1 are not values; Ace placed at key=14
  ranks = {0: None,
           1: None,
           2: "2",
           3: "3",
           4: "4",
           5: "5",
           6: "6",
           7: "7",
           8: "8",
           9: "9",
           10: "10",
           11: "Jack",
           12: "Queen",
           13: "King",
           14: "Ace"}

  # Methods
  def __init__(self, suit=None, rank=None):
    if (suit == None):
      suit = 0
    if (rank== None):
      rank = 2
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return("%s of %s" %(Card.ranks[self.rank], Card.suits[self.suit]))

  # Assume we're only drawing from one deck; only > or < available

  # < :=
  def __lt__(self, other):

    # using tuples
    self_tmp = (self.suit, self.rank)
    other_tmp = (other.suit, other.rank)

    return(self_tmp < other_tmp)

  # > :=
  def __gt__(self, other):

    # using tuples
    self_tmp = (self.suit, self.rank)
    other_tmp = (other.suit, other.rank)

    return(self_tmp > other_tmp)
