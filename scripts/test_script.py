from model import Deck, RegularCard, DiscardPile, Color

discard_pile = DiscardPile()
discard_pile.place_init_card(card=RegularCard(color=Color.RED, number=7))
discard_pile.place_card(new_card=RegularCard(color=Color.GREEN, number=7))