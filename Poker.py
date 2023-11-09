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
            
    deck = DeckInital() #test code
    for card in deck:
        print(card)
            
if __name__ == "__main__":
    main()