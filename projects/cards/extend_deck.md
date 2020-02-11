# Extending Deck's Behavior
Inheritance is a useful feature. Some programs that would be repetitive without inheritance can be written more elegantly with it. Inheritance can facilitate code reuse, since you can customize the behavior of parent classes without having to modify them. Because the following method's can be used by both `Deck` and `Hand` objects, we'll implement them in the `Deck` class, and then inherit this behavior along with any previously defined methods in our child classes.

### `move_cards`
In some games, cards are moved from one hand to another, or from a hand back to the deck. You can use move_cards for any of these operations: self can be either a Deck or a Hand, and hand, despite the name, can also be a Deck.
- move_cards takes two arguments, a `Hand` object and the number of cards to deal.
- inside the method, you should use a loop where on each iteration you add a card to self.card from the `Hand` object

### `deal_hands `
- deal_hands takes two parameters, the number of hands and the number of cards per hand, and that creates new Hand objects, deals the appropriate number of cards per hand, and returns a list of Hand objects.
