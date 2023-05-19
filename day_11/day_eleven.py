
import random

CARD_VALUES = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    user_cards = [random.choice(CARD_VALUES) for _ in range(2)]
    computer_cards = [random.choice(CARD_VALUES) for _ in range(2)]
    return user_cards, computer_cards

def calculate_score(cards):
    score = sum(cards)
    if score == 21:
        return 0
    elif score > 21 and 11 in cards:
        return score - 10
    else:
        return score

def determine_winner(user_score, computer_score):
    if user_score == computer_score:
        print("It's a draw!")
    elif computer_score == 0:
        print("The dealer has a Blackjack. You lose!")
    elif user_score == 0:
        print("You have a Blackjack. You win!")
    elif user_score > 21:
        print("You went over. You lose!")
    elif computer_score > 21:
        print("The dealer went over. You win!")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("You lose!")

def play_game():
    user_cards, computer_cards = deal_cards()
    print(f"Your cards: {user_cards}")
    print(f"Dealer's cards: [{computer_cards[0]}, *]")

    while True:
        user_score = calculate_score(user_cards)
        if user_score == 0 or user_score > 21:
            break

        choice = input("Do you want to hit or stand? ").lower()
        if choice == "hit":
            user_cards.append(random.choice(CARD_VALUES))
            print(f"Your cards: {user_cards}")
        else:
            break

    computer_score = calculate_score(computer_cards)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(random.choice(CARD_VALUES))
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {computer_cards}, final score: {computer_score}")

    determine_winner(user_score, computer_score)

play_game()

