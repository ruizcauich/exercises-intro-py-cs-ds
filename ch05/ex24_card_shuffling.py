import random


def initialize_deck():
    """Initialize the card deck with card tuples

    Return a list of tuples each one containing a face and
    a suit like:

    [('Ace', 'Hearts')...]

    The list returned is already shuffled.
    """

    faces = ('Ace', 'Deuce', 'Three', 'Four', 'Five',
             'Six', 'Seven', 'Eight', 'Nine', 'Ten',
             'Jack', 'Queen', 'King')

    suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')

    shuffled_deck = []

    for face in faces:
        for suit in suits:
            shuffled_deck.append((face, suit))

    random.shuffle(shuffled_deck)

    return shuffled_deck


deck = initialize_deck()

for index in range(0, len(deck), 4):
    # Get 4 cards, in the next iteration get
    # the next 4
    cards = deck[index:index+4]

    print(f'{cards[0][1] + " of " + cards[0][0]:<20}'
          f'{cards[1][1] + " of " + cards[1][0]:<20}'
          f'{cards[2][1] + " of " + cards[2][0]:<20}'
          f'{cards[3][1] + " of " + cards[3][0]:<20}')
