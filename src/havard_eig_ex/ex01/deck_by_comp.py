SUITS = ('C', 'S', 'H', 'D')
VALUES = range(1, 14)


def deck_loop():
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck


def deck_comp():
    return [(suit, value) for suit in SUITS for value in range(1, 14)]


if __name__ == '__main__':
    if deck_loop() != deck_comp():
        print('ERROR!')
