STATE:
each player:
- cards: 4 unknown
- unknown destination cards: 2-3

self:
- cards: 4 known
- 2-3 destination cards

initialize
- all routes owner set to None

Train Cars: 256 - (self.cards) - 4*(P-1) - 5 river cards
Burn Train Cars: []
River: 5 cards
Destination Cards:
Burn Destination Cards: []

Start:
- decide which (if any) destination cards to drop