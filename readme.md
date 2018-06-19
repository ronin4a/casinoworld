# PRIMARY INSTRUCTIONS

This is meant to simulate a basic game of poker, with increasing levels of
difficulty/complexity.

(1) The basic program should deal cards and assess poker hands.
    STATUS: ONGOING
(2) Incorporate betting.
    STATUS: 
(3) Upgrade basic program to simulate Texas Hold 'Em.
    STATUS: 
(4) Incorporate poker odds and a suggestion engine for the "best" play to make.
    Incorporate Kelly Criterion.
    STATUS: 
(5) Program an AI that plays heads up limit hold em.
    STATUS: 
(6) Incorporate Bowling paper (see 'holdem.pdf' in this folder)
    STATUS: 
(7) Incorporate blockchain for bank mechanism
    See: http://adilmoujahid.com/posts/2018/03/intro-blockchain-bitcoin-python/
    See: https://github.com/dvf/blockchain
    STATUS: commited initial repo to /pyblock

# LATEST UPDATES

** TODO
  - PokerHand instantiates to the same location in memory; assigning different
    cards :=> the count persists...incorrect self.label created (see deck_test)
  - add comparison functions for PokerHand (to figure out who the winner is)
  - assess # of players, deal hands, check a winner

* updated deck.py
  - all PokerHand checks pass (functionally)
* ...however, next steps:
  - get basic poker game analyzed (rankings work)
  - set up mechanics of game:
    - cmp two PokerHands
    - dealing Cards
  - update data structure of PokerHand so it's a little more elegant and less
    brute force

# FUTURE THOUGHTS

* craps
* baccarat
* other variations of poker
* blackjack

# BASIC DATA STRUCTURES

## Two atomic classes
* Chip
* Card

## Two parent classes
* Bank = composed of many Chips
* Deck = composed of many Cards
* Player = holds Chips and plays a Hand

## Two children classes
* Stack = individual stack of Chips (from Bank)
* Pot = Chips at stake for current hand
* Hand = individual hand of Chips (from Deck)

