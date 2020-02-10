# Defining Classes

Create classes to represent circles and rectangles in a 2-D space. Then create functions to work with each object type.

## Create the Circle and Rectangle Classes
- Write a definition for a class named `Circle` with attributes `center` and `radius`, where center is a `Point` object and radius is a number.
- Write a definition for a class named `Rectangle` with attributes `width`, `height`, `corner`. corner is a `Point` object that specifies the lower-left corner of the rectangle.

## Create Functions

### Define a main method
Inside main:  
- Instantiate a `Circle` object with its center at (150, 100) and radius 75, then print the circle's center x coordinate
- Instantiate a `Rectangle` object, then print the rectangles's corner x and y coordinates
- Later you will add calls to test additional functions

### Define Functions that accept Objects as Parameters

#### `point_in_circle`
Write a function named `point_in_circle` that takes a Circle and a Point as arguments and returns True if the Point lies in or on the boundary of the circle.

#### `rect_in_circle` 
Write a function named `rect_in_circle` that takes a Circle and a Rectangle and returns True if the Rectangle lies entirely in or on the boundary of the circle. (see image below for example)
#### `rect_circle_overlap`
Write a function named `rect_circle_overlap` that takes a Circle and a Rectangle and returns True if any of the corners of the Rectangle fall inside the circle. (see image below for example)

#### Rectangle / Circle Intersection:  

![Rectangle In Circle](https://github.com/kswarthout/has-hs-compsci-2019-20/master/assignments/classes_and_objects/defining_classes/docs/rect_in_circle.png)
