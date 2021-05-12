import random
import numpy as np

# Needed as globals since we need to access these two tuples from others
# functions.
FACES = ('Deuce', 'Three', 'Four', 'Five',
         'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')

SUITS = ('Hearts', 'Diamonds', 'Clubs', 'Spades')


def initialize_deck():
    """Initialize the card deck with card tuples

    Return a list of tuples each one containing a face and
    a suit like:

    [('Ace', 'Hearts')...]

    The list returned is already shuffled.
    """

    shuffled_deck = []

    for face in FACES:
        for suit in SUITS:
            shuffled_deck.append((face, suit))

    random.shuffle(shuffled_deck)

    return shuffled_deck


def get_unique_ranks_with_counts(hand):
    """Return the ranks (faces) of a hand with its counts"""
    hand_ranks = [card[0] for card in hand]
    unique_ranks = np.unique(hand_ranks, return_counts=True)

    return unique_ranks


def is_pair(hand):
    """Check whether the hand is a pair or not"""
    unique_ranks = get_unique_ranks_with_counts(hand)
    counts = list(unique_ranks[1])
    return counts.count(2) == 1 and counts.count(1) == 3


def is_two_pair(hand):
    """Check whether the hand is a two-pair or not"""
    unique_ranks = get_unique_ranks_with_counts(hand)
    counts = list(unique_ranks[0])
    return counts.count(2) == 2 and counts.count(1) == 1


def is_three_of_a_kind(hand):
    """Check whether the hand is a three or not"""
    unique_ranks = get_unique_ranks_with_counts(hand)
    counts = list(unique_ranks[0])
    return counts.count(3) == 1 and counts.count(1) == 2


def is_four_of_a_kind(hand):
    """Check whether the hand is a quad or not"""
    unique_ranks = get_unique_ranks_with_counts(hand)
    counts = list(unique_ranks[0])
    return counts.count(4) == 1


def is_five_of_a_kind(hand):
    """Check whether the hand contains five cards of one rank
    Always returns false since there are no wild cards
    """

    return False


def is_a_straight(hand):
    """Check whether a hand has sequential ranks"""
    # sort the hand in ascending order guided by
    # the FACES tuple
    ordered_hand = sorted(hand, key=lambda x: FACES.index(x[0]))
    # Use de FACES indices to check for continuity
    hand_rank_indices = [FACES.index(card[0]) for card in ordered_hand]

    for index, value in enumerate(hand_rank_indices[:-1]):
        if (hand_rank_indices[index + 1] - value) != 1:
            return False
    return True


def is_a_flush(hand):
    """Check whether a hand has all cards of same suit"""

    for index, card in enumerate(hand[:-1]):
        if card[1] != hand[index + 1]:
            return False
    return True


def is_a_straight_flush(hand):
    """Check if hand is both, a straight and a flush"""
    return is_a_straight(hand) and is_a_flush(hand)


def is_a_full_house(hand):
    """Check whether the hand is a three and a two at same time"""
    unique_ranks = get_unique_ranks_with_counts(hand)
    counts = list(unique_ranks[0])
    return counts.count(3) == 1 and counts.count(2) == 1


def is_a_high_card(hand):
    """Nothing, does not fall into any category"""
    return not is_pair(hand) and not is_two_pair(hand) and not is_three_of_a_kind(hand) and \
        not is_four_of_a_kind(hand) and not is_five_of_a_kind(hand) and not is_a_flush(hand) and\
        not is_a_straight(hand) and not is_a_full_house(hand)
