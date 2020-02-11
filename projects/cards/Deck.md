# Create a Deck Class
Let's create a class to represent a standard 52-card deck.

## Attributes
Since a deck is made up of cards, it is natural for each Deck to contain a list of cards as an attribute.
- Define a class property `cards`. This should be initialized inside the `__init__` method as a list of `Card` objects representing all suits and ranks. 
- You can use a nested for loop to achieve this task (*hint*: There are 4 suits and 13 ranks (1-13). You can use the `range` function in your implementation).

## Methods
We need to include behavior to add, remove, shuffle, sort, and print cards in the deck. Implement the following methods:

### `__str__`
You'll want to include a method that allows us to print the deck to the console, where each card is printed to a new line:
```
10 of Spades
Jack of Spades
Queen of Spades
King of Spades
```
- In your implementation, you'll want to build a return string using a for loop to iterate self.cards.
- *hint*: you can use `\n` in a string to indicate a newline character

### `add_card`
- This method should accept a `Card` object as a parameter and add it to self.cards
- To add a card to the list, we can use the list method [`append`](https://www.w3schools.com/python/ref_list_append.asp)

### `pop_card`
- To deal cards, we would like a method that removes a card from the deck and returns it.
- This can be achieved using the list method [`pop`](https://www.w3schools.com/python/ref_list_pop.asp)
- *Note*: This method must return a `Card` object

### `shuffle`
- This method will shuffle the order of the cards contained in self.cards
- We can use the function [`shuffle`](https://www.w3schools.com/python/ref_random_shuffle.asp) from the random module (*hint*: you'll need to use an import statement)

### `sort`
- This method will sort self.cards from smallest to largest. 
- We can use the list method [`sort`](https://www.w3schools.com/python/ref_list_sort.asp) to achieve this.
- The logic defined in the `Card` class's `__lt__` method will allow comparisons to be made using > and < symbols
