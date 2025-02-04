
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The computer is the dealer.

import random
from art import logo

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player = []
dealer = []
player_score = 0
dealer_score = 0


def draw_card():
    card = cards[random.randint(0, 12)]
    return card


def initial_deck():
    for i in range(0, 2):
        player.append(draw_card())
        dealer.append(draw_card())

    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)

    if player_score > 21:
        return game_end()
    elif dealer_score == 21:
        return game_end()
    else:
        return True


def calculate_score(deck):
    score = 0
    for i in deck:
        score += i
    if score > 21 and 11 in deck:
        change_eleven(deck)
        score = calculate_score(deck)
    return score


def change_eleven(deck):
    for i in deck:
        if i == 11:
            deck[deck.index(11)] = 1
            return deck
    return deck


def print_game():
    player_score = calculate_score(player)
    print(f"Your cards are {player}, current score: {player_score}")
    print(f"Dealer's first card: {dealer[0]}\n")


def final_hand():
    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)
    print(f"Your final hand: {player}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer}, final score: {dealer_score}")


def game_end():
    player_score = calculate_score(player)
    dealer_score = calculate_score(dealer)
    final_hand()

    if player_score > 21:
        print("Bust! Dealer wins!")
        return False
    elif dealer_score > 21:
        print("Dealer busted, you win!.")
        return False
    elif dealer_score == 21:
        print("Dealer has blackjack, Dealer wins.")
        return False
    elif player_score == 21:
        print("Blackjack! You win!")
        return False
    elif player_score == dealer_score:
        print("Draw!")
        return False
    elif player_score > dealer_score:
        print("You win!")
        return False
    elif player_score < dealer_score:
        print("Dealer wins.")
        return False


game_loop = True
while game_loop:
    game = True
    game = initial_deck()

    if game:
        print_game()

        hit_loop = True
        while hit_loop:
            hit = input("Type 'y' to hit, type 'n' to stand: ")
            if hit == "y":
                player.append(draw_card())
                player_score = calculate_score(player)
                print_game()
                if player_score > 20:
                    hit_loop = False
            elif hit == "n":
                hit_loop = False

        dealer_score = calculate_score(dealer)
        if dealer_score < 17:
            dealer_loop = True
            while dealer_loop:
                print("Dealer Draw: ")
                dealer.append(draw_card())
                dealer_score = calculate_score(dealer)
                print(f"Dealer's hand: {dealer}, score {dealer_score}\n")
                if dealer_score > 16:
                    dealer_loop = False

        game_end()

    play_again = input("\nType 'y' to play again, type 'n' to quit: ")
    if play_again == "n":
        game_loop = False
    else:
        player = []
        dealer = []
        player_score = 0
        dealer_score = 0

