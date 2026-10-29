# System Design

## `make_number_pyramid` function

1. Create formal parameter for the number of rows from the caller of the function
2. Create a string variable that will be returned. Start as an empty string.
3. Create a loop from 0 to the number of rows (including the number of rows value)
    * Create a string variable for the row of text
    * Create a loop from 0 to the current row number
        * Create a conditional to concatenate a space to the text if it's not the first character of the row
        * Concatenate the row number to the string
    * Add the row of text string to the message variable. Make sure to add a newline at the end
4. Return the string message


## `main` function

1. Get input from the user for the number of rows to print
2. Call `makeNumberPyramid` using the value from the user and save the return
3. Print the return value


## Program start

*Note: You do not need to include this in your future designs as this is implied.*

1. Call the `main` function