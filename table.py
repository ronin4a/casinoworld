from card import Card

class Table(object):

  """Basic functions."""

  def __init__(self, burn=True, cards=None):
    """Initialize a Table, which consists of burn and table cards."""

    self.__burn_cards = []
    self.table_cards = []

    if (cards != None):
      if burn is True:
        self.__burn_cards.extend(cards)
      else:
        self.table_cards.extend(cards)

  def __str__(self):
    """Print table cards."""

    print_cards = []
    for card in self.table_cards:
      print_cards.append(str(card))

    debug_cards = []
    for card in self.__burn_cards:
      debug_cards.append(str(card))

    return("Hole: %s\nTable: %s" %(debug_cards, print_cards))

  def add_burn_card(self, card=None):
    """Add a Card object to the burn pile."""

    if card == None:
      return("Error: Adding no cards to table.")

    self.__burn_cards.append(card)

  def add_table_card(self, card=None):
    """Add a Card object to the table."""

    if card == None:
      return("Error: Adding no cards to table.")

    self.table_cards.append(card)

  def return_cards(self):
    """Empty all cards and pop hole cards."""
    return_cards = []
    for i in range(0, len(self.__burn_cards)):
        return_cards.append(self.__burn_cards.pop())
    for i in range(0, len(self.table_cards)):
        return_cards.append(self.table_cards.pop())

    #TODO check to make sure all self.cards are empty
    return(return_cards)

