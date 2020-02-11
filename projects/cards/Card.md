# Create a Card Class
Let's create a `Card` class to represent a playing card from a standard 52-card deck in a Python program. See [card.py](card.py) for starter code.

## Attributes
There are two properties we need to keep track of for our `Card` objects, and that is **suit** and **rank**.
- These properties should be passed as arguments to our constructor (the `__init__` method). 
- Use these default values in your decleration: `suit=0, rank=2`. 
- A `Card` object can be instantiated as follows: `queen_of_diamonds = Card(1, 12)`

## Methods
We'll want to include some behavior for our `Card` objects, including a way to print our `Card` objects so people can easily read the encodings, and a way to compare two different instances.

#### `__str__`
The `__str__` method allows us to print a `Card` object in a way people can easily read by allowing us to custom define a string representation. When we call print(card) on a `Card` instance, we want it to display to the console as `<Rank> of <Suit>`, for example: `Jack of Hearts`

We can achieve this by adding **class attributes** *suit_names* and *rank_names* to the `Card` class. These will be lists of strings that contain values that map to our card's encoded suit and rank. 
- Access the appropriate string by indexing into the list using the encoded suit and rank class attributes
- To define **suit_names** use `suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']`
- To define **rank_names** use `rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']`
  - *Note: The first element of rank_names is None because there is no card with rank zero. By including None as a place-keeper, we get a mapping with the nice property that the index 2 maps to the string '2', and so on.*

#### `__lt__`
The `__lt__` method is used to compare two different `Card` objects. It takes two parameters, self and other, and returns True if self is less than other. 

To make your comparison you'll need to consider both suit and rank. This can change depending on the game you are playing, so we'll make the arbitrary choice that suit is more important, so for example, all of the Spades outrank all of the Diamonds, and so on. Here is some pseudocode for how your comparisons can be made:

  ```
  # Check Suits
  if self's suit is greater than other's suit: return False
  if self's suit is less than other's suit: return True
  
  # If Suits are the same, check ranks
  if self's rank is greater than other's rank: return False
  if self's rank is less than other's rank: return True
  
  # If ranks are the same
  return False
  ```
