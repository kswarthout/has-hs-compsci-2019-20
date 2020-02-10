# Define a class called Time that records the time of day. The class definition looks like this:
```
class Time:
    '''
    Represents the time of day.
    attributes: hour, minute, second
    '''
```
### Exercise 1  
Write a function called ```print_time``` that takes a ```Time``` object and prints it in the form hour:minute:second. Hint: the format sequence ```'{:02d}'``` prints an integer using at least two digits, including a leading zero if necessary.

### Exercise 2  
Write a boolean function called ```is_after``` that takes two ```Time``` objects, t1 and t2, and returns True if t1 follows t2 chronologically and False otherwise. Challenge: don’t use an if statement.

### Exercise 3
Write a function called ```add_time``` that creates a new ```Time``` object, initializes its attributes to be the sum of two time classes, and returns a reference to the new object. You must accept the time classes as arguments.

### Exercise 4
Write a function called ```increment```, which adds a given number of seconds to a ```Time``` object. The time and seconds should be accepted as arguments.
