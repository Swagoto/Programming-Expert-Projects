#### 1. Make the Deck
    each 1-9 plus J, Q, K, A (a list)
    For symbols:
        >>> print(u"\u2666") for diamond
        ♦
        >>> print(u"\u2665") for heart
        ♥
        >>> print(u"\u2663") for club
        ♣
        >>> print(u"\u2660") for spade
        ♠
    generate a dictionary {"card_key": "points"}
        1-9 correspond to number of their points, for J, Q, K each is 10 and for A 11 or 1 (if current score + 11 > 21)
        
#### 2. Make a dealing function.
