# PRIMARY INSTRUCTIONS

This is meant to simulate a basic game of poker, with increasing levels of
difficulty/complexity.

* (1) The basic program should deal cards and assess poker hands.<br />
    STATUS: Simple card dealing and presentation + individual scoring.
* (2) Incorporate betting.<br />
    STATUS: pyblock created; mechanism for Game and Bet
* (3) Upgrade basic program to simulate Texas Hold 'Em.<br />
    STATUS: 
* (4) Incorporate poker odds and a suggestion engine for the "best" play to make.
      Incorporate Kelly Criterion.<br />
    STATUS: 
* (5) Program an AI that plays heads up limit hold em.<br />
    STATUS: 
* (6) Incorporate Bowling paper (see 'holdem.pdf' in this folder)<br />
    STATUS: src code study required; currently not in pdf
* (7) Incorporate blockchain for bank mechanism<br />
    See: http://adilmoujahid.com/posts/2018/03/intro-blockchain-bitcoin-python/<br />
    See: https://github.com/dvf/blockchain<br />
    STATUS: commited initial repo to /pyblock

# LATEST UPDATES

UPDATES
- simulated hold em game with output and individual scoring

TODO
* thorough testing on dealing + hand assessments (noticed that a straight deal
  on the river wasn't scored as such)
* Note: hand.py -> self.ranks_in_hand() creats local dict for each call; restructure
        so only one instance of this dict is held in memory. (First confirm
        that this assumption is true.)
* use lambda functions to calculate kicker?
* inheritance Card -> Hand?
* include Exceptions or warning/error for app-specific exceptions; use this as a
  means of error checking
  - e.g. throw exception for invalid Card object
* add comparison functions for PokerHand (to figure out who the winner is)
* assess # of players, deal hands, check a winner

GENERAL CONSIDERATIONS
* security issues; chaos monkey this so no cheating can occur

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

