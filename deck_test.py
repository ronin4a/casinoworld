from deck import *

def create_pokerhand(fn):
  """ Decorator to create a deck and assign cards. """
  def wrapper(d, h):

    fn(d, h)

    p = PokerHand(h)
    print(p)

  return wrapper

@create_pokerhand
def test_pairs(d, h):
  """ Create a deck and add a pair. Add another non-pair. Test both. """

  c = Card(2,5)
  d.add_card(c)
  c = Card(3,5)
  d.add_card(c)
  d.move_card(h,2)

@create_pokerhand
def test_nopairs(d, h):

  c = Card(2,6)
  d.add_card(c)
  c = Card(3,5)
  d.add_card(c)
  d.move_card(h,2)

@create_pokerhand
def test_trips(d, h):

  rank = 5

  c = Card(2, rank)
  d.add_card(c)
  c = Card(3, rank)
  d.add_card(c)
  c = Card(1, rank)
  d.add_card(c)
  d.move_card(h,3)

@create_pokerhand
def test_notrips(d, h):

  c = Card(2,5)
  d.add_card(c)
  c = Card(3,6)
  d.add_card(c)
  c = Card(1,5)
  d.add_card(c)
  d.move_card(h,3)

@create_pokerhand
def test_quads(d, h):

  rank = 5

  c = Card(2, rank)
  d.add_card(c)
  c = Card(3, rank)
  d.add_card(c)
  c = Card(1, rank)
  d.add_card(c)
  c = Card(0, rank)
  d.add_card(c)
  d.move_card(h,4)

@create_pokerhand
def test_noquads(d, h):

  c = Card(2,3)
  d.add_card(c)
  c = Card(3,5)
  d.add_card(c)
  c = Card(1,5)
  d.add_card(c)
  c = Card(0,5)
  d.add_card(c)
  d.move_card(h,4)

@create_pokerhand
def test_flush(d, h):

  suit = 2

  c = Card(suit, 5)
  d.add_card(c)
  c = Card(suit, 9)
  d.add_card(c)
  c = Card(suit, 10)
  d.add_card(c)
  c = Card(suit, 2)
  d.add_card(c)
  c = Card(suit, 11)
  d.add_card(c)

  d.move_card(h,5)

@create_pokerhand
def test_noflush(d, h):

  c = Card(2,5)
  d.add_card(c)
  c = Card(2,9)
  d.add_card(c)
  c = Card(2,10)
  d.add_card(c)
  c = Card(2,2)
  d.add_card(c)
  c = Card(3,11)
  d.add_card(c)

  d.move_card(h,5)

@create_pokerhand
def test_2pair(d, h):

  rank1 = 5
  rank2 = 10

  c = Card(2, rank1)
  d.add_card(c)
  c = Card(1, rank1)
  d.add_card(c)
  c = Card(2, rank2)
  d.add_card(c)
  c = Card(0, rank2)
  d.add_card(c)
  c = Card(2,2)
  d.add_card(c)

  d.move_card(h,5)

@create_pokerhand
def test_no2pair(d, h):

  c = Card(2,5)
  d.add_card(c)
  c = Card(1,5)
  d.add_card(c)
  c = Card(2,10)
  d.add_card(c)
  c = Card(0,9)
  d.add_card(c)
  c = Card(2,2)
  d.add_card(c)

  d.move_card(h,5)

@create_pokerhand
def test_fullhouse(d, h):

  rank1 = 5
  rank2 = 10

  c = Card(2, rank1)
  d.add_card(c)
  c = Card(1, rank1)
  d.add_card(c)
  c = Card(2, rank2)
  d.add_card(c)
  c = Card(0, rank2)
  d.add_card(c)
  c = Card(1, rank2)
  d.add_card(c)

  d.move_card(h,5)

@create_pokerhand
def test_nofullhouse(d, h):

  c = Card(2,5)
  d.add_card(c)
  c = Card(1,5)
  d.add_card(c)
  c = Card(2,10)
  d.add_card(c)
  c = Card(0,10)
  d.add_card(c)
  c = Card(1,11)
  d.add_card(c)

  d.move_card(h,5)

@create_pokerhand
def test_straightflush(d, h):

  suit = 2
  beginning_rank = 5

  # straight flush
  c = Card(suit, beginning_rank)
  d.add_card(c)
  c = Card(suit, beginning_rank + 1)
  d.add_card(c)
  c = Card(suit, beginning_rank + 2)
  d.add_card(c)
  c = Card(suit, beginning_rank + 3)
  d.add_card(c)
  c = Card(suit, beginning_rank + 4)
  d.add_card(c)

  d.move_card(h,5)

@create_pokerhand
def test_nostraightflush(d, h):

  c = Card(2,4)
  d.add_card(c)
  c = Card(2,6)
  d.add_card(c)
  c = Card(2,7)
  d.add_card(c)
  c = Card(2,8)
  d.add_card(c)
  c = Card(2,9)
  d.add_card(c)

  d.move_card(h,5)

def main():

  # Create a deck and a hand
  d = Deck()
  h = Hand()

  # test_pairs(d, h)
  # test_nopairs(d, h)

  # test_trips(d, h)
  # test_notrips(d, h)

  # test_quads(d, h)
  # test_noquads(d, h)

  # test_flush(d, h)
  # test_noflush(d, h)

  # test_2pair(d, h)
  # test_no2pair(d, h)

  # test_fullhouse(d, h)
  # test_nofullhouse(d, h)

  # test_straightflush(d, h)
  # test_nostraightflush(d, h)

if __name__ == "__main__":
  main()
