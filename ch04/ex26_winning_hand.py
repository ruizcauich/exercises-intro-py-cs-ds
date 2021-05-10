import ex25_evaluating_hands as pocker_utils

deck = pocker_utils.initialize_deck()

hand_1 = []
hand_2 = []

for card in range(5):
    hand_1.append(deck.pop())
    hand_2.append(deck.pop())

if pocker_utils.is_a_straight_flush(hand_1):
    print('It is a straight flush')
    print(f'Hand 1 wins!')
elif pocker_utils.is_a_straight_flush(hand_2):
    print('It is a straight flush')
    print(f'Hand 2 wins!')
elif pocker_utils.is_four_of_a_kind(hand_1):
    print('It is a four of a kind')
    print(f'Hand 1 wins!')
elif pocker_utils.is_four_of_a_kind(hand_2):
    print('It is a four of a kind')
    print(f'Hand 2 wins!')
elif pocker_utils.is_a_full_house(hand_1):
    print('It is a full house')
    print(f'Hand 1 wins!')
elif pocker_utils.is_a_full_house(hand_2):
    print('It is a full house')
    print(f'Hand 2 wins!')
elif pocker_utils.is_a_flush(hand_1):
    print('It is a flush')
    print(f'Hand 1 wins!')
elif pocker_utils.is_a_flush(hand_2):
    print('It is a slush')
    print(f'Hand 2 wins!')
elif pocker_utils.is_a_straight(hand_1):
    print('It is a straight')
    print(f'Hand 1 wins!')
elif pocker_utils.is_a_straight(hand_2):
    print('It is a straight')
    print(f'Hand 2 wins!')
elif pocker_utils.is_three_of_a_kind(hand_1):
    print('It is three of a kind')
    print(f'Hand 1 wins!')
elif pocker_utils.is_three_of_a_kind(hand_2):
    print('It is three of a kind')
    print(f'Hand 2 wins!')
elif pocker_utils.is_two_pair(hand_1):
    print('It is a two pair')
    print(f'Hand 1 wins!')
elif pocker_utils.is_two_pair(hand_2):
    print('It is a two pair')
    print(f'Hand 2 wins!')
elif pocker_utils.is_pair(hand_1):
    print('It is a pair')
    print(f'Hand 1 wins!')
elif pocker_utils.is_pair(hand_2):
    print('It is a pair')
    print(f'Hand 2 wins!')
elif pocker_utils.is_a_high_card(hand_1):
    print('It is a is a high card')
    print(f'Hand 1 wins!')
elif pocker_utils.is_a_high_card(hand_2):
    print('It is a is a high card')
    print(f'Hand 2 wins!')


print(hand_1)
print(hand_2)