**Coding Guidelines**

A general guideline is to follow the clean code principles for any new code we write or existing code we modify. Also, emphasis is laid on testing. Having a corresponding unit test for every class will make sure the code we have written is actually exercised once before being deployed. This way, we can avoid nasty bugs and make maintenance easier.

Some of the coding guidelines include:
 * Using meaningful names for functions and variables
 * Writing small functions (3-4 lines would be ideal. Max of 10 lines) and having only one purpose in one function
 * Every function, and every block within a function, should have one entry and one return statement
 * Avoid writing duplicate code
 * Follow the ['girl scout'/‘boy scout’](http://programmer.97things.oreilly.com/wiki/index.php/The_Boy_Scout_Rule) rule of leaving the code cleaner than one finds it
 * For indentation, follow the [BSD/Allman style](https://en.wikipedia.org/wiki/Indent_style#Allman_style)
 * Use 4 spaces for indentation in place of hard tabs (does not apply to golang as tabs are recommended there)
