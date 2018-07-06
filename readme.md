# PRIMARY INSTRUCTIONS

This is meant to simulate a basic game of poker, with increasing levels of
difficulty/complexity.

* (1) The basic program should deal cards and assess poker hands.<br />
    STATUS: Dealing + winner logic created.
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
- complete HoldEm Class:<br />
  x wrote and did initial testing for find_winners function in Game Class<br />
  x tested multiplayer (n > 2) scoring<br />

TODO
* complete HoldEm Class:
  - test Game:find_winners() and create full game mechanics
  - maybe use turn deal_holdem as a decorator
* port logic over to functions (rather than body of main)
* make a list of exceptions and error checks; include in the Class files
* unicode cards for display
* use lambda functions to calculate kicker?
* inheritance Card -> Hand?
* include Exceptions or warning/error for app-specific exceptions; use this as a
  means of error checking
  - e.g. throw exception for invalid Card object
* add comparison functions for PokerHand (to figure out who the winner is)
* assess # of players, deal hands, check a winner

GENERAL CONSIDERATIONS
* security issues; chaos monkey this so no cheating can occur
* how to assign true ownership of a Card object; not enough to just have an
  array point to the Card objects (see hand.py)
* adding players = dict of a player account:Hands; tie in player accounts to
  Flask logins and accounts on pyblock; this will require additional backend
  db management
* how to concurrently run various Games in parallel; note that the same player
  can be involved in different Games, if required

# FUTURE THOUGHTS

* craps
* baccarat
* other variations of poker
* blackjack

# BASIC DATA STRUCTURES

## TO BE FILLED OUT
This section should be filled out once Game and HoldEm classes are completed.
It would be a good checkpoint to assess current state + clean everything up so
we have a fully functional game engine infrastructure. Then the next 2 - 3 major
milestones can be sketched out (implementing betting on the blockchain, db
management, and a web app frontend = what comes to mind).
