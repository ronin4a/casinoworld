""" Basic Card Object definition.

    A card can be anything in classic 52-deck card deck.

    This class assumes we are only dealing with ONE deck; hence only __lt__
    and __gt__ are defined.

    """

class Card(object):
  """ Represents a standard playing card."""

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


  def __init__(self, suit=None, rank=None):
    if (suit == None):
      suit = 0
    if (rank== None):
      rank = 2
    self.suit = suit
    self.rank = rank


  def __str__(self):
    return("%s of %s" %(Card.ranks[self.rank], Card.suits[self.suit]))


  """Because we assume we're only drawing from one deck; only > or <  are
     available."""

  def __lt__(self, other):
    """Less than."""
    # using tuples
    self_tmp = (self.suit, self.rank)
    other_tmp = (other.suit, other.rank)

    return(self_tmp < other_tmp)

  def __gt__(self, other):
    """Greater than."""

    # using tuples
    self_tmp = (self.suit, self.rank)
    other_tmp = (other.suit, other.rank)

    return(self_tmp > other_tmp)

class Hand(Card):
  """ Child of Hand
      
      PokerHand is initialized in Hand as a means of investigating and returning
      a label for the type of poker hand the cards being assessed have.

      They will also return a ranking. Default ranking = 0 (no hand)

      """

  rank = {'none': 0, # has nothing
          'pair': 1, # max subranking = 13 (top pair)
          'two pair': 2, # max subranking = 13 (top pair)
          'three of a kind': 3, # max subranking = 13 (top card)
          'straight': 4, # max subranking = 13 (top card)
          'flush': 5, # max subranking = 4 (top suit)
          'full house': 6, # max subranking = 13 (top card)
          'four of a kind': 7, # max subranking = 13 (top card)
          'straight flush': 8} # max subranking = 52 (top suit + card)

  # Dict used to represent count of suits and ranks. Default count = 0.
  count_suits = {0: 0,
                 1: 0,
                 2: 0,
                 3: 0}

  count_ranks = {0: 0,
                 1: 0,
                 2: 0,
                 3: 0,
                 4: 0,
                 5: 0,
                 6: 0,
                 7: 0,
                 8: 0,
                 9: 0,
                 10: 0,
                 11: 0,
                 12: 0,
                 13: 0}

  def __init__(self, cards=None):
    """Initialize a Hand, which is just a list of Card objects."""

    self.cards = []

    if (cards != None):
      self.cards.append(cards)

    self.rank = 0
