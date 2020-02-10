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

### Exercise 5
Write a function called ```mul_time``` that takes a ```Time``` object and a number and returns a new Time object that contains the product of the original Time and the number.

### Exercise 6
Write a function called ```race_pace``` that takes a ```Time``` object that represents the finishing time in a race, and a number that represents the distance, and returns a Time object that represents the average pace (time per mile). You must use ```mul_time``` in your implementation.

### Exercise 7:

The datetime module provides date and time objects that are similar to the Time class we've been working on, but they provide a rich set of methods and operators.

- Write a ```day_of_week``` function that uses the datetime module to get the current date and prints the day of the week.
- Write a ```next_birthday``` function that takes a birthday as input and prints the user’s age and the number of days, hours, minutes and seconds until their next birthday.
- Write a ```double_day``` function that takes two birthdays and computes their Double Day. For example, for two people born on different days, there is a day when one is twice as old as the other. That’s their Double Day.
