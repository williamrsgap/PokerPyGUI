import random

class Player(object):
    def __init__(self, name, initial_chips):
        self.name = name
        self.chips = initial_chips
        self.hand = []

    def bet(self, amount):
        if amount <= self.chips:
            self.chips -= amount
            return amount
        else:
            # Not enough chips to bet, so all-in
            all_in = self.chips
            self.chips = 0
            return all_in

    def receive_cards(self, cards):
        self.hand.extend(cards)

    def reset_hand(self):
        self.hand = []

def main():
    class Card(object):
        def __init__(self, value, suit):
            self.value = value
            self.suit = suit
            
        def __repr__(self):
            value_name = ""
            suit_name = ""
            match(self.value):
                case 0:
                    value_name = "Two"
                case 1:
                    value_name = "Three"
                case 2:
                    value_name = "Four"
                case 3:
                    value_name = "Five"
                case 4:
                    value_name = "Six"
                case 5:
                    value_name = "Seven"
                case 6:
                    value_name = "Eight"
                case 7:
                    value_name = "Nine"
                case 8:
                    value_name = "Ten"
                case 9:
                    value_name = "Jack"
                case 10:
                    value_name = "Queen"
                case 11:
                    value_name = "King"
                case 12:
                    value_name = "Ace"
                case _:
                    value_name = ""
            match(self.suit):
                case 0:
                    suit_name = "Spades"
                case 1:
                    suit_name = "Diamonds"
                case 2:
                    suit_name = "Clubs"
                case 3:
                    suit_name = "Hearts"
                case _:
                    suit_name = ""
            return value_name + " " + suit_name
    
    class DeckInital(list):
        def __init__(self):
            super().__init__()
            suits = list(range(4))
            values = list(range(13))
            [[self.append(Card(i, j)) for j in suits] for i in values]

    def print_player_status(player):
        print(f"{player.name}'s hand: {', '.join(map(str, player.hand))}")
        print(f"{player.name}'s chips: {player.chips}\n")

    def collect_bets(players, current_bet):
        total_bet = 0
        for player in players:
            
            print(f"{player.name}'s turn:")
            print_player_status(player)

            action = input("Choose action (Bet/Call, Raise, Fold, Check): ").lower()

            if action == "fold":
                print(f"{player.name} folds.\n")
            elif action == "check":
                print(f"{player.name} checks.\n")
            elif action in ["bet/call", "raise"]:
                bet_amount = int(input("Enter bet amount: "))
                actual_bet = player.bet(bet_amount)
                total_bet += actual_bet
                current_bet = max(current_bet, actual_bet)
                print(f"{player.name} {action}s {actual_bet}.\n")
            else:
                print("Invalid action. Please choose again.\n")
                continue

        return total_bet, current_bet

    # Currency System
    starting_chips = 2000  # Changed starting chips to 2000
    small_blind = 10
    big_blind = 20

    # Get the number of players
    num_players = int(input("Enter the number of players: "))

    # Initialize players
    players = [Player(f"Player {i+1}", starting_chips) for i in range(num_players)]

    while True:
        # Initialize deck and deal hands
        deck = DeckInital()
        random.shuffle(deck)
        for player in players:
            player.reset_hand()
            player.receive_cards(deck[:2])
            deck = deck[2:]

        # Betting rounds and community cards
        community_cards = []

        for round_num in range(4):
            current_bet = big_blind if round_num == 0 else 0
            total_bet, current_bet = collect_bets(players, current_bet)

            if round_num < 3:
                # Deal community cards
                community_cards.extend(deck[:round_num + 3])
                deck = deck[round_num + 3:]

        # Determine winner and distribute chips
        winner = max(players, key=lambda player: player.chips)
        winner.chips += total_bet

        print(f"{winner.name} wins the round!\n")
        for player in players:
            print_player_status(player)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()