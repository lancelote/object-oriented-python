import random
from typing import TypeAlias
from typing import TypedDict

Rank: TypeAlias = str
Suit: TypeAlias = str
Deck: TypeAlias = list["Card"]


class Card(TypedDict):
    rank: Rank
    suit: Suit
    value: int


SUITS = ("Spades", "Hearts", "Clubs", "Diamonds")
RANKS = (
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Jack",
    "Queen",
    "King",
)
N_CARDS = 8


def get_card(deck_in: Deck) -> Card:
    this_card = deck_in.pop()
    return this_card


def shuffle(deck_list_in: Deck) -> Deck:
    deck_out = deck_list_in.copy()
    random.shuffle(deck_out)
    return deck_out


def create_deck() -> Deck:
    deck = []
    for suit in SUITS:
        for this_value, rank in enumerate(RANKS):
            card = {"rank": rank, "suit": suit, "value": this_value + 1}
            deck.append(card)
    return deck


def main() -> None:
    print("Welcome to Higher or Lower")
    print(
        "You have to choose whether the next card to be shown "
        "will be higher or lower than the current card"
    )
    print(
        "Getting it right adds 20 points; get it wrong and "
        "you lose 15 points."
    )
    print("You have 50 points to start.")
    print()

    starting_deck = create_deck()
    score = 50

    while True:
        print()
        game_deck = shuffle(starting_deck)

        current_card = get_card(game_deck)
        current_rank = current_card["rank"]
        current_suit = current_card["suit"]
        current_value = current_card["value"]

        print(f"Starting card is: {current_rank} of {current_suit}")
        print()

        for card_number in range(N_CARDS):
            answer = input(
                f"Will the next card be higher or lower than the "
                f"{current_rank} of {current_suit}? "
                f"(enter h or l): "
            )
            answer = answer.casefold()
            next_card = get_card(game_deck)
            next_rank = next_card["rank"]
            next_suit = next_card["suit"]
            next_value = next_card["value"]

            print(f"Next card is: {next_rank} of {next_suit}")

            if answer == "h":
                if next_value > current_value:
                    print("You got it right, it was higher")
                    score += 20
                else:
                    print("Sorry, it was not higher")
                    score -= 15
            elif answer == "l":
                if next_value < current_value:
                    print("You got it right, it was higher")
                    score += 20
                else:
                    print("Sorry, it was not higher")
                    score -= 15

            print(f"Your score is {score}")
            print()

            current_rank = next_rank
            current_value = next_value

        again = input("To play again, press ENTER, or q to quit: ")
        if again == "q":
            break

    print("OK bye")


if __name__ == "__main__":
    main()
