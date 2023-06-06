import random

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    value = 0
    has_ace = False

    for card in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            has_ace = True
            value += 1
        else:
            value += int(card)

    if has_ace and value + 10 <= 21:
        value += 10

    return value

# Function to deal a new card
def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

# Game setup
player_hand = []
dealer_hand = []

# Deal initial cards
for _ in range(2):
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())

game_over = False

while not game_over:
    player_score = calculate_hand_value(player_hand)
    dealer_score = calculate_hand_value(dealer_hand)

    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    # Check if player or dealer has blackjack or went over 21
    if player_score == 21 or dealer_score == 21 or player_score > 21:
        game_over = True
    else:
        # Ask the player if they want to get another card or stop
        should_continue = input("Type 'y' to get another card, or 'n' to pass: ")

        if should_continue == 'y':
            player_hand.append(deal_card())
        else:
            game_over = True

    # Update scores after the player takes another card
    player_score = calculate_hand_value(player_hand)
    dealer_score = calculate_hand_value(dealer_hand)

# Dealer's turn to draw cards
while dealer_score < 17 and dealer_score <= player_score and player_score <= 21:
    dealer_hand.append(deal_card())
    dealer_score = calculate_hand_value(dealer_hand)

print(f"\nYour final hand: {player_hand}, final score: {player_score}")
print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")

# Determine the winner
if player_score > 21:
    print("You went over. You lose.")
elif dealer_score > 21:
    print("Dealer went over. You win!")
elif player_score > dealer_score:
    print("You win!")
elif player_score < dealer_score:
    print("You lose.")
else:
    print("It's a draw.")
