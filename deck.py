from card import Card
import random
import copy


class Deck(object):


  """ Create a deck of cards."""
  
  def __init__(self):
    """Initialize a deck of cards, represented as a list of Card objects.
       Note that rank goes from 2 - 14 (inclusive), as 0 and 1 are not valid
       rank values; this is due to the Ace being the default highest value
       card, above the King (position 13)."""
    self.cards = []
    for suit in range(4):
      for rank in range(2,15):
        card = Card(suit, rank)
        self.cards.append(card)
    print("Deck initialized...")


  """Basic functions."""

  def __str__(self):
    """Outputs user-readable string of cards in Deck."""
    res = []
    for card in self.cards:
      res.append(str(card))
    # return("%s" %('\n'.join(res)))
    return("%s" %(res))

  def len(self):
    """Returns # of cards in the Deck."""
    return(len(self.cards))

  def pop_card(self):
    """Pops off top card in deck. 
       Primarily used for for dealing Cards to a Hand."""
    try:
      return(self.cards.pop())
    except IndexError as e:
      return("No mord Cards in Deck!")

  def add_card(self, card):
    """Adds a card to the top of the deck. 
       Primarily used for putting Cards from Hand back to Deck."""
    self.cards.append(card)

  def shuffle(self):
    """Shuffles the Deck."""
    random.shuffle(self.cards)


  """Advanced functions."""

  def sort(self, hand=None):
    """Basic insertion sort."""

    if (hand == None):
      hand = self.cards
    
    for i in range(1,len(hand)):
      current = hand[i]
      j = i - 1
      while (j >= 0) and (current < hand[j]):
        hand[j + 1] = hand[j]
        j = j - 1
      hand[j+1] = current

