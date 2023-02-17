# Python Chess

This is an opportunity to explore all of the new class based syntax that Python provides!

## Task

Build a chess engine using Classes.

This should be done using OOP principles. Below is a rough guideline of what each element of the sprint should need and some acceptance criteria. However, much of the implementation is left to you. Remember to, where appropriate, use the tools Python provides you with to build your classes with SOLID principles in mind.

**As always, test your code.**

### **1. Position Class**

You should have a class to represent a `Position`. This will have file (A-H) and rank (1-8) properties. `Position` should also have a `distanceFrom` method that will return the numerical file and rank distances from a given position.

### **2. Piece Class**

You will need to have a `Piece` class that represents a generalised chess piece without any specifics attributed to the behaviour of different piece types. A `Piece` should be a `parent` class and each game piece (knight, queen etc) should be a `child` class.
</br></br>
Each Piece should: -

-   have its constructor take the colour that it should be, and a Rank and File to give it a starting position
-   know its `position` on the board
    -   this `position` should make use of the `Position` class and adhere to its constraints
-   have a `moveTo` method that will act as a setter for its position
-   have a `colour` property
-   have a `captured` property
-   have a `canMoveTo` method
    -   We would recommend `canMoveTo` being a method on the `Piece` class. Each `child` class(pawn, king etc) will have slightly different `canMoveTo` functionality but the method itself should be inherited.
-   have a setter for its `captured` property

### **3. Specific Piece Subclasses**

-   Each of the game pieces will have their own `child` class. They will each have a different `canMoveTo` method and may have extra properties based on their in game functionality. For example a pawn may need a `hasMoved` property to check if it can move 2 spaces on the first move.

Pick a couple of `Piece` `child` classes with different movement behaviours and, once you have implemented them, move on to the `Game` class. You can return and complete the rest later.

## Advanced Tasks

### **1. Game Class**

`Game` should: -

-   have a `makePieces` method that will automatically generate the pieces in their starting positions upon creation
    -   this could be a private static method as the pieces only want to be 'made' once per game as part of instantiating a new game
-   have a `pieces` property that will store all the game pieces
-   have a means to keep track of whose turn it is - `b/w`?
-   have a `makeMove` method that takes a chess notation string and updates the game pieces accordingly
-   have a method to return all the `pieces`

### **2. Piece Child Classes**

-   Complete the remaining `Piece` subclasses.
-   Think about how you are testing and whether you need any extra functionality within these classes.
-   Try to refactor any classes that you think would benefit from stricter adherence to SOLID principles.
