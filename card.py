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

  """Basic functions."""

  def __init__(self, suit=None, rank=None):
    """Initialize Card object. This is the most atomic unit for all games in
       Casino World. A few issues we must address:
       
        - no valid cards allowed
        - default values assigned if an empty Card is attempted to be
          initialized
        - copies of the same Card are allowed to exist in the Casino, depending
          on rules of the Game being played

      """

    if (suit == None):
      suit = 0
    if (rank== None):
      rank = 2
    
    # if (rank not in range(0,4)) or (suit not in range(2,15)):
     #  return

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

  """Advanced functions."""

  def card_value(self):
    """Returns value of the card, based on suit and rank. Each of these
       properties are respectively ranked by their keys in the local dicts ranks
       and values."""

    return(13*self.suit + (self.rank-2))

  def face_value(self, card_value=0):
    """Given a card_value int, returns corresponding face value tuple,
       representing a Card."""
    face_suit = int(card_value/13)
    face_rank = card_value%13
    return(face_suit, face_rank)
