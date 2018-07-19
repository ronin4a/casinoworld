from card import Card

#TODO - restructure Hand vs PokerHand so Hand can be used as a generic class
class Hand(object):

  """In general, Hand object has two sets of cards - public cards (self.cards)
     which are shared by a group, and hole cards (__hole_cards) which belong
     to the Hand and are not shared or exposed to the group."""

  def __init__(self):

    self.__hole_cards = []
    self.cards = []

  def __str__(self):
    """Print list of Card objects in __hole_cards."""

    print_cards = []
    for card in self.__hole_cards:
      print_cards.append(str(card))

    return("%s" %(print_cards))


class BaccaratHand(Hand):

  """Local variables, used for ranking the BaccaratHand."""
  rank = {'none': 0, # has nothing
          'pair': 1, # max subranking = 13 (top pair)
          'two pair': 2, # max subranking = 13 (top pair)
          'three of a kind': 3, # max subranking = 13 (top card)
          'straight': 4, # max subranking = 13 (top card)
          'flush': 5, # max subranking = 4 (top suit)
          'full house': 6, # max subranking = 13 (top card)
          'four of a kind': 7, # max subranking = 13 (top card)
          'straight flush': 8} # max subranking = 52 (top suit + card)


  def __init__(self):
    """Baccarat is a two-player game; thus every initialization is the same.
       Players joining the game under their unique id will always be tagged
       Player. There will always be a bank."""

    super().__init__()
    self.__hole_cards = []
    self.score = 0

  def __str__(self):
    """Print list of Card objects in __hole_cards."""

    print_cards = []
    for card in self.__hole_cards:
      print_cards.append(str(card))

    return("%s" %(print_cards))


  def __len__(self):
    return len(self.__hole_cards)


  def add_card(self, card=None, is_hole=True):
    """Add a Card object as part of this Hand.

       is_hole flag needed to identify cards that are actually owned by the
       Hand; this is to distinguish these cards from community cards (e.g. the
       cards on the table in a game of Texas Hold Em)

       Note: The same Card can exist in multiple objects (other Hands, Decks,
             etc. This flexibility is provided with Hold Em Poker in mind, where
             Card objects on the Table are shared in multiple Hands between
             Players.
       """

    if card == None:
      return("Error: Adding no cards to hand.")

    if is_hole is True:
      self.__hole_cards.append(card)
    self.cards.append(card)


  def return_cards(self):
    """Empty all cards and pop hole cards."""
    self.cards = []
    return_hole_cards = []
    for i in range(0, len(self.__hole_cards)):
        return_hole_cards.append(self.__hole_cards.pop())

    #TODO check to make sure all self.cards are empty
    return(return_hole_cards)


  def hand_value(self):
    self.score = 0 # reset score
    for card in self.__hole_cards:
      if card.rank == 14: # Ace
        self.score += 1
      elif card.rank >= 10: # 10 or face cards
        self.score += 0
      else:
        self.score += card.rank
    return self.score % 10

  def return_3rd_card(self):
    if len(self.__hole_cards) != 3:
      return IndexError
    return self.__hole_cards[2]

class PokerHand(Hand):

  """Local variables, used for ranking the PokerHand."""

  rank = {'none': 0, # has nothing
          'pair': 1, # max subranking = 13 (top pair)
          'two pair': 2, # max subranking = 13 (top pair)
          'three of a kind': 3, # max subranking = 13 (top card)
          'straight': 4, # max subranking = 13 (top card)
          'flush': 5, # max subranking = 4 (top suit)
          'full house': 6, # max subranking = 13 (top card)
          'four of a kind': 7, # max subranking = 13 (top card)
          'straight flush': 8} # max subranking = 52 (top suit + card)


  """Basic functions."""

  def __init__(self, cards=None, is_hole=False):
    """Initialize a Hand, which is just a list of Card objects."""

    super().__init__()
    self.__hole_cards = []

    if (cards != None):
      if is_hole is True:
        self.__hole_cards.extend(cards)
      self.cards.extend(cards)

  def __str__(self):
    """Print list of Card objects in Hand."""

    print_cards = []
    for card in self.__hole_cards:
      print_cards.append(str(card))

    hand_rank, kicker_card = self.hand_value()

    return("PokerHand.rank: %s\nKicker card: %s\n%s" %(hand_rank, kicker_card, \
                                                  print_cards))


  def __len__(self):
    return(len(self.__hole_cards))

  #TODO Are these needed?
  def __lt__(self, other):
    return


  def __gt__(self, other):
    return


  def __eq__(self, other):
    return


  """Game functions."""


  def add_card(self, card=None, is_hole=False):
    """Add a Card object as part of this Hand.

       is_hole flag needed to identify cards that are actually owned by the
       Hand; this is to distinguish these cards from community cards (e.g. the
       cards on the table in a game of Texas Hold Em)

       Note: The same Card can exist in multiple objects (other Hands, Decks,
             etc. This flexibility is provided with Hold Em Poker in mind, where
             Card objects on the Table are shared in multiple Hands between
             Players.
       """

    if card == None:
      return("Error: Adding no cards to hand.")

    if is_hole is True:
      self.__hole_cards.append(card)
    self.cards.append(card)


  def return_cards(self):
    """Empty all cards and pop hole cards."""
    self.cards = []
    return_hole_cards = []
    for i in range(0, len(self.__hole_cards)):
        return_hole_cards.append(self.__hole_cards.pop())

    #TODO check to make sure all self.cards are empty
    return(return_hole_cards)

  def hand_value(self):
    """Hand value is calculated using a tuple of the PokerHand.rank (provided above)
       and the maximum card.card_value for card in self.cards as the kicker.
       
       Values are assessed by checking for the biggest hands first, then
       going down."""

    kicker = self.cards[0]
    for card in self.cards:
      if card.card_value() > kicker.card_value():
        kicker = card

    if self.has_straightFlush():
      return(PokerHand.rank['straight flush'], self.straightflush_kicker())
    if self.has_4ofAKind():
      return(PokerHand.rank['four of a kind'], self.generic_kicker(4))
    if self.has_fullHouse():
      """Note: want the kicker among the trips."""
      return(PokerHand.rank['full house'], self.generic_kicker(3))
    if self.has_flush():
      return(PokerHand.rank['flush'], self.flush_kicker())
    if self.has_straight():
      return(PokerHand.rank['straight'], self.straight_kicker())
    if self.has_3ofAKind():
      return(PokerHand.rank['three of a kind'], self.generic_kicker(3))
    if self.has_2Pair():
      return(PokerHand.rank['two pair'], self.generic_kicker(2))
    if self.has_pair():
      return(PokerHand.rank['pair'], self.generic_kicker(2))
    else:
      return(PokerHand.rank['none'], self.generic_kicker(1))
    # Catch all
    return False


  """Private functions."""
  #TODO make these inaccessible to anything outside this Class


  def find_card(self, suit=0, rank=2):
    """Basic function for returning the Card in self.cards, given the suit and
       rank values."""
    for card in self.cards:
      if card.suit == suit and card.rank == rank:
        return card
    return False


  def straightflush_kicker(self):
    """Straight flush kicker = highest flush first, then highest straight
       kicker."""

    flush_suit = self.flush_kicker().suit

    straight_cards = []
    for card in self.cards:
      if card.suit == flush_suit:
        straight_cards.append(card.rank)

    straight_cards = list(set(straight_cards))
    straight_cards.sort(reverse=True)

    try:
      high_rank = straight_cards[0]
    except IndexError as e:
      return("Error - no straight cards found. Please investigate.")

    for i in range(0, len(straight_cards)-5):
      if (straight_cards[i]-4) == straight_cards[i+4]:
        high_rank = straight_cards[i]
        break

    kicker = self.find_card(flush_suit, high_rank)

    return kicker


  def straight_kicker(self):
    """Assuming we have a straight, return the kicker card for the straight.
       Kicker := highest ranked card for ALL suits and all straights.
       """

    cards_by_rank = {}
    for card in self.cards:
      if card.rank not in cards_by_rank:
        cards_by_rank[card.rank] = []
      cards_by_rank[card.rank].append(card.suit)

    straight_ranks = list(set(self.ranks_in_hand()))
    straight_ranks.sort(reverse=True)

    for i in range(0, len(straight_ranks)-4):
      if straight_ranks[i+4] == (straight_ranks[i]-4):
        kicker_rank = straight_ranks[i]
        break

    try:
      kicker_suit = max(cards_by_rank[kicker_rank])
    except NameError:
      print("This was not a straight. Please investigate.")

    kicker = self.find_card(kicker_suit, kicker_rank)

    return kicker


  def flush_kicker(self):
    """Assuming we have a flush, return kicker card for the flush.
       Kicker := highest rank card for highest flush suit.
       """

    flush_suits = {}
    all_suits = self.suits_in_hand()

    for suit in all_suits:
      if all_suits[suit] >= 5:
        flush_suits[suit] = []

    for card in self.cards:
      if card.suit in flush_suits:
        flush_suits[card.suit].append(card.rank)

    kicker_suit = max(flush_suits)
    kicker_rank = max(flush_suits[kicker_suit])

    kicker = self.find_card(kicker_suit, kicker_rank)
    
    return kicker


  def generic_kicker(self, num=1):
    """Generic kicker given a number of cards. This function should work for
       any given set of cards (e.g. a pair, trips, etc.).
       Kicker := high Card for all sets where total number of Card objects
                 with rank = num.
       """

    ranks = self.ranks_in_hand()

    kicker_ranks = []

    for rank in ranks:
      if ranks[rank] == num:
        kicker_ranks.append(rank)

    kicker_ranks.sort(reverse=True)

    try:
      high_rank = kicker_ranks[0]
    except IndexError as e:
      return("There seem to be no Cards with count of %s." %(num))

    kicker_suits = []

    for card in self.cards:
      if card.rank == high_rank:
        kicker_suits.append(card.suit)

    kicker_suits.sort(reverse=True)
    try:
      high_suit = kicker_suits[0]
    except IndexError as e:
      return("Suits not found! Please investigate.")

    kicker = self.find_card(high_suit, high_rank)

    return kicker


  """Card counting functions."""

  def suits_in_hand(self):
    """Returns a dict of suits in hand. 
       Note: Suits are in raw numerical form rather than human-readable form. 
             E.g. 1 vs Clubs.
       """

    count_suits = {}

    for c in self.cards:
      current_suit = c.suit
      if current_suit in count_suits:
        count_suits[current_suit] += 1
      else:
        count_suits[current_suit] = 1

    return count_suits

  def ranks_in_hand(self):
    """Returns dict of ranks in hand. 
       Note: Ranks are in raw numerical form rather than human-readable form.
             E.g. 11 vs 'Jack'.
       """

    count_ranks = {}

    for c in self.cards:
      current_rank = c.rank
      if current_rank in count_ranks:
        count_ranks[current_rank] += 1
      else:
        count_ranks[current_rank] = 1

    return count_ranks


  """Poker hand assessment functions."""


  def check_multiple_ranks(self, num=1):
    """Template for checking for num instances of a rank in the Hand."""
    return(num in self.ranks_in_hand().values())

  def has_pair(self):
    """Check for a pair."""
    return(self.check_multiple_ranks(2))
    
  def has_3ofAKind(self):
    """Check for 3 of a kind."""
    return(self.check_multiple_ranks(3))

  def has_4ofAKind(self):
    """Check for 4 of a kind."""
    return(self.check_multiple_ranks(4))


  def has_2Pair(self):
    """Check for 2 different pairs in hand."""
    if self.has_pair() is False:
      return False
    count_pairs = 1
    for num_rank in self.ranks_in_hand().keys():
      if num_rank == 2:
        count_pairs += 1
      if count_pairs == 2:
        return True
    return False


  def has_straight(self):
    """Check for straight in the hand."""
    ranks = list(set(self.ranks_in_hand().keys()))
    if len(ranks) < 5:
      return False
    ranks.sort()

    for i in range(1, len(ranks)):
      if (ranks[i-1] + 1) != ranks[i]:
        return False
    return True


  def has_flush(self):
    """Check for 5 cards with the same suit in the hand."""
    return(max(self.suits_in_hand().values()) >= 5)

  def has_fullHouse(self):
    """Check for full house in hand."""
    return((self.has_3ofAKind()) and (self.has_pair()))


  def has_straightFlush(self):
    """Check for straight flush in hand."""
    return((self.has_flush()) and (self.has_straight()))
