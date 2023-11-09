def main():
    class Card(object):
        def __init__(self, value, suit):
            self.value = value
            self.suit = suit
    
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