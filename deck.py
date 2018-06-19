""" Basic Deck and Hand Objects.

    Import Card object, as a Deck creates many Cards.

    Deck is the parent of Hand; a Hand can basically be interepreted as a small
    Deck.

    This class is meant to be used for the game of Poker:

    Remaining exercises = pdf page 199

    """

from card import *
import random
import copy

# Parent
class Deck(object):
  """ deck of cards
      """
  
  def __init__(self):
    self.cards = []
    for suit in range(4):
      for rank in range(1,14):
        card = Card(suit, rank)
        self.cards.append(card)
    print("Deck initialized...")

  def __str__(self):
    res = []
    for card in self.cards:
      res.append(str(card))
    # return("%s" %('\n'.join(res)))
    return("%s" %(res))

  def len(self):
    return(len(self.cards))

  def pop_card(self):
    return(self.cards.pop())

  def add_card(self, card):
    self.cards.append(card)

  def shuffle(self):
    random.shuffle(self.cards)

  # Use a basic insertion sort
  def sort(self,hand=None):

    if (hand == None):
      hand = self.cards
    
    for i in range(1,len(hand)):
      current = hand[i]
      j = i - 1
      while (j >= 0) and (current < hand[j]):
        hand[j + 1] = hand[j]
        j = j - 1
      hand[j+1] = current

  # Moves a Card from Object to target
  # Note that this can be a Hand -> Deck, Deck -> Hand, Hand -> Hand.
  # Technically, it can go from Deck to Deck (though this is probably not going
  # to happen in real life).
  # Args
  #   - hand = Hand() must be provided
  #   - num = number of cards to deal; default = 1
  # Returns
  #   - nothing; updates self and hand Objects 
  def move_card(self, target=None, num=1):

    if (target== None):
      return # should throw exception

    for i in range(0,num):
      if (self.len() == 0):
        print("No more cards! Error.") # should throw exception
        return
      card = self.pop_card()
      target.add_card(card)

  # Deals cards from current Object to given num_hands, with cards_per_hand.
  # Should create num_hands Hands, then returns them.
  # Args:
  #   - num_hands = number of hands to create
  #   - cards_per_hand = # of cards per hand
  # Returns:
  #   - num_hands Hand Objects
  def deal_cards(self, num_hands=1, cards_per_hand=1):

    hands = []

    for i in range(0, num_hands):
      tmp = Hand("Hand #%s" %(i))
      self.move_card(tmp, cards_per_hand)
      tmp.sort()
      hands.append(tmp)

    return(hands)

# Child - Deck.Card objects in a player's hand
# - has to evaluate current hand
class Hand(Deck):

  def __init__(self, label=''):
    self.cards = []
    self.label = label
    print("Hand initialized...")

  #TODO
  # Classifies hand to its highest value and returns the appropriate label
  #   - pair
  #   - two pair
  #   - three of a kind
  #   - straight
  #   - flush
  #   - full house
  #   - four of a kind
  #   - straight flush
  def classify(self):

    poker_hand = None # default value

    self.label = poker_hand

# Grandchild of Deck
# Child of Hand
class PokerHand(Hand):
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

  """ self.cards = deepycopy of cards, or a new Hand()
      self.card_tuples = tuple version of self.cards; (suit, rank)
      self.suits = suits of self.cards
      self.ranks = ranks of self.cards
      self.label = default as ''; 
                  will be updated to assign rank, using PokerHand.rank
      self.sublabel = subrank for each given label
      """
  def __init__(self, cards = None):
  
   if (cards == None):
     self.cards = Hand()
   else:
     self.cards = copy.deepcopy(cards)
   tmp_cards = copy.deepcopy(self.cards)

   tmp_card_tuples = []
   for i in range(0, self.cards.len()):
     tmp_card = tmp_cards.pop_card()
     tmp_card_tuples.append((tmp_card.suit, tmp_card.rank))

   suits = list(list(zip(*tmp_card_tuples))[0])
   ranks = list(list(zip(*tmp_card_tuples))[1])

   # Update dicts
   for index in range(0, len(ranks)):
     current_rank = ranks[index]
     PokerHand.count_ranks[current_rank] += 1

   for index in range(0, len(suits)):
     current_suit = suits[index]
     PokerHand.count_suits[current_suit] += 1

   # Note: self.cards already defined above
   self.card_tuples = tmp_card_tuples
   self.suits = suits
   self.ranks = ranks

   # Check for card in hand and assign a label + subrank
   if (self.has_straightFlush()):
      self.label = 'straight flush'
      self.subrank = max(self.ranks)
      return
   elif (self.has_4ofAKind()):
      self.label = 'four of a kind'
      self.subrank = max(self.ranks)
      return
   elif (self.has_fullHouse()):
      self.label = 'full house'

      subrank_tmp = {}

      for i in range(0, len(self.ranks)):
        tmp = self.ranks[i]

        if tmp in subrank_tmp.keys():
          subrank_tmp[tmp] += 1
        else:
          subrank_tmp[tmp] = 1

        if subrank_tmp[tmp] == 3:
          self.subrank = tmp

      return
   elif (self.has_flush()):
      self.label = 'flush'
      self.subrank = max(self.ranks)
      return
   elif (self.has_straight()):
      self.label = 'straight'
      self.subrank = max(self.ranks)
      return
   elif (self.has_3ofAKind()):
      self.label = 'three of a kind'
      self.subrank = max(self.ranks)
      return
   elif (self.has_2Pair()):
      self.label = 'two pair'
      self.subrank = max(self.ranks)
      return
   elif (self.has_pair()):
      self.label = 'pair'
      self.subrank = max(self.ranks)
      return
   else:
      self.label = 'none'
      self.subrank = max(self.ranks)


  def __str__(self):
    return("%s has hand %s, rank %d" %(self.cards, self.label,
                                        PokerHand.rank[self.label]))

  #################################  RANKING ##################################

  def has_num_ranks(self, num_ranks=2):
    return(num_ranks in PokerHand.count_ranks.values())

  def has_pair(self):
    return(self.has_num_ranks(2))
    
  def has_3ofAKind(self):
    return(self.has_num_ranks(3))

  def has_4ofAKind(self):
    return(self.has_num_ranks(4))

  def has_flush(self):
    return(5 in PokerHand.count_suits.values())

  def has_2Pair(self):
    count_pairs = 0
    for count_values in PokerHand.count_ranks.values():
      if (count_values == 2):
        count_pairs = count_pairs + 1
      if (count_pairs == 2):
        return True
    return False

  def has_straight(self):
    count = 0
    high_card = None
    for rank, num_rank in PokerHand.count_ranks.items():
      if num_rank == 0:
        count = 0
        continue
      count = count + 1
      if count == 5:
        high_card = rank
        count = count - 1
    return(high_card != None) # If None returned, no straight

  def has_fullHouse(self):
    return((self.has_3ofAKind()) and (self.has_pair()))

  def has_straightFlush(self):
    return((self.has_flush()) and (self.has_straight()))

# Child - Deck.Card objects on the table
class Table(Deck):

  def __init__(self):
    self.cards = []
    self.label = label
    print("Table initialized...")

  def deal_flop(self, deck, num_cards=3):
    tmp = self.cards
    deck.move_card(tmp, num_cards)


