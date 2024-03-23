<details>
    <summary>Python-Week-1</summary>

## Day 1:
### Introduction and Onboarding
I was introduced to the Python course content as well as what is expected of me in the end. Taken through how computers work with regards to memory and how it stores information, how we are able to access it and what happens when we write and run a computer program. I was then taken through installing Python, pip and Jupyter. Jupyter can only be installed using pip, which is the Python package installer which allows us to view most exercise files. Once everything was installed, I ran "jupyter notebook" which opened up the exercise files in the browser and from there I was able to create a new python 3 file which allowed me to run code in python without needing to use the command line. I also installed VS Code and ran the same Python code to see if it also works well on a text editor. Coming into this I was only familiar with VS Code so navigating and understanding Jupyter initially came with a bit of a challenge but I managed to work through it after reading more about it.

### Introduction
This compromised of a knowledge check going over finding the value of a variable when an array was already given and then altered, how a computer reads a comment line in Python and which symbol represents a comment when one is written. I found this questions helpful as they gave me a guide into what I can expect during the Python course. 

## Day 2:
### Variables and Types
I learnt that a **variable** is a basic unit of a program, which is assigned a value. The variable name cannot begin with a number, otherwise, it won't be used but it can include upper and lower case letters, including underscores. I did note that in Python, variable names begin with lowercase letters. Python has several types of variables such as *integers* - whole numbers, *floats* - decimal numbers, *complex numbers* - for complex calculations, *strings* - collections of characters, and booleans - true or false. Strings can be concatenated using a plus sign but cannot be used to add strings and numbers.

### Data Structures
These allow for the storage of a list of values in a single variable. Which are the following: **List** data structure - order is important, can contain any data type, incl. a list within a list and len funtion is used to determine the length, **Set** data structure - similar to a list, contains unique elements, declared by curly braces and order not important. **Tuples** - similar to lists, cannot be modified once declared, useful in storing large amounts of data in an efficient way in memory. **Dictionary** - collections of key-value pairs and are declared using curly braces and accessed using keys.

### Operators
These instructions that perform operations on variables and values by manipulating and performing actions on data. **Addition (+)** - adding things together to get a result and can concatenate two strings, **multiplication (*)** - multiplies numbers together but can also work with a string, **exponent** - raises a number to specified power, **division (/)** - returns floating point value even if the result is a whole number, **modulus (%)** - provides remainder after division e.g. 20/6 remainder 2 returned by modulus.
Other operators include **comparison operators** - evaluate two variables or values and produce boolean result e.g. ==, <, <=, >, >=. **Logical operators ('and', 'or' and 'not')** - 'and' returns true if both operands true, 'or' returns true if at least one operand is true and 'not' negates (reversing the truth value) boolean value it operates on. **Membership operators ('in' and 'not in')** - 'in' to check if a number of a string exits in given list/string.

### Control Flow
If statement allows us to execute a block of code only if a certain condition is met. If a condtion is true, indented code under if statement =  executed, if there's more code and an else statement is added, then the code under that = executed if condition is false. Indentation is very important - determines structure of the program.
- **For loop** - used to iterate over a list of any iterable object.
- **While loop** - similar to for loop but keeps looping until a certain condition is false. Important to make sure condition in while loop will eventually = false or loop will continue indefinitely.

### Functions
Like a machine that takes inputs and produces outputs e.g. toaster takes bread, produces toast. Toaster can still apply toasting function even if bread is not used.
- Defined by using *'def'* keyword followed by function name and arguments in parentheses.
- Can take one or more arguments and may or may not return a value.
- may mutate a variable without returning anything e.g. print function only prints output and doesn't return anything.
- keyword *'None'* represents absence of value, default return value for functions that do not explicitly return anything.

### Classes and Objects
- Class - help label and organize related collections of functions and attributes.
- E.g. a class called has multiple functions and attributes such as legs, a name and bark.
    - special function (init) created and gets called when instance of class is created.
    - init function takes variable called *'self'* which refers to specific instance of the Dog class.
```
class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ' says: Bark!')
```
- Defining attributes and functions of Dog class. E.g. Dog with four legs and has the name 'Rover' and a function called 'speak', which prints 'bark'.
- These attributes or functions in the class can be accessed using 'self' variable.
- Can be used by creating a new instance by calling 'dog' passing other variables such as name.
- Speak function takes 'self' as first variable ---> instance of the class  
    - class instances ---> objects
        - variables inside these classes ---> attributes
            - functions ---> methods.
```
my_dog = Dog('Rover')
another_dog = Dog('Fluffy')

my_dog.speak()

another_dog.speak()
```
### Factorial challenge
Factorial function gives the number of possible arrangements of a set of items of length 'n'
```
E.g. 4! ('four factorial') or ways to arrange four items
* can be calculated as 4 * 3 * 2 * 1
* 5! = 5 * 4 * 3 * 2 * 1 = 120
* 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
* 0! = 1
```
factorial = ! after a number = to the product of that number and all the integers below it down to one.
If type of 'num' is not an integer, we return none, this includes floats e.g. 1.2 and string. Negative numbers such as '-2' are integers but are also special cases, therefore if number < 0, return none.

- Recursion: when a function calls itself directly or indirectly.
    - all same checks performed then return the number multiplied by the factorial of the number minus one.
    - It calls itself, but with a number that's one smaller than before.
    - all checks repeated until input number = 0 and we return one.
    - factorial of the number if returned.
## Day 3:
### Ints and Floats
Division with ints = returns float e.g. 20/4 = 5.0
Returns float to accomodate non-whole numbers and adding a float to an int or multiplying/ using exponents with both = float.

- e.g. 256.0 can be converted to int using int class.
- Casting: converting from one type to another.
      - values like 8.9 casts to 8 and not 9.
      - no rounding when casting floats to ints, just removes the decimal.
      - can use round function when casting to round to nearest int ---> can also specify number of decimal places to round to.

- Floats = approximations resulting in rounding errors.
- stored as binary ones and zeros in memory, due to memory limitations ---> approximations = rounding errors.
- rounding function can mitigate (reduce, alleviate or lesson) this issue.

### Alternate Number Types
If you pass a number in a string, int class = convert to integer e.g. "100" --> 100.
If you pass second argument as a numer, it will convert first argument from that base to base 10. e.g. "100" in base 2 = 4 base 10.
First argument always = **string**
Due to maybe having non-numeric characters in the string that are valid in some bases e.g. "1ab" in base 16. "1ab" is not an integer.
```
int('1ab', 16)
1: 1*16^2, a: 10*16^1, b: 11*16^0
256 + 160 + 11 = 427
```

### Decimals
To use decimal module - import decimal class and the getcontext function. Deccimal class can help instantiate a decimal object with a number value e.g. 1/3 = 0.3333 with four decimals. Pass float as string so no problems are encounted.
```
from decimal import *
getcontext()
getcontext().prec=4 (changing decimal places)
Decimal(1) / Decimal(3)
= Decimal('0.3333')
```
```
getcontext().prec=2
Decimal(1) / Decimal(3)
= Decimal('0.33')
```

### Booleans
* Python casts integers to booleans: 1 = true and 0 = false.
* Anything except 0 = true, even -1 and imaginary 1 = true but float 0 and imaginary 0 = false.
* When it comes to strings: Boolean true = true, anything other than an empty string = true.
* Even "false" = true.
* Only false string is an empty one, with no spaces.
* Can also cast data structures to booleans - empty list or dictionary = false but anything inside = true.
* When non-value returned from a function = false.

### Strings
- Slicing: taking a portion of a string and returning it.
```
name = 'My name is Iron-man'
for first character: name[0] --> 'M'
for second character: name[1] --> 'y'
first 7 characters: name[0:7] --> 'My name'
same result as the one above: name[:7] --> 'My name'
All characters from index 11 to the end of the string: name[11:] --> 'Iron-man'

```

- Few ways to create strings --> string concatenation and f-strings
      - f-strings: allow us to insert variables or expressions inside curly braces in a string. Can also do rounding and number formating.
      - Triple quotes used to create multi-line strings.
      - Back slash used to include literal triple quotes in the strings.


### Bytes
- Data that is passed aroung but rarely modified directly.
- information is stored in ones and zeros.
- raw data = bytes project
- used for streaming files or transmitting texts without knowing the encoding.

- create empty bytes object that's four bytes long e.g bytes(4) --> /x followed by 2 hexadecimal numbers. Each has 8 bits.
    * if b is printed in front --> it's a bytes object.
    * To create bytes object with actual data --> type in utf-8 and can also used decode function to turn a bytes object --> string.
- Bytes objects = immutable like tuples, but can use a byte array if you need to modify the data.
- Can treat it like a string and modify specific byte values using slice notation.
- Can also use int library to convert hexadecimal values back to bytes.



## Day 4:
### Lists
- Slicing used to extract a range of values from a list or string, can also add a third value to control the step size.
- Range function --> generate longer lists (can be sliced)
- Negative values --> used to step backwards through the list.
```
e.g. slicing:
myList = [1,2,3,4,5]
myList[0,6,2] = [1,3,5]

0: starting index of the slice (first element)
6: ending index of slice, exclusive so slice will include elements up to but not including index 6. Since there are only 5 elements in myList, it includes all elements up to the end of the list.
2: step size, which indicates how many elements to skip between each element, included in the slice.

```

- **append() method**: To add an item to the end of a list.
  ```
  e.g. myList = [1,2,3,4]
       myList.append(5)
       print(myList)
  =    [1,2,3,4,5]
  ```
- **insert() method**: To insert an item at a specific position in the list.
  ```
  e.g. myList.insert(3,10) ---> inserting value 10 at position 3.
  ```
- two ways to remove:
  - **remove() method**: removes an item based on its value and not the index. e.g. if we want to remove number 5 from the list ```myList.remove(5)```
  - **pop() method**: removes and returns the item at the end of the list. e.g. ```myList.pop() --> last item removed```
  - can also use a loop with pop() to remove all items from the list. e.g. ``` while len(myList) > 0 and inside loop we can print myList.pop(). After the loop, the list will be empty.```
    
- when assign list to variable, variable stores a reference to the list and not a copy.
- can modify list through one variable, changes reflected in other variables that reference the same list.
- **copy() method**: used to make copy of a list so that changes to one list don't affect the other.
- e.g. ```list with values 1,2,3,4,5 = b = a.copy()``` and then print both a and b to see difference.

### Sets
+ uses curly brackets e.g ```{'a', 'b', 'c'}, mySet or mySet = set(('a', 'b', 'c'))```
+ Commonly used to remove duplicates from a list, since sets only contain unique values.
+ e.g.
  ``` list with duplicate values and de-duplicate by converting to set and back:
  myList = ['b', 'c', 'd']
  mySet = list(set(myList))
  
+ not ordered
+ can't access elements in a set using an index or slicing syntax.
+ **add() function**: used to add elements to a set
+ **discard() function**: used to remove elements

+ **membership operation (in)**: used to check if an element is in a set
+ **length() function**: find the length of a set
+ **pop() function**: removes and returns an arbitrary element from set

### Tuples
- uses parenthesis ()
- ordered
- immutable - can't be modified
- more effecient, better for storing large amounts of data.
- e.g. ``` myTuple = ('a', 'b', 'c')
           myTuple --> ('a','b','c') ```


## Day 5:
### if and Else
- Conditional statements
- allows us to execute a block of code only if a certain condition is met.
-  ```a = true, if a: print it is true``` If condition is true, indented code under if statement will be executed. If else statement added, code under that will be executed, if condition is false.
-  indentation is important.

-  Elif: if the previous conditions were not true = try this condition.

-  if else statements sometimes drag on and you only want to evaluate somthing in a one-liner.
      * use ternary operator: takes in a boolean condition, evaluates it and returns one valuse if true and another value = false.

### While Loops
- Similar to a **for** loop but keeps looping until a certain condition is false.
- ``` a = 0, while a < 5: print a, a = a + 1```
- Important to make sure that condition in the while loop will eventually become false, otherwise loop will continue indefinitely.
  * Break: used to exit a loop early and will move to the next line of code outside of the loop.
  * Continue: used to skip over certain lines within a loop and jumps back to the top of the loop to start the next iteration.
- Sometimes you might use **continue** statement inside an if statement to prevent code in the lopp from running under certain conditions.
- Another way to use **continue** and **break** is to rearrange your code and make it more readable.

### For Loops
- To iterate over a list or any iterable object.
- ```for item in my_List: print item```
    - item in for loop = variable that represents the current item in the list
- You can declare a new variable, like 'item' to hold the value of each element in your list as you iterate through it.
  1. Pass: used to write a stub for a **for** loop.
  2. Continue: used to skip the rest of a loop during a specific iteration.
  3. Break: used to stop the loop early if you founc what you are looking for.
  4. Break-else: used to find prime numbers in just a few lines - can be used with **while** loops.
</details>

<details>
    <summary>Python-Week-2</summary>

 ## Day-1
The basic unit of a program = a function

### Functions
- composed of a name and parameters, denoted by the **def** statement.
 ```
  def performOperation(num1, num2, operation):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2
    
performOperation(2, 3, 'sum')

 ```
### Named Parameters
- can assign our value, 'operation = multiply' to override it.
- can pass in 'multiply' as a third parameter, to call this function.
- use "operation equals multiply" instead of having optional keyword parameters.
```
def performOperation(num1, num2, operation= 'sum', message='Default message'):
    print(message)
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2
    
performOperation(2, 3, message='A new message!', operation='multiply')
```
```
A new message!
6
```
- 'message' argument added with a specific default message is printed when the function is     called.
- when calling function, message is passed before or after operation as long as you specify which argument is which by using a comma to separate everything.

### *args
* *important rule*: keyword arguments must come after positional arguments.
* order of first two arguments is important.
* keyword arguments can be in any order.
* functional limitation to how many variables can be anticipated.
* Use asterisks before argument name: To allow users to pass any number of variables to create a pointer to the inputted variables.
* example below, the function is called with 3 arguments only one is expected and by adding an asterisk before args, Python understands that the variable name is just a reference to the arguments being passed.
```
def performOperation(*args):
    print(args)
performOperation(1,2,3)
```
```
(1, 2, 3)
```
* When a keyword argument is passed you get an error because this only works for positional arguments.
* If keyword argument passed in, an 'unexpected keyword argument' error will occur
```
performOperation(1,2,3, operation='sum')

TypeError: performOperation() got an unexpected keywword argument 'operation'
```
### **kwargs
* used to handle arguments
* print kwargs to see that the keyword arguments are now stored as a dictionary instead of a tuple.
```
def performOperation(*args, **kwargs):
    print(args)
    print(kwargs)
performOperation(1,2,3, operation='sum')
```
```
(1, 2, 3)
{'operation': 'sum'}
```
### Function Scope
* Both *args and **kwargs are used to print our the arguments passed into a function
* Allows us to see a tuple and dictionary of the passed arguments.
* 'locals' function - allows us to access all the variables within a Python function without any asterisks.

#### locals()
- locals: variable names that are only accessible locally within a function.
- Trying to reference a variable outside its scope = error
```
def performOperation(num1, num2, operation='sum'):
    print(locals())

performOperation(1, 2, operation='multiply')
print(num1)
```
```
{'num1': 1, 'num2': 2, 'operation': 'multiply'}
NameError: name 'num1' is not defined
```
- Two variables
  - local variables: defined inside the function
  - global variables: defined outside the function in the main code block. Built-in function 'globals' enables us to retrieve all of these variables.

#### globals()
- results in so many items, some are pre-built in Python.
- can be classified as either global variable scope or local variable scope.

### Global and Local Scope
- Two functions: function 1 with variables A and B, function 2 with variables C and B. Both functions will print out their local variables.
- Function 1 is called with arguments 1 and 2, and function 2 is called with arguments 3 and 4.
- Each function has its *local variable* scope and access to any variables in the *global scope*.
- They can't access each other's data.
```
message = 'Some global data'
def function1(varA, varB):
    print(message)
    print(locals())

def function2(varC, varB):
    print(message)
    print(locals())

function1(1, 2)
function2(3, 4)
```
```
Some global data
{'varA': 1, 'varB': 2}
Some global data
{'varC': 3, 'varB': 4}
```
- The defined variable, 'message' is printed out in both functions but when varA is attempted to be printed in function 2, an error occurs.
- Due to varA only being defined in function 1's local scope.
- If varA is defined in global scope, it can be printed in both functions.
- Python checks for local and global scope when looking up the variables data.
- 'message' can be redefined in function 1's local scope and print both the local and global values of the message.
- A function can also be declared within a function - inner function in function1.
- Inner function can only be called within function one.
- Syntax error - if called outside of function 1.
- When local variables in function 1 are printed, the inner function is defined as a variable.

```
message = 'Some global data'
varA = 2
def function1(varA, varB):
    message = 'Some local data'
    print(varA)
    print(message)
    print(locals())

def function2(varC, varB):
    print(varA)
    print(message)
    print(locals())

function1(1, 2)
function2(3, 4)
```
```
1
Some local data
{'varA': 1, 'varB': 2, 'message': 'Some local data'}
2
Some global data
{'varC': 3, 'varB': 4}
```
### Functions as Variables
#### Variables as Functions
- Variables and functions - have names and data associated with them
- Data includes information about required parameters and the lines of instruction to be executed.
- In Python, a function is represented as an object.

#### Viewing Function Data with __code__
- The "code" attribute of Python function objects can be used to confirm that functions are just variables in Python.
- attribute prints the names and the byte object of all the lines of instruction in a function - not typically used.
```
print(x.__code__.co_varnames)
print(x.__code__.co_code)
```
```
()
b'\x97\x00y\x01'
```
**Note**: Functions are simply variables associated with some data.

#### Text Processing in Python
- Two text processing operations and a function that can make the text lowercase, remove punctuation, new lines and words that are 3 characters or less.
- can also remove long words, by calling the function in a list, the order can be changed or decide which functions to apply.
- allows for flexibility in the order and selection of text processing functions.

#### Lambda Functions





## Day-2

## Day-3
 
 

</details>












