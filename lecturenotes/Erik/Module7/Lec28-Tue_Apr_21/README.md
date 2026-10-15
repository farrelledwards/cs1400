CS1400 - Tuesday, April 21 - Lecture 28 - Module 7

# Topics:
* [Two Truths and a Lie Exam Review](#two-truths-and-a-lie-exam-review)


------------------------------------------------------------
# Announcements

## *TONIGHT* FSLC - Playing Archipelago

*   **When**    6:30 PM Tuesday, April 21st
*   **Where**   WIDT 007
*   **Website** https://linux.usu.edu
*   **Discord** https://discord.gg/PvgG6N2hsU

Our final meeting of the semester, and it's going to be a chill one. We'll start up an Archipelago multiworld on this day and play our first couple of hours together! Come unwind from the stress of finals with snacks!


## [Take the IDEA Survey](https://usu.campuslabs.com/eval-home/)

*   We're at a 61% response rate!
*   **The survey closes tonight at 11:59 PM**
*   It's worth 185 points of extra credit



# Final Logistics

*   The final exam opens at 12:00 AM on **Wednesday the 22nd**, and closes at 11:59 PM on **Tuesday the 28th**
    *   This exam covers material from Units 4-7. This exam is proctored by Proctorio. You take this on your own computer. Ensure that you have a quiet space where you will be uninterrupted. Make sure to turn your phone off as well as other things that have pop up notifications (computer/watch/roommates/etc).
    *   You will have **80 minutes** to complete the exam, which is much longer than it takes students on average in previous semesters. Time should not be an issues if you are prepared. This exam is created by taking all quiz questions and then modifying them and/or adding similar questions on related topics. Thus, questions are very similar to what you have seen before.
    *   You are not allowed any outside resources such as notes, books, websites, etc. You much complete this using only what you have stored in your mind.
    *   Now, after all these scary warnings, you should relax. This exam is nothing new as you've taken quizzes every week to prepare you for this. Good luck!
*   My last office hours session will be **Thursday, April 23rd** from 1 PM to 4 PM
*   The IDEA survey extra credit will appear in Canvas sometime **after** the survey closes
    *   I expect it to happen early next week
*   Final grades will be entered following final exams
    *   If your grade isn't as high as you'd like, it is too late to earn more points (even if you are just 1 point below a letter grade boundary)
    *   It is **inappropriate** to ask professors to bump your grade, so please don't ask
    *   I can **fix grading mistakes**; please let me know about it ASAP


# Two Truths and a Lie Exam Review

There are 68 questions on the final exam.  Use this study guide along with the quizzes to prepare.  Good luck!


### Functions and Parameters

```
T: A function definition normally includes a name, a parameter list in parentheses, and a colon at the end of the header
T: The body of a function is the block of indented code that runs when the function is called
F: In Python, any code placed before the def keyword becomes part of the function body automatically
```

```
T: Actual parameters are the values you pass in when you call a function
T: Formal parameters are the variable names listed in the function header
F: The same identifier must be used for both the actual and formal parameter names
```

```
T: When you call a function, Python matches positional arguments from left to right
T: Keyword arguments use the parameter name to decide which value goes where
F: Keyword arguments must always come before all positional arguments in a function call
```

```
T: A return statement can be used to send a result value back to the caller
T: A function that reaches the end of its body without a return statement still finishes normally
F: If a function has no explicit return statement, Python raises a runtime error when it is called
```

```
T: A function may have parameters that provide default values if no argument is given
T: Default values are specified in the function header next to the parameter name
F: Default argument values can only be set inside the function body, not in the header
```


### Function Design and main()

```
T: The main() function is often used as a clear starting point for a program’s execution
T: Grouping the top-level work of a script inside main() can make programs easier to test
F: Python requires every program file to define a main() function or it will not run
```

```
T: When designing a function, you should think about its parameters before writing the formula or algorithm
T: Clearly describing what a parameter represents helps keep the function focused
F: It is best to decide on the return value only after all code has been written and tested
```

```
T: Using several small functions can improve the organization of a program
T: Well–designed functions make it easier to reuse code in multiple projects
F: Breaking code into functions always makes a program run significantly faster
```


### Void Functions and Return Values

```
T: A void function is one whose main purpose is to perform an action rather than compute a value
T: In Python, a function that does not explicitly return a value actually returns the special object None
F: A void function may freely contain more than one return value in the same call
```

```
T: A function can print something and also return a value to its caller
T: The caller decides whether to save or ignore the value that is returned
F: Once a function prints a message, it cannot also execute a return statement
```


### Modules and Imports

```
T: A module is a separate file that can contain functions, classes, and variables for reuse
T: The from m import f syntax allows you to use f without writing the module name first
F: Python automatically imports every file in the current folder whenever your program starts
```

```
T: One advantage of modules is that they help keep code organized by responsibility
T: Putting reusable functions into a module makes them easier to share across programs
F: Functions defined inside a module cannot be tested unless the module is imported into another file
```


### Classes, Objects, and Methods

```
T: A class definition describes the data and behavior that all its objects will share
T: You can create many separate objects from the same class
F: Each object created from a class must be stored in a variable with the same name as the class
```

```
T: The __init__ method is automatically called when you create a new object from a class
T: The first parameter of an instance method in Python is typically named self
F: The __init__ method may not accept any parameters other than self
```

```
T: Instance variables store data that is specific to each individual object
T: Methods can read or modify instance variables using self
F: Local variables defined inside a method are automatically shared by all objects of that class
```

```
T: Two different objects can call the same method and produce different results
T: Differences in each object’s instance variables can lead to different behavior
F: Methods are global functions that are not attached to any particular class
```


### Scope and Variables

```
T: A variable created inside a function is local to that function
T: Code outside a function cannot directly use a variable that was defined only inside the function
F: A local variable keeps its value permanently even after the function ends
```

```
T: Lists and other mutable objects can be changed by a function that receives them as parameters
T: Modifying an element inside a list parameter will be visible to the caller after the function returns
F: Reassigning a new list to the parameter name will always update the original list in the caller
```


### Game Loop and Pygame Concepts

```
T: A typical game loop repeatedly updates game state and then draws the new frame to the screen
T: The update and draw steps usually run many times per second in an animation
F: Once the first frame is drawn in a game, the loop normally stops running
```

```
T: The pygame.key.get_pressed() function provides information about which keys are currently held down
T: pygame.key.get_pressed() returns a sequence of boolean values that can be checked with specific key constants
F: pygame.key.get_pressed() only reports the very last key that was pressed
```

*This is the response that we dediced was incorrect:*

~~`F: Once an image has been blitted, it will stay on the screen forever without any further drawing`~~

*I even tested this on my computer to confirm that a blitted image indeed stays on the screen forever unless and until something is blitted on top of it.  Here is a replacement:*

```
T: In Pygame, the blit method is commonly used to copy an image onto the screen surface
T: The arguments to blit include the image and the position where it should appear
F: Images blitted later appear beneath those blitted earlier
```


### Lists and List Operations

```
T: A list slice like my_list[2:5] creates a new list containing items at indices 2, 3, and 4
T: Leaving off the first index in a slice starts from the beginning of the list by default
F: Slicing a list permanently removes the sliced items from the original list
```

```
T: The split method can be used to turn a string into a list of substrings
T: Converting list elements from strings to integers is necessary before doing arithmetic with them
F: input() automatically returns a list when the user types multiple values separated by spaces
```

```
T: The shuffle function in the random module rearranges the elements of a list in place
T: After shuffling, the list still has the same length as before
F: The shuffle function returns a brand new list and leaves the original list unchanged
```


### Lists as Maps and Multidimensional Lists

```
T: A list can be used as a simple map from numbers to meaningful labels, such as month names
T: Converting a user’s 1-based month number into a 0-based index allows access to the correct list element
F: Accessing a list with index 0 always gives you the second item in the list
```

```
T: A list of lists can be used to store values in rows and columns, like a grid
T: You can access an element in a 2D list by using two indices, such as grid[row][col]
F: All inner lists in a multidimensional list must be exactly the same length
```

```
T: Nested loops are often used to process every value in a multidimensional list
T: An outer loop can iterate over rows while an inner loop handles the values within each row
F: A multidimensional list cannot be created using a literal like [[1, 2], [3, 4]]
```


### UML, Privacy, and List Safety

```
T: UML class diagrams are a tool used to plan out the attributes and methods of classes
T: Designing classes before coding can help prevent major structural mistakes
F: UML is a Python library that must be imported before you can define a class
```

```
T: A private instance variable is intended to discourage direct access from outside the class
T: Requiring methods to control changes to important data can make a class more robust
F: Making a variable private guarantees that no code outside the class can ever reach it
```

```
T: Assigning one list variable directly to another simply makes both names refer to the same list object
T: Making a separate copy of a list can be useful when you plan to modify one version but not the other
F: Removing items from a list while iterating over a copy can never affect the original list
```


