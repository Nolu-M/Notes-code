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

 ## Day 1:
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
* A **parameter** is the variable listed inside the parentheses in the function definition.
* An **argument** is the value that is sent to the function when it is called.
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
* Both *args and **kwargs are used to print out the arguments passed into a function
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
- a way to represent a function without giving it a variable name.
- lambda keyword used to define a small function
```
(lambda x: x + 3)(5)
```
```
8
```
- a lambda function that takes a single parameter x and returns x plus 3
- no need to use the return keyword in lambda functions since it's implied.
- useful when you need to pass a function as an argument to another Python function, such as the sorted function that sorts a list of values.
```
myList = [{'num': 3}, {'num': 2}, {'num': 1}]
sorted(myList, key=lambda x: x['num'])
```
```
[{'num': 1}, {'num': 2}, {'num': 3}]
```

## Day 2:
### Anatomy of a Class
#### Instance Attributes
- Dog class has two attributes: name and legs, which are attributes that every instance of the dog class possesses.
- a new instance, 'Rover', can print its name and legs using 'my_dog.name' and 'my_dog.legs'
- **Note**: we cannot directly see the value of the legs attribute even though it is hardcoded in the dog initialization function. If we try to access 'dogs.legs' = ERROR, and we cannot modify the value of legs.
```
class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ' says: Bark!')

myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)
```
```
Rover
4
```
#### Static Attributes
- Defining something in a static variable outside of the constructor: each instance of the class will have the same value for legs.
- legs attribute can be accessed directly on the class itself by calling dog.<=gs.
- static variables: don't change with each instance, are commonly used to hold constants or fundamental business logic.
```
class Dog:
    legs = 4
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' says: Bark!')

myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)
```
```
Rover
4
```
```
Dog.legs = 4
```
**NB**: static variables can still be changed, to prevent this, an underscore is added before the variable name to indicate the variable should not be modified directly - *getter* method should be used instead.

- Getter method: retrieves the value of the variable, >=t<=gs in this case.
    - does not need to pass in the *self* attribute, because legs is a static variable in the class.
    - method called without passing in *self*, but it is also possible to call it with *self* included.
    - *self* variable: conventional variable name to refer to the class instance.

**Note**: classes have their own variable scope rules. If *self.<=gs* is not set to something else, it references the class variable<=*gs*. The instance variable<=*gs* can also be modified by assigning a new value to *mydog.<=gs*.

### Instance and Static Methods
- clean text method: static method because it does not belong to any particular class instance
- add text: instance method that belongs to a particular instance of the class
- static variables i.e. replace puncs, can also be added to control which punctuations get replaced.
- use the class name or class instance to refer to static variables, but this cannot be done with instance methods.

#### decorators
- special annotation or description for a function definition.
- adding @staticmethod decorator to the function definition, states in Python that the function is a static method and should not have 'self' passed in as an argument.
- allows the use of the function without creating an instance of the class.

### Inheritance
#### Class Inheritance
- One class can inherit all the methods and attributes of another class
- Original class = Parent class
- New class = Child class
- Inheritance process happens automatically when the child class is created.
**NB**: If child class defines an attribute or method that is the same as the parent class, the child's version will overwrite the parent's version.

#### Extending Build-in Classes
- creating a new list can be done by instantiating it as a 'list'.
- although it appears as a function, 'list' = class.

- if you want a list that ensures all appended items are unique, like a set
- create list by extending the list class
- unique list class inherits from the list class and we will override the append function.

- new function: check if item is already in the list --> it will return
- cannot use self.append --> cause infinite recursion or an endless loop
- call original append function in the parent class instead --> 'super' function
- **'super'** function: assess the underlying instance of the parent class and will be called super.append
- e.g. ```super().SetPrice(50) -call a function of its parent class```

- 'super' function can also be used in the constructor.
- new attribute added to child class instance done using ```self.some_property = unique_list```
- This overwrites the constructor of parent class.

- to avoid such, use 'super' again and ensure parent constructor is called first before adding our new property
- when new class initiated = new property added.
  
## Day 3:
### Handling Errors and Exceptions
- when something is divided by zero --> zero division error
- such problems are referred to as errors while other times are called exceptions
- exceptions: determined during runtime and can be retried
- errors: cannot be retried

- All Python errors and exceptions stem from a class called the **basic exception**
- division by zero is a type of arithmetic error --> type of exception --> extends the base exception class.
- base exception class: provides useful and powerful properties to exceptions, i.e. halting code execution and providing information about why and how the execution was halted.

- Can determine the file in which zero division error occurred
- can identify the specific line, line one in this case
- if 1/0 is placed into a function called 'causeError' and then the function is called, the stack trace becomes more elaborate.

- This entire traceback is known as a stack trace.
- it provides a trail through the stack that aids in debugging our program.
- stack trace extended further by adding function called 'callCauseError' that returns 'causeError' function and is called.

```
def causeError():
    return 1/0

def callCauseError():
    return causeError()

callCauseError()
```
```
ZeroDivisionError                         Traceback (most recent call last)
Cell In[2], line 7
      4 def callCauseError():
      5     return causeError()
----> 7 callCauseError()

Cell In[2], line 5
      4 def callCauseError():
----> 5     return causeError()

Cell In[2], line 2
      1 def causeError():
----> 2     return 1/0

ZeroDivisionError: division by zero
```
#### Try/Except
- a zero division error
- exception is can't and will not be raised anymore
- it is a class with attributes that can be created and even returned.
- try block: used to check some code errors i.e. code inside the try block will execute when there is no error in the program
- except block: code inside block will execute whenever the program encounters some error in the preceding try block
- if no exception, then only the try clause will run, except clause is finished
- if exception occurs, try clause will be skipped and except clause will run
- if exception occurs, but ecept clause within the code can't handle it, it is passed on to the outer try statements. *IF exception* left unhandled, then execution stops.
```
try:
    1/0
except Exception as e:
    print(type(e))
```
```
<class 'ZeroDivisionError'>
```
### Managing and Handling Exceptions
- catching the exception and just returning it.
```
def causeError():
    try:
        return 1/0
    except Exception:
        print('There was some sort of error!')
causeError()
```
```There was some sort of error!```
#### Finally
- finally statement: they execute no matter what happens inside this try block
- except statements not needed
- error is thrown, but is still printed
- even if no exception is raised at all, it still executes
- often used when *timing how long a function takes to execute*
- to time our function --> import time class and time
- finally needs to be after everything else, including an 'else' statement, otherwise you'll get a runtime error.
```
import time

def causeError():
    start = time.time()
    try:
        time.sleep(0.5)
        return 1/0
    except Exception:
        print('There was some sort of error!')
    finally:
        print(f'Function took {time.time() - start} seconds to execute')

causeError()
```
```
There was some sort of error!
Function took 0.5015561580657959 seconds to execute
```
#### Catching Exceptions by Type
```
def causeError():
    try:
        return 1 + 'a'
    
    except TypeError:
        print('There was a type error!')
    except ZeroDivisionError:
        print('There was a zero division error!')
    except Exception:
        print('There was some sort of error!')

causeError()
```
```There was a type error!```

- order doesn't matter if general exception moved up --> this is the class from which all of these extend
- always want the most general exceptions at the bottom and the more specific ones up top.
- involved exception handling and catching --> HTTP request-response handling

#### Custom Decorators
```
def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print('There was a type error!')
        except ZeroDivisionError:
            print('There was a zero division error!')
        except Exception:
            print('There was some sore of error!')
    return wrapper

@handleException
def causeError():
    return 1/0

causeError()
```
``` There was a zero division error!```

- decorator handleException, placed in a causeError function returns 1/0
- when causeError is called, this handle exception, is used to accept those various exceptions that this could throw.
- decorator can be reused for another function
- **custom decorator**: changes the name of a function
- allows for the modification of functions or class through their behaviour 

#### Raising Exceptions
- use **handleException** decorator
- a function called raiseError raises Exception
- raise statement raises or throws this new exception that was created when it reached
```
@handleException
def raiseError(n):
    if n == 0:
        raise Exception()
    print(n)

raiseError(1)
```
``` 1 ```

- function excepts any input except the number zero
- else statement not needed: once the exception is raised, execution will halt and throw this exception and then the print n will never be reached.
  
### Working with Custom Exceptions
- class CustomExceptions extends Exception: pass
- pass statement: used because nothing else is defined for our new CustomException class, it inherits the constructor of the Exception class that it is extending

- are usually lightweight classes with very little in the way of special attributes and methods but might have some attributes useful for organizing and presenting information to the user about the error.

#### Adding Attributes
```
class HttpException(Exception):
    statusCode = None
    message = None
    def __init__(self):
        super().__init__(f'Status code: {self.statusCode} and message is: {self.message}')

class NotFound(HttpException):
    statusCode = 404
    message = 'Resource not found'

class ServerError(HttpException):
    statusCode = 500
    message = 'The server messed up!'

def raiseServerError():
    raise ServerError()

raiseServerError()
```
```
ServerError                               Traceback (most recent call last)
Cell In[4], line 19
     16 def raiseServerError():
     17     raise ServerError()
---> 19 raiseServerError()

Cell In[4], line 17
     16 def raiseServerError():
---> 17     raise ServerError()

ServerError: Status code: 500 and message is: The server messed up!
```

- HttpException extends the Exception and is given a status code.
- exception message gets formatted with the status code and message because it extends this HttpException.


## Day 4:
### Fundamentals of Threads and Processes
- computers have both memory and file storage
- long-term memory: save a file and load to a file from the disc
- short-term memory: declare a variable in our program.
- the operating system responsible for allocating memory to each process running on the computer.
    - puts walls between the processes so they cannot access each other's memory.
    - memory: segmented, access is controlled by the operating system.
    - allow us to move these two pieces of code into the same process --> get to share memory.
  
### Multithreading
-	The ability of a processor having multiple threads and executes them at the same time in parallel
-	threads share the same space in memory
-	when the program has periods of **'waiting' and doing nothing**, multi-threading **decreases the runtime of a program**.
-	longSquare: calculates the square of a number but takes a long time to do it.
-	Threads: when waiting to fetch data from a remote server, code is sitting around doing nothing, you can do all the waiting in parallel and not one at a time.
-	```T1 is threading.thread and nd, t2 is threading.thread```
-	Target = name of the target function, longSquare
-	Args = arguments
-	all threads of a process share global variables (stored in heap) and the program code
```
def longSquare(num, results):
    time.sleep(1)
    results[num] = num ** 2

results = {}
t1 = threading.Thread(target=longSquare, args=(1,results))
t2 = threading.Thread(target=longSquare, args=(2,results))

t1.start()
t2.start()

t1.join()
t2.join()

print(results)
```
``` {1: 1, 2: 4} ```

### Multiprocessing
- two Python processes running independently, multi-processing and Python
- can have two separate Python processes running but you have to start by hand
- multiprocessing module is used to start, stop and manage these processes.
- more than one processor being used
```
def longSquare(num, results):
    time.sleep(1)
    print(num ** 2)
    print('Finished computing!')

results = {}
processes = [Process(target=longSquare, args=(n,results)) for n in range(0, 10)]
[p.start() for p in processes]
[p.join() for p in processes]
```
- processes do not share memory
- they get a copy of this dictionary in their own separate memory space, with no way of accessing it except if they record it somewhere i.e. a file system or a database.
- can print the computed value from within the function itself, rather than returning this or saving it in the results, we just print.

- Processes = list
- processes can contain multiple threads
- threads share the same space in memory

- start(): starts a process
- join(): stop execution of current program until process is completed
  
## Day 5:
### Opening, Reading and Writing
#### Reading Files
- two applications making changes to the same file at the same time causes problems
- use open function and pass in the name of the file
- and have a file 10_01_file.txt, second argument = string R.
```
f = open('10_01_file.txt', 'r')
print(f)
```
#### Writing Files
- open the file in read modem prin f = file object
- readline: get the actual text inside the file by reading the lines of the file one at a time (f.readline)
- when run again you get different line each time --> file contains some sort of bookmark of which lines of the file are already read

- lines are double-spaced --> each line of the file has a new line character on it at the end, the print statement also includes its own new line.
- can be fixed by stripping out any leading or trailing white space, including new lines, done with the strip function on each line.

#### Appending files
- use 'W' instead of 'R' for write
- writing to files - an expensive operation, Python makes it more efficient by putting all of the data you are writing to the file in a buffer
- it only writes to the file when that buffer gets full or when the file is closed
- f.close and then run that to close the file
```
f = open('10_01_output.txt', 'a')
f.write('Line 3\n')
f.write('Line 4\n')
f.close()
```
```
with open('10_01_output.txt', 'a') as f:
    f.write('some stuff\n')
    f.write('some other stuff\n')

print(f)
```
``` <_io.TextIOWrapper name='10_01_output.txt' mode='a' encoding='cp1252'> ```

``` f.write('PS. I forgot some stuff') ```
```
ValueError                                Traceback (most recent call last)
Cell In[6], line 1
----> 1 f.write('PS. I forgot some stuff')

ValueError: I/O operation on closed file.
```
### CSV
#### Reading
- CSV file contains tab-separated values, all of these are tabs
- reader object is not a list: it is a csv reader class used as you would use a list an it is iterable
- reader has an internal bookmark that keeps track of where you are
- multiple lines can be called and can also be converted to a list
- header data from Python --> use the dict reader

#### Filtering Data
- converting from reader object to a list object
```
primes = []
for number in range(2, 99999):
    for factor in range(2, int(number ** 0.5) + 1):
        if number % factor == 0:
            break
    else:
        primes.append(number)
```
```
data = [row for row in data if int(row['postal code']) in primes and row['state code'] == 'MA'] 
len(data)
```
### JSON
#### loading JSON
- JSON is not Python
- looks like a dictionary, but it's a string
- turn json string to dictionary --> import JSON module
- json.loads is used to parse a JSON string into a Python object
  
```
jsonString = '{"a":"apple", "b":"bear", "c":"cat"}'
try:
    json.loads(jsonString)
except JSONDecodeError:
    print('Could not parse JSON!')
```
``` Could not parse JSON! ```
                                                 
``` {'a': 'apple', 'b': 'bear', 'c': 'cat',} ```
``` {'a': 'apple', 'b': 'bear', 'c': 'cat'} ```

- JSON string shouldn't have a trailing comma --> JSON decode error

#### Dumping JSON
- use json.dumps method
```
pythonDict = {'a': 'apple', 'b': 'bear', 'c': 'cat',}
json.dumps(pythonDict)
```
``` '{"a": "apple", "b": "bear", "c": "cat"}' ```

#### Custom JSON Decoders
- use JSONEncoder because JSON module can't handle Animal class
- 'o' is the object that's being passed that needs to be decoded into JSON
```
from json import JSONEncoder
class Animal:
    def __init__(self, name):
        self.name = name

class AnimalEncoder(JSONEncoder):
    def default(self, o):
        if type(o) == Animal:
            return o.name
        return super().default(o)
    
pythonDict = {'a': Animal('aardvark'), 'b': Animal('bear'), 'c': Animal('cat'),}
json.dumps(pythonDict, cls=AnimalEncoder)
```
``` '{"a": "aardvark", "b": "bear", "c": "cat"}' ```

</details>

<details>
    <summary> Python-Week-3 </summary>

## Day 1:
### Finding Inspiration
- Developing an application to send a daily email digest, neatly compiling all the information needed in one convenient place.
  
### User Stories
- depicts small scenarios from the user's perspective
- these stories should emphasize the user's goal and motivation rather than the application itself.
- user stories: brief, simple and informal, perfect for jotting down on index cards
- as a [user/role], I want [goal] so that [reason/benefit] format (three core elements).
```
As a digest recipient, I want to receive an email every morning with current and useful information to know what's happening in the world and learn something new daily.
```
*Important*: consider the needs of the administrator role. An admin might want to curate content, control the email's timing and manage the recipient list.

### Use Cases
- typically include a title, an actor (a user or system), and a scenario that describes how a goal is achieved
- scenario can be written as a paragraph or a list of steps
- user stories focus on the who, what and why of a task/goal
- user cases cover the who, what and how of achieving that goal

### Project Requirements
- to capture the capabilities and limitations of an application
- functional requirements: describe what the application should or should not do and are written as sentences starting with "the application must" or "the application shall"
  
- requirements act as a checklist to ensure the application meets all necessary functionalities

- non-functional requirements: describe how the application should accomplish its tasks
- focus on qualities like maintainability, reliability, and usability
```
the application should have a configurable GUI for the admin to interact with, be extensible for adding more content types, and be resilient to content errors
```

### Architecture
- identifying nouns helps determine potential objects
- for instance, in functional requirements, words like quote, forecast, location, trends, article, content, email and recipients stand out as potential objects

- group related nouns together such as content and email, provides a starting point for potential classes
- content, email and GUI emerge as candidates for classes
- behaviours and responsibilities are determined by extracting simplified verb phrases from the requirements, like generating quotes, retrieving forecasts, formatting content, and sending emails.
- These behaviours are assigned to the corresponding classes based on their relevance

- The content class is responsible for generating and retrieving content, the email class handles formatting content and sending emails, and the GUI manages configuration-related behaviours.
- This process helps draft method names and provides an initial structure for the program
  
![image](https://github.com/Nolu-M/Python/assets/119700411/3422a5f5-051c-47c4-9566-d154dad9382b)

### Stub Code
- provides the structure for implementation, allowing for separate development of the email class, independent content functions and the GUI
- 3 Python modules used
    - *dd_content.py*: contains independent functions to retrieve data e.g. random quotes, weather forecasts etc, allowing easy expansion with additional content sources in the future 
    - *dd_email.py*: contains the skeleton for the daily digest email class, with placeholder methods using the pass statement.
      - allows the script to be executed without errors
    - *dd_gui.py*: handles the graphical user interface for the email digest administrator & utilizes *TKinter* module.
      - if name = main section is filled with standard code to build and run the GUI when the module is executed as the main script.

## Day 2:
### Daily Inspirational Quotes
- stored using the CSV format chosen for simplicity
  
- The `get_random_quote` function is implemented.
- function takes named parameter for the quotes file location, default value = quotes.csv
- file loading code is wrapped in a try-except block to handle potential exceptions
- CSV file opened and a list of dictionaries is created using list comprehension
- CSV reader is instructed to use the vertical pipe symbol as the delimiter
- In except block, default quote is defined in case the file fails to load

- random module's 'choice' function: used to select a random quote from the list, which is returned as a dictionary object
- the function is called without an input argument, and the returned quote is printed
- quotes file argument set to None, triggering the exception clause and returning the default quote.

### Weather Forecasting with OpenWeatherMap
- used to fetch weather information from the internet
- two ways:
    - using Python web-scraping library to extract forecast information from a website like weather.com
    - search the Python Package Index for a Python library that can retrieve weather data from an online source or find an online source of weather information that provides API we can directly call from our program = *openweathermap.org*

*Important*: Several Python libraries on pypy.org can retrieve OpenWeatherMap data.

- OpenWeatherMap offers various callable APIs for accessing current and forecast weather information
- must register to obtain an API key

- when accessing forecast API, default format for returned data is JSON
  
### Trending Social media Content (Twitter)

## Day 3:



## Day 4:
### GUI Design Planning
- designed for the admin to have control over the daily digest application
- based on the example: Gui is used to provide users with options to customize their digest email
    - should be able to choose content sources, manage recipients, schedule sending time and configure sender credentials
    - spin boxes: used to select the hour and minute in the 24 hour format

### Exploring Python Tkinter GUI
- GUI module called "dd GUI" is used
- TKinter variables: instantiated to store recipient data, and these variables, along with the frame reference, and are passed to the "build GUI recipients" function that handles creating the GUI widgets.
- all variables are instantiated within the initialization method to easily initialize their values in one place
- the init method also instantiates and starts the scheduler thread and reregisters an event to stop the thread before closin the GUI window.

</details>

<details>
<summary> Data Analytics </summary>

# Data Analytics:
## Introduction and Induction
### The Cape Innovation and Technology Initiative
* non-profit organization established in 1998
* mission: to create a future-proof, inclusive society by using innovation and technology to transform our present and protect our future
* interventions focused on:
  - Entrepreneurial support and ecosystem development: Ecosystem development = a group of different independent businesses create products/services that together make one complete offereing e.g. manufacturing of cars, different companies like glass, paint and tire/rubber manufacturers supply different parts in order to make a car.
  - Digital economy job-readiness
  - Strategic open innovation clutter development: where global economic hot spots occur and new technologies germinate at an astounding rate and where pools of capital, expertise, and talent foster the development of new industries and new ways of doing business.

## Computing with Confidence
### What is a confident computer user?
- one who knows more than just the required key presses to operate the software they are using.
- important qualities:
    - knowing how to cope when things go wrong
    - knowing how to learn computing skills independently

### How to cope when things go wrong?
- personal computiing is changing, need to cope with the changes and unreliability.
    - save work often
    - back up all your important work regularly
    - look for workarounds: if one way doesn't work, look for another
    - built in sources for help
    - develop and use your support network
      
### Learning new Computing Skills
- use websites and Youtube videos
- try out and explore, errors will occur and modern software will warn you and allow you to undo them
- look for patterns, differences/similarities so you can begin to guess what to expect
- learn from others while also offering help

## Module Focus
* domain of data analytics - two primary components:
    * conceptual understanding of data (theoretical aspect)
    * hands-on manipulation of data (practical aspect)
* both components can operate independently
* aim is to extract actionable insighs and valuable information from data
* achieved through coding, low-code platforms or no-code solutions

# Module 1: The Basics of Data
## Chapter 1: The Data Analyst

### What is Data Analytics
- **Data analyst**: transforms raw data into actionable insights that guide decision-making process within an organization.
    1. Data collection and preparation:
          * sourcing data from various channels i.e. databases, spreadsheets, external sources
          * cleaning and organizing the data for accuracy, consistency and readiness for analysis
    2. Data Analysis:
          * statistical methods, machine learning techniques, analytical tools to interpret data
          * identifying trends, patterns and correlations
    3. Data Visualization and Storytelling:
          * creating visual representations of the data i.e. chars, graphs and dashboards to understand complex information easily
          * articulating findings to communicate significance of the data to stakeholders
    4. Decision Support:
          * Making recommendations based on data-driven insights to guide business decisions
          * providing context around the data, and implications and future trends
    5. Collaboration and Communication:
          * working closely with other departments to understand their data needs, provide insights
          * effectively communicate complex data findings clearly and concisely
    6. Continous Learning and Adaptation:
          * keeping up-to-date with latest industry tends, tools and technologies in data analysis
          * Adapting to new types of data and analytical
- goal is to contribute to organization's success by turning data into a valuable asset that informs and drives decision-making

### Welcome to the World of Analytics

Three major pillers that come together to allow analytics to thrive
- data
- storage
- computing power: Moore's Law, we will double the amount of computing power on a single device every two years.
    
### Career in Analytics
Data analysts and scientists are in high demand

### The Analytics Process

1. Data acquision
2. Cleaning and Manipulation
3. Analysis
4. Visualization
5. Reporting and Communication

#### The Analytics Process is Iterative
- *analytics process*: a set of interrelated actions that may be revisited frequently while working with a dataset.
- e.g. analyst reviewing a visualization may notice unusual data points that do not belong in the dataset, causing them to return to the data cleaning stage and rerun their analysis with the newly cleaned dataset
- e.g. analyst running an analysis might discover their analysis woule be enriched by adding another source of data, causing them to return to the acquision stage
- this process helps you understand the different activities that take place during a data analysis and the approximate order in which they typically occur

#### Analytics Techniques
techniques are grouped into categories based on the purpose of the analysis and/or nature of the tool.
- Descriptive Analytics
- Predictive Analytics
- Prescriptive Analytics

#### Machine Learning, Artificial Intelligence and Deep Learning
- *machine learning*: uses algorithms to discover knowledge in your datasets that can be applied to help make informed decisions about the future.
    - segmenting customers, determining the marketing messages that will appeal to different customer groups
    - discovering anomalies in a system and application logs that may be indicative of a cybersecurity incident
    - Forecasting product sales based on market and environmental conditions etc.
  
- *artificial intelligence*: includes any tyoe of technique where you are attempting to get a computer system to imitate human behaviour.
- *maching learning (ML)*: subset of AI techniques, ML techniques attempt to apply statistics to data problems in an effort to discover new knowledge or are AI techniques designed to learn

- *deep learning*: uses complex techniques, known as neural networks, to discover knowledge in a particular way.
- highly specialized subfield of machine learning, commonly used for image, video and sound analysis

### Data Governance
- Data governance programs ensure that the organization has high-quality data and is able to effectively control that data.

#### Analytics Tools
- software helps analysts work through each one of the phases of the analytics process
- tools automate the heavy lifting of data analysis, improving the analyst's ability to acquire, clean, manipulate, visualize and analyze data.
- also provide invaluable assistance in reporting and communicating results
- e.g. Microsoft Excel or Google Sheets (spreadsheet tools)
- e.g. advanced skills: R programming language provides analysts with direct access to their data, but requires basic coding skills

## Chapter 2: Understanding Data

### Exploring Data Types
- *data element*: an attribute about a person, place or thing containing data within a range of values
    - also describe characteristics of activities, including orders, transactions and events
- *data type*: limits the values a data element can have
    - individual data types support structured, unstructured and semi-structured data

#### Tabular Date
- data organized into a table made up of columns and rows
- table represents information about a single topic
- each column represents a uniquely named field within a table, also called a *variable*, about a single characteristic
- contents of each column contain values for the data element as defined by the column header

- think of tabular data as rectangular data, easy to draw a rectangle around the data
- top of the rectandgle is defined by columns, rows define the left side of the rectangle

- intersection of a row and column contains a specific value
- e.g. to identify Hazel's breed, look at where her row intersects with the Breed Name column and see that she is a Labradoodle

- spreadsheets, including Microsoft Excel, Google Sheets and Apple Numbers: practical tools for representing tabular data
- relational database management system (RDMS), called a database: extends the tabular model
- database: organizes related data across multiple tables, connection between tables is known as a *relationship*
- Oracle, Microsoft SQL Server, MySQL and PostgreSQL, examples of database software
- tabular data is the concept underpins both spreadsheets and relational                                                                       
### Structured Data Type
- tabular, organized into rows and columns
- in a spreadsheet, cells are where columns and rows intersect
  
![image](https://github.com/Nolu-M/Python/assets/119700411/592f05b1-300d-448e-b8b0-cc51ada48a8b)

#### Character
- character type limits data entry to only valid characters
- characters can include the alphabet and numbers
- multiple data types are available that can enforce character limits

#### Alphanumeric
- widely used data tyoe for stroing character-based data
- when a data element consists of both numbers and letters
- ideal for storing product stock-keeping units (SKUs), common in retail clothing space for items
- excluding numbers can be achieved using the text data type
- text is subset of aphanumeric, only allowing the storage of alphabetic characters

data types:
* char, varchar2, varchar, CLOB, varchar(max) and LONGTEXT
* CLOB and LONGTEXT: vendor specific

#### Character Sets
- databases use character sets to map or encode, data and store digitally
- individual characters may consume multiple bytes, impacting the length of a character string you can store in a character data type

1. Numeric: databases accomodate two types - *integer* and *numeric*
2. Whole Numbers: integer and all subtypes are for storing whole numbers. Microsoft and MySQL databases support the bit data type, can be empty, or store a 0 or a 1. Flags indicate is something is on or off, on = 1 or true and off = 0 or false. The bit stores status of a flag.
3. Rational Numbers: numeric data type is for rational numbers that include a decimal point. 
4. Date and Time
5. Currency:
    * data storage - contains actual value for a given data element
    * data formating - takes a given data value and then formats it for display purposes, common when dealing with currency and date data types.
    * only Microsoft SQL Server has data types specifically for storing currency
#### Strong and Weak Typing
- strong typing: when technology rigidly enforces data types
- weak typing: loosely enforces data types
    - spreadsheets use weak typing to help make it easier to accomplish work
    - default to an 'automatic' data type and accomodate practically any value
    - when data type is specified, it is loosely enforced compared to a database

### Unstructured Data Types
- any data type that does not fit neatly into the tabular model
- e.g. digital images, audio recordings, video recordings and open-ended survey responses
  
1. *Binary*: supports any digital file, file size = limiting factor, you need to select a data type that is as large as the largest file you plan on stroring.
2. *Audio*: audio is stored in its raw form, consuming the most storage space. It can be encoded with a compression algorithm to reduce the amount of space required and it requires a data type designed to handle raw binary data.
3. *Images*: computer sees images as a binary file stored as ones and zeros, artificial intelligence algorithms for image processing over digital photos allow us to see the images.
    - the greater the resolution, the more detail an image contains and the more storage space it needs
    - storing images in a database requires a data type designed to handle raw binary data i.e. varbinary or BLOB
4. *Video*: resolution and video duration have an impact on the stroage a video consumes
5. *Large Text*: Oracle created CLOB data type to handle large text
   
### Categories of Data
- semi structured data: represents the space between structured speadsheets and unstructured videos
    1. *Quantitative vs Qualitative*:
          * quantitative = numeric values and answers questions like 'how many?', data discrete or continuous e.g. age
          * qualitative = text values and answers questions like 'why?' and 'what?', data is discrete
    2. *Discrete vs Continuous Data*:
          * discrete = measurements that can't be subdivided, useful when you have things to count. **Applies when counting**.
          * continuous = typically need a decimal point, measuring things like height/weight. **Applies when measuring**
    3. *Categorical data*:
          * text data with a known, finite number of categories is categorical e.g. animal type
    5. *Dimensional Data*:
          * dimensional modeling = an approach to arranging data to facilitate analysis and organizes data into fact tables and dimension tables.
          * fact tables store measurement data that is of interest to a business i.e. appointment data table
    
### Common Data Structures

#### Structured Data
* tabular data = structured, values stored in a consistent, defined manner, organized into columns and rows
* method of organization facilitates aggregation and makes summarization easy
* does not translate directly to data quality

#### Unstructured Data
* qualitative, describing the characteristics of an event or an object
* images, phrases, audio or video recordings and descriptive text
* machine data =  common source i.e. smartphones, tablets, personal computers and servers
* object storage facilitates storage of unstructured data
* the key is a unique identifier, value is the unstructured data itself i.e. key = filename, value = contents of the file

#### Semi-Structured Data
* data that has structure and that is not tabular i.e. email
* semi-structured formatting options use separators or tags to provide context around a data element

### Common File Formats
facilitate data exchange and tool interoperability

#### Text Files
- consist of plain text amd are limited in scope to alphanumeric data
- ability to be opened regardless of platform or operating system
- referred to as **flat files**
- when machines generate data, output is stored in a text file

- delimiter = facilitates transmitting structured data via a text file, the character that separates individual fields and can be any character i.e. comma and tab.
- comma-separated values (CSV): when a file is comma-delimited
- tab-separated values (TSV): when a file is tab-delimited

#### Fixed-Width Files
- before delimited files with variable-length columns, flat files were fixed-width
- more laborious to create due to extra steps
- data rows requires you to determine the maximum length of each column, then pad values that are shorter than the max length
- numeric fields = accomplish padding by prepending a leading zero
- alphanumeric/text fields =  done by prepending or appending spaces

#### JavaScript Object Notation
- JavaScript Object Notation (JSON) is an open standard file format, designed to add structure to a text file without incurring significant overhead
- easily readable and easily parsed by modern programming languages
- Python, R and Go have libraries containing functions that facilitate reading/reading JSON files
- R factilitates statistical analysis of data

#### Extensible Markup Language (XML)
- Extensible Markup Language (XML) is a markup language that facilitates structuring data in a text file
- incurs more overhead like JSON because it makes extensive use of tags
- tags: describe a data element and enclose each value for each data element, help readability but add significant amount of overhead
- results in a file roughly double in size
- in 1999, it was the data format of choice and facilitated Asynchronous JavaScript and XML(Ajax) web development techniques.
- AJAX allowed client applications, written in HTML, to retrive data from a server asynchronously, without waiting for server response, the speed with which dynamic web pages operated increased.

#### HyperText Markup Language (HTML)
- a markup language for documents designed to be displayed in a web browser, tag based
- HTML pages serve as the foundation of how people interact with the World Wide Web

# Module 2: Data Preparation and Exploration
## Chapter 3: Databases and Data Acquision

### Exploring Databases 
1. Relational: oldest and most mature databases, excel at stroing and processing structured data
2. Nonrelational: unstructured data

#### Relational Model
- developed in 1969 by IBM's Edgar F. Codd
- builds on the concept of tabular data
- an entity contains data for a single subject, i.e. nouns
- benefits include consistency rollback, stored procedures, locking and concurrency
  
- row = instance of an entity
- the entity relationship diagram (ERD): visual artifact of the data modeling process
    - it shows the connection between related entities
    - a relationship is a connection between entities, symbols adjacent to an entity describe the relationship
 
- cardinality: the relationship between two entities, showing how many instances of one entity relate to instances in another entity
    - specify cardinality in an ERD with various line endings
    - first component of the terminator indicated whether the relationship between two entities is optional or required
    - second component indicates whether an entity instance in the first table is associated with a single entity instance in the related table or if an association can exist with multiple entity instances.

![image](https://github.com/Nolu-M/Python/assets/119700411/961e6486-ab25-417b-8e01-c40f4dc1d944)

    - *unary* relationship: when an entity has a connection with itself (comparatively complex & rare)
    - *binary* relationship: connects two entities (most common & easy to explore)
    - *ternary* relationship: connects three entities e.g. use ticket entity to connect a venue, a performing artist and a price (comparatively complex & rare)

#### Relational Databases
- pieces of software that let you make an operational system out of an ERD
- every row = unique
- relational entities correspond to database tables, and entity attributes correspond to table columns
- when creating tables, order does not matter becuase you can specify the column order when retrieving data from a table
- when an attribute becomes a column, you assign it a data type
- end result = schema (ERD with the additional details needed to create a database)
![image](https://github.com/Nolu-M/Python/assets/119700411/6a45acdf-831b-47cf-9b94-229e1a79ddc5)

- **associative table**: both a table and a relationship e.g. an animal can belong to more that one person
    - lets you identify the relationship between specific animal and a particular person with a minimum amount of data duplication

- **primary key**: one or more attributes that uniquely identify a specific row in a table
    - best to use synthetic primary key: an attribute whose only purpse is to contain unique values for each row

- to link to tables you need a **foreign key**: one or more columns in one table that points to corresponding columns in a related table
    - references another table's primary key
    - enforces referential integrity or how consistent the data is in related tables
- **composite primary key**: a primary key with more than one column
  
- to pull data from a relational database = perform a query, composed using a programming language called Structured Query Language (SQL)
    - query needs to perform a database join to retrieve the data to substitute
    - a join uses data values from one table to retrieve associated data in another table, typically using a foreign key
![image](https://github.com/Nolu-M/Python/assets/119700411/6b6c299a-4cbb-4a09-b3c1-2496b56674b9)

- a database administrator (DBA): a highly trained person who understands how database software interacts with computer hardware
    - looks after how the database uses the underlying storage, memory and processor resources assigned to the database
    - looks for processes that are slowing the entire database down

- use foreign keys to implement data constraints in a database e.g. relationship connecting address with state

- relational database providers:
    - Oracle: released in 1979
    - Microsoft: developed SQL Server, MariaDB and PostgreSQL
    - Amazon Web Services (AWS) developed Aurora, which is compatible with MySQL and PostgreSQL.
      - Aurora = unique, because it takes advantage of AWS's underlying cloud platform and it is easy to scale

#### Nonrelational Databases
- does not have a predefined structure based on tabular data
- flexible, scalable and cost-effective
- data available = absent, therefore, need to know more about the data itself to interact with it
- data validation happens in code as opposed to being done in the database
    1. Key-Value:
          * data stored as a collection of keys and their corresponding values
          * key = globally unique across the entire database, key identifies an individual row in a specific table, can be a sequence of numbers, alphanumeric strings or some other combination of values
          * scalability
          * only way to search is to have the key e.g song = key, audio file = value
    3. Document:
          * similar to a key-value database, with additional restrictions
          * value is restricted to a specific structured format e.g. JSON document
          * more flexible than key-value databases
          * searching using a field within the document is possible
          * document key = profile name
    5. Column-Family:
          * use an index to identify data in groups of related columns
          * e.g. Person_ID becomes index and other columns are stored independently
          * this design facilitates distributing data across multiple machines, enabling handling massive amounts of data
          * ability to handle large data volumes is due to the technical implementation details of how these databases organize and store
          * optimizes performance when examining the contents of a column across many rows
          * scalability benefit
    7. Graph:
          * specialize in exploring relationships between pieces of data
          * e.g. animal and person represent a node in the graph, and each node can have multiple properties
          * properties store specific attributes for an individual node
          * arrow connecting nodes represents a relationship
          * used when you need to create a recommendation engine

            ![image](https://github.com/Nolu-M/Python/assets/119700411/10c83ede-6c49-4975-b92e-02d010659aa8)

### Database Use Cases
- databases support two major categories of data processing;
    1. Online Transactional Processing (OLTP)
    2. Online Analytical Processing (OLAP)

#### Online Transactional Processing
- handle everyday transactions e.g. booking a flight reservation, ordering online or executing a stock trade
- OLTP systems balance the ability to write and read efficiently

#### Normalization
- a process for structuring a database in a way that minimizes duplication of data
- one of the principles: a given piece of data is stored once and only once
- a normalized database is ideal for processing transactions

- first normal form (1NF): when every row in a table is unique and every column contains a unique 
![image](https://github.com/Nolu-M/Python/assets/119700411/f9fb26b8-d8ff-4072-8f9f-548a504c3312)

- second normal form (2NF): starts where 1NF leaves off
- in addition to each row being unique, 2N applies an additional rule = all nonprimary key values must depend on the entire primary key
![image](https://github.com/Nolu-M/Python/assets/119700411/4a0b4db2-0d0c-4bda-a1e2-74a3ee21683f)

- third normal form (3NF)L builds upon 2NF by adding a rule = all columns must depend on only the primary key
- highly normalized databases
![image](https://github.com/Nolu-M/Python/assets/119700411/3cefb6e7-1c8c-490a-bd1a-fa3c743067e3)

#### Online Analytical Processing
- focus on the ability of organizations to analyze data
- have denormalized design
- denormalization results in wider tables than those found in an OLTP database
- more efficient for analytical queries to read large amounts of data for a single table instead of incurring the cost of joining multiple tables together.
- the greater the number of joins = more complex, the more complex = longer it takes to retrieve results

#### Schema Concepts
- data warehouse: a database that aggregates data from many transactional systems for analytical purposes
    - data mart: subset of a data warehouse, data warehouse = serves entire organization and data mart = focuses on the needs of a particular department within the organization
 - data lake: stores raw data in its native format instead of conforming to a relational database structure
    - more complex than a data warehouse or data mart, requires additional knowledge about the raw data to make it analytically useful
    - relational databases enforce structure encapsulating business rules & logic, which are both missing in a data lake

1. Star:
    - facilitates analytical processing, gets its name from what the schema looks like when looking at its entity relationship diagram
    - denormalized to improve read performance over large datasets
    - centre of star = fact table: store numerical facts about a business
    - dimension tables connect directly to the fact table
    - data marts use a star-schema approach
![image](https://github.com/Nolu-M/Python/assets/119700411/96c9bed0-bb28-46e6-b880-a3b4446b3828)
![image](https://github.com/Nolu-M/Python/assets/119700411/aff2a63e-962d-409a-be0f-7da34496fd71)

- when data moves from an OLTP design into a star schem, there is a significant amount of data duplication
- star schema consumes more space than its associated OLTP design to store the same data

2. Snowflake:
    - schema diagram = snowflake
    - central fact table surrounded by dimensions
    - dimensions have subcategories, which give snowflake its shape
    - less denormalized than the star schema
    - need more than one join to get the data you are looking for
    - snowflake schema query more complex than star schema
    ![image](https://github.com/Nolu-M/Python/assets/119700411/506468c5-1263-416b-af91-40d878930e2a)


#### Dimensionality
- refers to the number of attributes a table has, the greater the number, the higher the dimensionality
- dimension table provides additional context around the data in fact tables
- time is a dimension that you will encounter frequently

#### Handling Dimensionality
- start and end approach e.g. using time
- extending the snowflake approach to model dimensions
- use an indicator flag for the current price; requires another column
    - indicator flag method keeps all pricing data in a single place, simplifies the query structure to get the current price. use the current flag = 'Y' instead of doing date math

### Data Acquision Concepts
#### Integration
- extract, transform and load (ETL) as a method to transfer data efficiently and effectively
    1. **Extract**: extract data from the source system and place it in a staging area, goal is to move data from a relational database into a flat file as quickly as possible
    2. **Transform**: transforms data, goal is to reformat the data from its transactional structure to the data warehouse's analytical design
    3. **Load**: purpose is to ensure data gets into the analytical system as quickly as possible
- variant of ETL, with ETL data is extracted from a source database and loaded directly into the data warehouse
- once extract and load phases are complete, transformation phase gets underway
- key difference (ETL & ELT): technical component performing the transformation; ETL: data transformation takes place external to a relational using Python and ELT: uses SQL and the power of a relational database to reformat the data.
- ELT has an advantage in the speed with which data moves from the operational to the analytical database
    - e.g. need to get massive amounts of transactional data into analytical environment as quickly as possible

#### ETL Vendors
- an initial load occurs the first time data is put into a data warehouse, after initial load, each additional load is a delta load: known as incremental load
- delta load only moves changes between systems e.g. delta load below
    ![image](https://github.com/Nolu-M/Python/assets/119700411/f81d6a68-90c8-4eee-a701-16ec9baf136f)
- when moving data between systems, balance the speed and complexity of the overall operation
- e.g. you operate nationally within the US and start processing transactions at 7 in the morning and finish by 7 in the evening, the 12 hours between 7 p.m and 7 a.m represent the batch window or time period available to move data into your data warehouse. The duration of a batch window must be taken into account when designing a delta load strategy

#### Data Collection Methods
* Application Programming Interfaces (APIs)
    * structured method for computer systems to exchange information, provide consistent interface to calling applications
    * can be transactional, returning data as JSON objects, can facilitate bulk data extraction, returning CSV files
* Web Services
    * data is found in private and public data sources and is accessible via a web service
    * web service: an API you can call via HyperText Transfer Protocol (HTTP), the language of the World Wide Web.
    * an API does not have to be a web service e.g. 
* Web Scraping
    * data may not be available internally as an API or publicly via a web service, but may exist on a website
    * web scraping: programmatic retrieval of data from a website
    * can use software bots to scrape data from a website, Python and R make it easy to create a web scraper
    * web scraper reads a web page similar to a browser i.e. Chrome, Safari or Edge and they read and parse the HTML to extract the data the web pages contain
    * must understand how many result pages exist and then iterate through them to harvest the data.
* Human-in-the-Loop
    * you can get insight into competitive pricing by scraping your competitors' websites
* Surveys
    * collecting data from customers by conducting a survey
* Survey Tools
    * instead of designing a custom application to collect survey data, some survey products let you design complex surveys without building a database
    * Qualtrics is a powerful tool for developing and administering surveys, its API can be used to integrate survey response data into a data warehouse for additional analysis
* Observation
    * the act of collecting primary source data from people or machines
    * can be qualitative (leads to unstructured data challenges) or quantitative
* Sampling
    * collecting a sample or subset of the overall population, once collected, statistical methods can be used to make generalizations about the entire population.

### Working With Data 
- Data Definition Language (DDL) components of SQL: allows you to turn a database design into an operational database ready to accept data by allowing you to create, modify and delete tables and other associated database objects.
- a productive analyst needs to generate insights by using the Data Manipulation Language (DML) capabilities of SQL to insert, modify and retrieve information from databases
- DDL: manages structure of a database
- DML: manages the data in the database (components of SQL change very slowly)

#### Data Manipulation
when manipulating data, one of four possible actions occurs:
1. Create new data
2. Read existing data
3. Update existing data
4. Delete existing data

CRUD (Create, Read, Update, Delete)

- SQL uses verbs for type of activity a specific statement performs
- each CRUD activity, there is a corresponding DML verb, known as keywords or words that are part of the SQL language itself.

![image](https://github.com/Nolu-M/Python/assets/119700411/e44222dc-14ca-4dc8-b668-000f9537d9eb)

- syntax of a query, SELECT, FROM AND WHERE are reserved i.e. **SELECT** <what> **FROM** <source> - SQL SELECT statement
- **SELECT**: identifies the columns from the table(s) that are retrieved, if you want to list the name and animal type e.g. ```SELECT Animal_Name, Breed_Name```
- **FROM**: identifies the source of data, frequently a databse table, both SELECT and FROM required for example ```SELECT Animal_Name, Breed_Name FROM Animal```

#### SQL Considerations
- keywords = case-insensitive
- Select Animal_Name, Breed_Name FROM Animal returns the same results as the previous query
- SQL can also span multiple lines

#### Filtering
- a way to reduce the data down to only the rows that you need
- use **WHERE**: to filter data
- NOTE: the column you are filtering on does not have to appear in the SELECT clause eg. retrieve the name and breed for only the dogs ```SELECT Animal_Name, Breed_Name FROM Animal WHERE Animal_Type = 'Dog'```

#### Filtering and Logical Operators
- can use logical operator to account for complex filtering needs
- e.g. need to retrieve the name and breed for dogs weighing more that 60 pounds;
  ```
  SELECT Animal_Name, Breed_Name
  FROM Animal
  WHERE Animal_Type = 'Dog'
  AND Weight > 60
  ```
  - AND operator: evaluates Animal_Type and Weight filters together, only returning records that match both criteria
  - OR operator: e.g. if you want to see the name and breed for all dogs and any animals that weight more than 10 pounds regardless of the animal type
    ```
    SELECT Animal_Name, Breed_Name
    FROM Animal
    WHERE Animal_Type = 'Dog'
    OR Weight > 10
    ```
- complex queries use multiple logical operators at the same time, use parentheses around filter conditions

#### Sorting
- ORDER BY: component of SQL query that makes sorting possible
- no need to specify the columns you are using to sort the data in the SELECT clause
- e.g. want to retrieve the animal and breed for dogs over 60 poubds, with the oldest dog listed first
 ```
 SELECT  Animal_Name, Breed_Name
 FROM   Animal
 WHERE  Animal_Type = 'Dog'
 AND   Weight> 60
 ORDER BY Date_of_Birth ASC
```
- if you want to return the youngest dog first, change the ORDER BY clause to DESC
- ASC and DESC keywords work across various data types, include date, alphanumeric and numeric
  
#### Date Functions
- commonly found in OLAP environments, also appear in transactional systems

#### Logical Functions
- can make data substitutions when retrieving data
- using IFF logical function: ```IFF(boolean_expression, true_value, false_value)```
    1. **Boolean Expression**: must return either TRUE or FALSE
    2. **True Value**: if the Boolean expression returns TRUE, the IFF function will return this value
    3. **False Value**: if the Boolean expression returns FALSE, the IFF function will return this value
```SELECT Animal_Name, IFF(Sex = 'M', 'Male', 'Female') FROM Animal```
- with IFF approach, the values for Male and Female come from the function parameters, not from the source table
- if description in the underlying table gets modified, the results of the IFF query will not reflect the modified data
```SELECT Animal_Name, IFF(Sex = 'M', 'Boy', 'Girl') FROM Animal```
- IFF is just one example of a logical function, when using logical functions you need to balance their convenience with the knowledge that you are replacing data from the database with the function's coded values.

#### Aggregate Functions
- easy way to summarize data
- they summarize a query's data and return a single value
    ![image](https://github.com/Nolu-M/Python/assets/119700411/7a1314cb-d25c-4dc9-b9e2-09779ed03a55)


- can also aggregate functions to filter data
- can also operate across subsets of data

#### System Functions
- frequently used returns the current date
- current date: a component of transactional records and enables time-based analysis in the future

- also return data about the database environment e.g. whenever a person/automated process uses data from a database, they need to establish a database session.
- database session: begins when a person/program connects to a database, session lasts until the person/program disconnects

#### Query Optimization
* Parametrization:
    - SQL query executes, the database has to parse the query
    - parsing translates human-readable SQL into code the database understands, parsing takes time and impacts how long it takes for query to return data
    - effective use of parameterization reduces the number of times the database has to parse individual queries
    - e.g. if people have to login a website then login details serve as parameters to the query to retrieve information for display
    - use a variable name to deal with performance problem, instead of looking for the exact string match for every customer, the query uses a variable called &customer_name.
    ![image](https://github.com/Nolu-M/Python/assets/119700411/d6d282e7-1906-4045-b7f4-1f7cd72e07bb)

* Indexing:
    - when retrieving data from a table, database has to scan each row until it finds the ones that match the filters in the **WHERE** clause.
    - process is looking at each row is called a **full table scan**
    - full table scan is like flipping through every page in a book to find a specific piece of data, the more data volume increases, scanning entire table takes a long time and is not efficient.
    - to speed up query performance = database index, which works like the index at the back of a book to find what you are looking for, using a specific number in the index
    - can point to a single column or multiple columns
    - indexing improves query speed, but slows down create, update and delete actvity, indexing strategy needs to match type of system the database supports, be it transactional or reporting.
* Data Subsets and Temporary Tables:
    - dealing with large data volumes, work with a subset of records
    - possible to create a temporary table to make the data more manageable
    - temporary tables: can store the results of a query and are disposable, get automatically removed when the active session ends
    - using temporary tables effective method of creating subsetsfor ad hoc analysis
    - e.g. can establish a database session, create temporary table with the order history for a single customer, run queries against the temp. table and disconnect from the database, when session disconnects, the database automatically purges any temporary tables created in the session.
* Execution Plan:
    - shows the details of how a database runs a specific query
    - extremely helpful in troubleshooting query performance issues
    - provide additional information about how a query is spending its time e.g. can tell you if a slow-running query uses a full table scan instead of an index scan, in this case, it could be that the query is poorly written and not using the existing indexes or that a column needs a new index.

## Chapter 4: Data Quality
### Data Quality Challenges
- data warehouses aggregate multiple data sources and provide a platform for conducting analysis
- each data source has its own unique quality issues that need resolution before finding its way into a data warehouse
- whether designing an extract, transform and load (ETL) process or digging into a new set of data warehouse tables
- an analyst needs to examine each data source and resolve underlying quality issues

#### Duplicate Data
- occurs when data representing the same transaction is accidentally duplicated within a system.
- e.g. when you double-click on something, the first click is intentional and the second is a duplicate
- to resolve duplicate data is to prevent creation in the first place, a common approach is a visual warning to alert users
- having multiple data sources for the same data elements is also a source of duplicate data
```
e.g. where Allison wants to update her billing address:
She speaks with Jackson, who inputs her address information into the Sales database. After some time, Allison moves and wants to update her billing address. This time, she speaks with Rachel. Instead of updating Allison's existing billing information, Rachel adds a new billing address. At this point, Allison has duplicate data in the Sales system.

To resolve duplicate data issues, the company has a duplicate resolution process. This process looks for customers with multiple billing addresses, validates the correct address, and updates the Sales database by removing the duplicate record.
```
#### Redundant Data
- happens when the same data elements exist in multiple places within a system
- another root cause is an inappropriate database design
- is a function of integrating multiple systems
- resolve redundancy by restructuring the tables
```
For example, multiple source systems that perform different business functions and use shared data elements create the conditions for data redundancy. When a record changes in one system, there is no guarantee that its new value changes in another system. Since there is no certainty of data synchronization, a data element can have conflicting values across systems. When integrating multiple data sources, dealing with redundant data is a persistent challenge.
```
- resolving redundant data, one approach synchronizes changes to shared data elements between the Accounting and Sales systems, however, technical/political realities make synchronizing source systems unfeasible.
- resolving redundancy with an integrated ETL process, this integrated ETL process takes a delta load approach.
- when an address changes, ETL job sets effective end date for old address and inserts a new row for current address, the additional ETL logic ensures that the warehouse contains the correct values
  
#### Missing Values
- occur when you expect an attribute to contain data but nothing is there
- also known as **null values**
- **null value**: the absence of a value, a null is not a space, blank or other character
- some situations where allowing nulls makes sense e.g. if there is a column for Middle Initial, since not everyone has a middle initial, the Middle Initial column should be optional
- when a column optionally contains data, it is nullable, meaning the column can contain null values, although, having nulls in a dataset poses calculation challenges.
- to handle missing values = check for their existence

#### Invalid Data
- values outside the valid range for a given attribute
- an invalid value violates a business rule instead of having an incorrect data type
- e.g. -99.999 is a valid number but an invalid temperature for a location on Earth, programming languages do not have native functions to tell you whether or not a value is invalid, it's up to you as a data professional to work with software developers to create these rules based on the needs of an organization.

#### Nonparametric Data
- data collected from categorical variables
- sometimes the categories indicate differentiation and sometimes they have a rank order associated with them, the rank order of the values is of significance, not the individual values themselves
- e.g. ranking stomach pain from a scale of 0 - 10, 10 being severe pain

#### Data Outliers
- a value that differs significantly from other observations in a dataset
- need to understand why they exist and whether they are valid in the context of your analysis

#### Specification Mismatch
- describes the target value for a component
- occurs when an individual component's characteristics are beyond the range of acceptable values
- in manufacturing, a specification mismatch causes a component to fail post-production quality checks
- when data is invalid, it has values that fall outside a given range
- a specification mismatch occurs when data does not conform to its destination data type e.g. loading data from a file into a database, if the destination column is numeric and you have text data = specification mismatch
- to resolve the mismatch, you must validate that the inbound data consistently maps to its target data type

#### Data Type Validation
- ensures that values in a dataset have a consistent data type
    ![image](https://github.com/Nolu-M/Python/assets/119700411/573c8a72-7c96-4d7a-979e-f95a6ffa8fc3)
- if you want to load the data from the table below into the schema above, the first 9 rows would load successfully, while row 10 fails because the identifier consists of two asterisks, which is not a valid integer.
- how the load process handles the data type validation failure determines whether or not the remaining rows load successfully
- depending on the tool, a single failure may cause the load to stop, alternatively, the load process might write each failed record to an error file before loading the remaining records

    ![image](https://github.com/Nolu-M/Python/assets/119700411/1721e87b-848d-41b2-a924-cf2d41990df5)

- programming languages including SQL, Python and R all have data type validation functions
- use these functions to validate the data type for each column in a data file before attempting a database load.

### Data Manipulation Techniques
#### Recoding Data
- a technique you can use to map original values for a variable into new values to facilitate analysis
- recoding groups data into multiple categories, creating a categorical variable
- useful when you have numeric data you want to analyze by category
- categorical variable = nominal or ordinal
    - nominal variables: any variable with two or more categories where there is no natural order of the categories e.g. hair colour or eye colour
    - ordinal variables: are categories with an inherent rank e.g. t-shirt size = small, medium, large and extra-large. variable values fit into a fixed number of categories.

![image](https://github.com/Nolu-M/Python/assets/119700411/df95b084-eb23-4719-bc6b-3d916f68d984)

#### Derived Variables
- a new variable resulting from a calculation on an existing variable
- e.g. the Pain_Category categorical variable above is an example of a derived variable
- don't have to be categorical

    ![image](https://github.com/Nolu-M/Python/assets/119700411/64a46265-d618-451b-96ba-87ac47ce1c5c)

- storing age as a derived column shouldn't be done as it would need constant updates over time
- you should embed the formula to derive age in code, to avoid potential age-related data errors

#### Data Merge
- uses a common variable to combine multiple datasets with different structures into a single dataset
- merging data improves data quality by adding new variables to your existing data
- ETL processes commonly append data while transforming data for use in analytical environments
- data merge adds columns to a dataset, therefore, gives you additional data about a specific observation
- e.g. getting info on a patient from their dentist, dietician, GP etc.

#### Data Blending
- combines multiple sources of data into a single dataset at the reporting layer
- similar conceptually to ETL process, the ETL process operates on a schedule, copying data from source systems into analytics environments
- differs from ETL in that it allows an analyst to combine datasets in an ad hoc manner without saving the blended dataset in a relational database
- blended dataset exists only at the reporting layer, not in the source databases
- e.g. data visualization tools such as Tableau allow analysts to connect to different source systems and blend the data using a shared attribute
- data blending can reduce the burden on IT as it gives analysts the ability to merge data

#### Concatenation
- the merging of separate variables into a single variable
- highly effective technique when dealing with a source system that stores components of a single variable in multiple columns
- need for concatenation frequently occurs when dealing with date and time data
- useful when generating address information e.g if you want to send an email campaign using first and last names from independent columns, you can concatenate the first and last names together for use in the campaign
    ![image](https://github.com/Nolu-M/Python/assets/119700411/64a357ff-b784-41b8-881a-6b2323396fbc)

#### Data Append
- combines multiple data sources with the same structure, resulting in a new dataset containing all the rows from the original datasets
- when appending data, you save the result as a new dataset for ongoing analysis

#### Imputation
- a technique for dealing with missing values by replacing them with substitutes
- when merging multiple data sources, you may end up with a dataset with many nulls in a given column
- if you are collecting sensor data = possible to have missing values due to collection or transmission issues
- e.g. weight not measured on 4 occasions, few approaches for an analyst:
    1. Removing missing data: removing rows with missing values
    2. Replace with zero: might negatively impact the data
    3. Replace with overall average: compute average weight value for all rows
    4. Replace with most frequent (mode): add the frequently occurring value
    5. Closest value average: use values from the rows before and after missing values

#### Reduction
- the process of shrinking an extensive dataset without negatively impacting its analytical value
- *dimensionality* reduction and *numerosity* reduction are two techniques for data reduction

#### Dimensionality Reduction
- removes attributes from a dataset which reduces the dataset's overall size
  
    ![image](https://github.com/Nolu-M/Python/assets/119700411/efb31d22-a6c1-4460-bbb5-455f1c7bfbe5)

#### Numerosity Reduction
- reduces the overall volume of data
- to reduce the volume of quantitative data by creating a histogram (a diagram made up of rectangles/bars, that show how frequently a specific value occurs)
- when creating a histogram, you can conFigure the width of a rectangle to represent a range of values
- *histograms*: great at reducing the number of data points you have to consider
- can also reduce data through sampling; **sampling**: a technique that selects a subset of individual records from the initial dataset
- most straightforward technique = a random sample and applies in many cases

    ![image](https://github.com/Nolu-M/Python/assets/119700411/84568bac-e8d1-49e4-92f5-a1169725de2d)

1. Aggregation:
    * Data aggregation is the summarization of raw data for analysis
3. Transposition:
    * when you want to turn rows into columns or columns into rows to facilitate analysis
    * when transposing, each value from a column becomes a new column
5. Normalization:
    * converts data from different scales to the same scale
    * if you want to compare columns whose measurements use different units, you want to normalize the data, after normalization is complete, the dataset is ready for statistical analysis
    * e.g. to compare height and weight = you need to scale the data using the min-max normalization technique that sets 0 and 1 as the lower and upper limits for numeric column values.
7. Min-Max Normalization:
    * consider mathematical definition:
      ![image](https://github.com/Nolu-M/Python/assets/119700411/b392e0a5-5280-4a79-a9a5-7353e085fe58)
      
    * ![image](https://github.com/Nolu-M/Python/assets/119700411/6565420f-353e-4f4f-b51c-dc29da406e9c)

9. Parsing/String Manipulation:
    * raw data can contain columns with composite or distributed structural issues
    * composite issue: when a raw data source has multiple distinct values combined within a single character column, when this happens each value in a composite column has data that represents more than one attribute
    * composite columns need to be split into their component parts to aid analysis
       ![image](https://github.com/Nolu-M/Python/assets/119700411/4d0f6363-2f08-4df7-9552-e129f9fc6844)
      
    * can have a distributed structural issue when data in a single column spreads across multiple columns, when this happens, you need to combine the individual columns
    * whenever you have composite or distributed structural data issues = manipulate the strings before starting your analysis.

### Managing Data Quality
#### Circumstances to Check for Quality
- Errors during data acquisition, transformation, manipulation and visualization all contribute to degrading data quality
    1. Data Acquisition
    2. Data Transformation and Conversion
    3. Data Manipulation
    4. Final Product Preparation

  #### Automated Validation
  - one way to prevent data entry mistakes from adversely impacting data quality is to automate data validation checks
  - You first need to understand how source data fields map to their corresponding database columns
  - when mapping input data, pay attention to the data types in the database e.g. you have a web form where customers supply phone numbers and the destination database uses a numeric data type to store phone data
  - if the input form allows for free text entry, someone may enter (312) 555-1212, attempting to insert parentheses and a hyphen into a numeric column results in a database error due to a data type mismatch
  - automating the data type validation before passing the data to the database prevents this from happening.

#### Data Quality Dimensions
- essential to consider multiple attributes of data when considering its quality
- 6 dimensions to take into account:
    1. Data Accuracy,
    2. Data Completeness,
    3. Data Consistency,
    4. Data Timeliness,
    5. Data Uniqueness
    6. Data Validity.

#### Data Quality Rules and Metrics
- data conformity: encompasses elements of accuracy, consistency, uniqueness and validity
- when consolidating data from multiple source systems into an analytics environment ---> assess the conformity or nonconformity of data
- if source data does not match the destination data type, size and format, you have **nonconformity** (presents an ETL challenge).
- to validate a data conformity issue is to confirm how many rows pass successfully to the target environment and how many fail.

#### Methods to Validate Quality
1. Reasonable Expectations
    - determine whether or not the data in your analytics environment meets your reasonable expectations
    - spend time reflecting on what measures are reasonable for your environment, after defining how to measure expectations, automate the reasonable expectation check by creating exception reports as part of your ETL processes
3. Data Profiling
    - uses statistical measures to check for data discrepancies, including values that are missing, that occur either infrequently or too frequently or that should be eliminated
    - can also identify irregular patterns within your data
4. Data Audits
    - look at your data and help you understand whether or not you have the data you need to operate your business
    - use data profiling techniques and can help identify data integrity and security issues
5. Sampling
    - statistical technique in which you use a subset of your data to inform conclusions about your overall data
6. Cross Validation
    - a statistical technique that evaluates how well predictive models perform
    - works by dividing data into two subsets: training set and testing/validation set
    - training set data = build a predictive model, then cross-validate the model using testing/validation
    - helpful in identifying sampling issues, identify sampling bias since predictions using biased data are inaccurate

## Chapter 5: Data Analysis and Statistics
### Fundamentals of Statistics
- census: when you obtain data for every element of your population
- collecting a sample is a cost-effective and time effective alternative to gathering census data
- sample: subset of the population
- a variable: a unique attribute of a data subject; corresponds to a column in a table
- univariate analysis: when you explore the characteristics of a single variable, independent of the rest of the dataset
- an observation: an individual record in a dataset corresponding to a tabular data row
- sample size: the number of observations you select from the population
- a statistic: a numeric representation of a property of a sample; used to infer estimates about the population as a whole e.g. avg height is a statistic
- sample statistic: used to estimate a population parameter
- a parameter: numeric representation of a property for the population; summarize the entire population
- population: a total number of things

#### Common Symbols in Statistics

![image](https://github.com/Nolu-M/Python/assets/119700411/276cabd1-8a8e-48f0-8a08-47eeb56263f3)

### Descriptive Statistics
- a branch of statistics that summarizes and describes data
- when initially exploring a dataset, perfomr univariate analysis to answer questions about a variable's values
- also use descriptive measures to develop summary information about all of a variable's observations.
- this context helps orient you and informs the analytical techniques you use to continue your analysis

#### Measures of frequency
- helps you understand how often something happens
- when encountering a dataset, first understand the size of the datases by counting the number of observations
    1. Count: count the number of observations; understanding the total number of observations is a frequently performed task 
    2. Percentage: a frequency measure that identifies the proportion of a given value for a variable with respect to the total number of rows in the dataset; need total number of observations and the total number of observations for a specific value of a variable
    3. Frequency: describes how often a specific value for a variable occurs in a dataset; typically explored when conducting univariate analysis, use histogram

#### Measures of Central tendency
- to help establish an overall perspective on a given dataset, an analyst explores various measures of central tendency
- used to identify the central, or most typical, value in a dataset
    1. Mean: a measurement of central tendency that computes the arithmetic average for a given set of numeric values; take sum of all values for an observation and divide by the number of observations
    2. Median: identifies the midpoint value for all observations of a variable; sort data numerically and then identify the median 
    3. Mode: a variable's most frequently occurring observation; more applicable when working with categorical data

#### Measures of Dispersion
- used to create context around data spread
    1. Range: the difference between its maximum and minimum values; helps put the data you are looking at into context and can help you determine what to do with outlier values and can also identify invalid values in your data
    2. Distribution: a function that illustrates probable values for a variable and the frequency with which they occur; histograms
    3. Normal Distribution: symmetrically dispersed aorund its mean, give a distinctive bell-like shape (bell curve)
    4. Skewed Distribution: has an asummetrical shape with a single peak and long tail on one side; when skew is to the right, mean > median and if skew is to the left then mean < median
    5. Bimodal Distribution: two distinct modes, multimodal = multiple distinct modes; has two separate peaks
    6. Variance: a measure of dispersion that takes the values for each observation in a dataset and calculates how far away they are from the mean value; indicates how spread out the data is in sqaured units; Bessel's correction specifies that when calculating sample variance you need to account for bias, or error in your sample. When variance is large = observations' values are far from the mean and thus far from each other, small variance = values are close together.
    7. Standard Deviation: a statistic that measures dispersion in terms of how far values od a variable are from its mean; average deviation between individual values and the mean. Also known as the three-sigma rule, the empirical rule states that almost every observation falls within three standard deviations of the mean in a normal distribution. 

#### Each sample if Unique
- take two different samples from a population = variance and standard deviation for each sample will be different. 
    1. Special Normal Distributions: The Central Limit Theorem and empirical rule combine to make the normal distribution in statistics
    2. Standard Normal Distribution: or Z-distribution is a special normal distribution with a mean of 0 and a standard deviation of 1. You can standardize any normal distribution by converting its values into Z-scores, lets you compare normal distributions with different means and standard deviations
   ![image](https://github.com/Nolu-M/Python/assets/119700411/559474f8-97dc-4e97-9c1f-d2f4b7e9cd3e)

    4. Student's T-Distribution: commonly known as the t-distribution, and it similar to the standard normal distribution in that has a mean of 0 with a bell-like shape. There is more area under the tails of the t-distribution than of the normal distribution. degrees of freedom represent the number of values that can vary when calculating a statistic.

#### Measures of Position
- statisticians commonly use quartiles to describe a specific observation's position
- obtaining quartiles is similar to that of determining the median; first sort a numeric dataset from smallest to largest, and divide it positionally into four equal groups
- each grouping = quartile. Fiest quartile is the group that starts with the minimum value, whereas the fourth quartle is the group that starts with the minimum value, whereas 4th quartile is the group that ends the maximum value.
- Interquartile range (IQR): the combination of the 2nd and 3rd quartiles and contains 50% of the values in the data
- using the IQR as a dispersion indicator, in addition tot he range, improves your perspective since the IQR excludes outliers.

### Inferential Statistics
- a branch of statistics that uses sample data to draw conclusions about the overall population

#### Confidence Intervals
- describes the possibility that a sample statistic contains the true population parameter in a range of values around the mean
- when calculating a confidence interval, you end up with a lower bound value and an upper bound value
- given the confidence interval range, the lower bound is the lower limit and the upper bound is the upper limit.
    1. Confidence Interval Considerations:
        * when calculating a confidence interval, you need to specify the confidence level in addition to the sample mean, population standard deviation and sample size
        * based on empirical rule, the confidence level is a percentage that describes the range around the mean, the wider the confidence level, the more confident one can be in capturing the true mean for the sample
        * high confidence levels have a wide confidence interval, while low confidence levels have a narrower confidence interval
        * critical value is a Z-score you specify to denote the percentage of values you want the confidence interval to include
        * also need standard error which measures the standard deviation of the distribution of means for a given sample size, calculated by taking the population standard deviation divided by the sqaure root of the sample size.
    2. Substituting Sample Standard Deviation For Population Standard Deviaion:
        * when calculating confidence intervals you need to have the standard deviation of the entire population
        * getting measures about the whole population is challenging, the population standard deviation is likely unknown
        * if sample size > 30, it's reasonable to use the normal distribution and substitute the sample standard deviation as follows: 

        ![image](https://github.com/Nolu-M/Python/assets/119700411/5df138e6-7c37-4bfe-9d6b-8637d274d5df)

#### Hypothesis Testing
- hypotheis test consists of two statements, only one can be true
- it uses statistical analysis of observable data to determine which of the two statements is most likely to be true
- consists of two components: the null hypothesis and the alternative hypothesis
- when designing a hypothesis test, you first develop the null hypothesis
- **Null hypothesis (H<sub>0</sub>)**: presumes that there is no effect on the test you are conducting
- when hypothesis testing, default assumption = the null hypothesis is valid and that you have to have evidence to reject it
- **Alternative hypothesis (H<sub>a</sub>)**: presumes that the test you are conducting has an effect.
- ultimate goal is to assess whether the null hypothesis is valid or if there is a statistically significant reason to reject the null hypothesis.
- to determine statistical significance of whether to accept or reject the null hypothesis, you need to compare a test statistic against a critical value
- a test statistic: a single numeric value that describes how closely your sample data matches the distribution of data under the null hypothesis
- to get critical value: choose a significance level also known as alpha (a) is the probability of rejecting the null hypothesis when it is true
    ![image](https://github.com/Nolu-M/Python/assets/119700411/59229797-2b5b-4f91-b3ca-b6ae4a1fff23)

    ![image](https://github.com/Nolu-M/Python/assets/119700411/bad03489-f6c3-4546-993b-77a39bb6e4b9)

- once you have a test statistic, you can calculate a p-value; the probability that a test statistic is as or more extreme as your actual results, presuming null hypothesis = true
- two-tailed test: when the alternative hypothesis seeks to infer that something is not equal to the assertion in the null hypothesis
    1. Hypothesis testing with the Z-test: when you have a sample size > 30
    2. Hypthesis testing with the T-test: uses t-distribution instead of standard normal distribution
    3. Hypothesis Testing with Chi-Square: available when you need to assess the association of two categorical variables; null hypothesis asserts that there is no association between the variables and the alternative hypothesis states that there is an association between them.
 
#### Simple Linear Regression
- an analysis technique that explores the relationship between an independent variable and a dependent variable
- can be used to identify whether the independent vaiable is a good predictore of the dependent variable
- can be performed in spreadsheets; when plotting the results of a regression, the independent variable is on the x-axis and the dependent variable is on the y-axis



#### From Simple to Multiple Linear Regression
- multiple linear regression builds on the concept by examining the effect of numerous independent variables on a dependent variable
- crucial aspect --> correlation between how far the observations are from the regression line
- Correlation: a measurement of how well the regression line fits the observations
- correlation coefficient (r) ranges between -1 and 1 and indicates the strength of the correlation; the stronger the correlation, the more tightly the points wind around the line of best fit
- perfect correlation is when **r** has a value of either -` or 1.
- the better the correlation, the stronger the relationship between the independent and dependent variables




    
### Analysis Techniques
#### Determine Type of Analysis
- need to understand the business objectives and desired outcomes; this understanding informs the type of analysis you will conduct
- ensure you have clarity on business at hand; while reviewing requirements, develop a list of clarifying questions
- the list can help define scope of analysis and can also identify any gaps between what is achievable given data source and time constraints
- maintain requirements document as you go about your work, use it track new issues that impact timeline and any adjustments to project scope or ultimate deliverables

#### Types of Analysis
- trend analysis: seeks to identify patterns by comparing data over time
- performance analysis: examines defined goals and measures performance against them and can inform the development of future projections, can identify whether properties are achieving those goals
- combining performance analysis with trend analysis can help develop projections for the future.

#### Exploratory Data Analysis
- when first exploring a dataset, perform an exploratory data analysis
- Exploratory data analysis (EDA): uses descriptive statistics to summarize the main characteristics of a dataset, identify ouliers and give you context for further analysis
    1. Check Data Structure: data is in the coreect format for analysis i.e. tabular format
    2. Check Data Representation: validate data types and ensure variables contain the data expected
    3. Check if Data is Missing: check for missing data
    4. Identify Outliers: determine cause of outliers and consider leaving them or not
    5. Summarize Statistics: calculate summary statistics for each variable e.g. mean, median and variance etc.
    6. Check Assumptions: understand the shape of the data.

# Module 3: Data Analytics and Reporting
## Chapter 6: Data Analytics Tools
### Spreadsheets
- productivity software packages that allow users to create documents that organize any type of data into rows and columns
- lack any of the constraints of a relational database
- That does, of course, reduce the usefulness of the spreadsheet, but the user of spreadsheet software has total flexibility in how they organize their data.
- Microsoft Excel is the most commonly used desktop spreadsheet application.
### Programming Languages
- Programming languages allow skilled software developers to write their own instructions to the computer, allowing them to directly specify the actions that should take place during the analytics process.

#### R
- extremely popular among data analysts because it is focused on creating analytics applications.
- avaiable to everyone as a free, open-source langauge developed by a community of of committed developers
- R redistributable package, offered as open-source code on the Comprehensive R Archive Network (CRAN), a worldwide repository of popular R code.
- the creation of R packages known as the Tidyverse by Hadley Wickham etc.
    - simplifies the use of the language and makes it accessible to anyone willing to invest a few hours in learning some basic syntax.
- RStudionis the IDE used to write, test and deploy code
- a graphical interface provides a well-designed environment to manage your code, monitor its progress, and troubleshoot issues that might arise in your R scripts

![image](https://github.com/Nolu-M/Python/assets/119700411/70d36422-10cc-4ff1-9f4c-83e0ec76b709)

#### Python
- Python is about the same age as R, but Python is a general-purpose programming language
- it is capable of creating software to meet just about any need you might imagine.
- Python also has specialized libraries that focus on the needs of analysts and data scientists.
- In particular, the Python Data Analysis Library (pandas) provides a set of tools for structuring and analyzing data.

#### Structured Query Language (SQL)
- the language of databases, SQL is divided into two major sublanguages:
    1. **The Data Definition Language (DDL)** is used mainly by developers and administrators. It's used to define the structure of the database itself. It doesn't work with the data inside a database, but it sets the ground rules for the database to function.
    2. **The Data Manipulation Language (DML)** is the subset of SQL commands that are used to work with the data inside of a database. They do not change the database structure, but they add, remove, and change the data inside a database.

- three DDL commands:
    1. CREATE: used to create a new table within your database or a new database on your server.
    2. ALTER: used to change the structure of a table that you've already created.
    3. DROP: deletes an entire table or database from your server.

- four DML commands:
    1. SELECT: used to retrieve information from a database.
    2. INSERT: used to add new records to a database table e.g. adding new rows.
    3. UPDATE: used to modify rows in the database.
    4. DELETE: used to delete rows from a database table.

- a developer, administrator, or power user who knows SQL might directly access the database server and send it a SQL command for execution
- happens through a graphical user interface, such as the Azure Data Studio interface
- allows you to write database queries in SQL, send them to the database, and then view the results.

- Azure Data Studio also offer a graphical way for database administrators to reconfigure a database.
- many query and report builder tools are available that simplify database access for end users, allowing them to click through a series of menus and drag objects around on the screen to retrieve data from a database.
- The tool then translates those actions into a SELECT statement that retrieves the desired information from the database.

### Statistics Packages
#### IBM SPSS
- most popular pieces of statistical software is IBM's SPSS package
- one of the oldest statistical software packages, first released in 1968

#### Stata
- dates back to the 1980s
- offers same features as SPSS and SAS and provides users with both a graphical interface and a command-line interface depending on their personal preference.
- less widely used than the more popular SAS and SPSS tools

#### Minitab
- The final statistical software package covered on the Data+ exam is Minitab
- shares most of the same features as SPSS, SAS, and Stata but fits into the same category as Stata - an older tool that is not widely used today

### Machine Learning
- graphical tools are designed to help analysts build machine learning models without requiring them to actually write the code to do so
- aim to make machine-learning techniques more accessible

#### IBM SPSS Modeler
- builds graphical machine learning models
- provides an intuitive interface where analysts can select the tasks they would like the software to carry out and connect them in a flowchart-style interface
  
![image](https://github.com/Nolu-M/Python/assets/119700411/a5940ad5-b620-43fb-8182-5443b9f699f8)

#### RapidMiner
- works in a manner similar to IBM SPSS Modeler
- offers access to hundreds of different algorithms that may be placed in a visually designed machine-learning workflow
- also offers prebuilt analytic templates for common business scenarios
  
![image](https://github.com/Nolu-M/Python/assets/119700411/603069eb-ee6b-4341-ad58-01925ed6b8bf)

### Analytics Suites
- provides powerful capabilities that cross all phases of an analytical process
- the tools allow analysts to ingest and clean data, perform exploratory statistical analysis, visualize their data, produce models, make predictions, and communicate and report their results.

#### IBM Cognos
- uses a web-based platform to offer analysts within an organization access to their data and is backed by IBM's Watson artificial intelligence capability
- major components:
    - **Cognos Connection:** a web-based portal that offers access to other elements of the Cognos suite.
    - **Query Studio:** provides access to data querying and basic reporting tools.
    - **Report Studio:** offers advanced report design tools for complex reporting needs.
    - **Analysis Studio:** enables advanced modeling and analytics on large datasets.
    - **Event Studio:** provides real-time data monitoring and alerting, allowing business leaders to be immediately notified when certain events take place and/or provide automated responses to those events.
    - **Metric Studio:** offers the ability to create scorecards for business leaders to quickly analyze key metrics from across the organization.
    - **Cognos Viewer:** allows stakeholders to easily interact with data and analyses prepared using Cognos.

#### Microsoft Power BI
- major components:
    - **Power BI Desktop:** a Windows application for data analysts, allowing them to interact with data and publish reports for others.
    - The **Power BI service:** Microsoft's software-as-a-service (SaaS) offering that hosts Power BI capabilities in the cloud for customers to access.
    - **Mobile apps:** for Power BI provide users of iOS, Android, and Windows devices with access to Power BI capabilities.
    - **Power BI Report Builder:** allows developers to create paginated reports that are designed for printing, email, and other distribution methods.
    - **Power BI Report Server:** offers organizations the ability to host their own Power BI environment on internal servers for stakeholders to access

#### MicroStrategy
- offers many of the same tools as its counterparts
- making it easy for users to build dashboards and reports and apply machine learning techniques to their business data.

#### Domo
- a *software-as-a-service (SaaS)* analytics platform that allows businesses to ingest their data and apply a variety of analytic and modeling capabilities. 

#### Datorama
- Salesforce Datorama focuses on a specific component of an organization's business: sales and marketing.
- focused on applying machine learning, visualization, and other analytics techniques to the sales and marketing process

#### AWS QuickSight
- a dashboarding tool available as part of the Amazon Web Services cloud offering
- available on a pay-as-you-go basis and its integration with the powerful data storage, data warehousing, machine learning, and artificial intelligence capabilities offered by the Amazon cloud

#### Tableau
- easy ingestion of data from a wide variety of sources and powerful visualization capabilities
- allows analysts and business leaders to quickly identify trends in their data and drill down into specific details

#### Qlik
- popular SaaS analytics platform
- offers access to cloud-based analytics capabilities
- major products offered:
    - **QlikView:** the company's original analytics platform that focuses on providing rapid insights.
    - **Qlik Sense:** a more advanced platform providing more sophisticated analytics capabilities (at a higher cost).

#### BusinessObjects
- an enterprise reporting tool from SAP that is designed to provide a comprehensive reporting and analytics environment for organizations
- has the ability to integrate BusinessObjects reports with other applications, allowing organizations to integrate analytics into other portions of their workflow.

## Chapter 7: Data Visualization with Reports and Dashboards
### Understanding the Business Requirements
- A report is a static electronic or physical document that reflects information at a given point in time
- A dashboard is an interactive visualization that encourages people to explore data dynamically.
- The most important thing to define when developing a report or dashboard is answering the question, “Who is the audience?”
- As an analyst, your job is to ensure that you have access to the appropriate data sources.

- Report parameters let you define data range limits for the data elements in your report
- people who want to access the report digitally --> pull approach
- With a pull approach, you publish a report to a known location, like a web page, and let people know the frequency and timing of when the report updates
- alternatively, push approach --> With a push approach, the report is automatically sent to the appropriate people as it becomes available. When designing a push approach, you need to think through distribution considerations
    - For example, a report may prove to be too large to distribute via email. In that case, you could use a blended distribution approach.
    - blended approach, you store the report centrally and let people know when the report has been updated and is ready for use.
    - With the blended approach, you inform people that the report is available while maintaining central control of the report itself.

### Understanding Report Design Elements
- When creating a report or a dashboard, you can use existing design principles as guideposts
- These design principles, known as the “five Cs” of creating visualizations, will help ensure that your reports and dashboards communicate clearly and efficiently.
    1. **Control** has to do with how you focus the attention of your audience.
    2. **Correctness** makes sure that your information is accurate and that there are no spelling mistakes.
    3. **Clarity** refers to selecting the right visualization tool for communicating your message, making sure the visualization is easy to interpret and visually crisp, and using fonts and sizes that are easy to read.
    4. **Consistency** refers to using the same design and documentation elements throughout your report or dashboard to give your visualization a cohesive and complete feel.
    5. **Concentration** refers to using visuals to focus your audience's attention on the most relevant information without overwhelming them with details.

#### Report Cover Page
-  Since the cover page is the first thing a person sees, it is vital that it sets expectations about the observations and insights the reader will find within.
-  a concise title that describes the contents of the report
-  Ideally, a cover page will also communicate a significant insight from the report itself.
-  Accompanying the title page should be clear instructions on how to use the report.

#### Executive Summary
- The executive summary provides an overview of the report's contents.
- begin with the end in mind, summarizing crucial observations and insights
- With time as an executive's most precious resource, the summary needs to convey the big ideas, while the body of the report details the analysis that led to those ideas

#### Design Elements
- Color schemes, page layout, font size and style, charts, and corporate standards are among the many design elements you should consider.
  
#### Color Schemes
- The first decision to make is whether you need to use a monochromatic color palette or have the flexibility to use more than one color
- A monochromatic palette limits you to working with shades of a single color
- A complementary palette starts with two contrasting colors

#### Layouts
- determines the arrangement of its component parts
- When developing the layout for a report, begin with a summary before diving into the supporting details.
- For a long, multipage report, use a table of contents so that the reader can efficiently navigate to a topic of interest, as well as headings for sections and subsections.
- Use brief paragraphs and bullet points to focus the reader's attention.
- Ensure parallel construction when developing bullet points.
- Parallel construction is when all bullet points use the same form and have the same style and approximate length.

#### Fonts
- When choosing a font style, pick one that is easy for people to read by avoiding ornate fonts
- In typography, a serif is a finishing detail for each letter in a typeface.
- A serif font style includes serifs (the curls), whereas a sans serif font style does not.
- After selecting a font style, determine the appropriate font size for your title, table of contents, headings, subheadings, and body text. 

#### Graphics
- Think through the key chart elements when designing charts, including the chart's title, labels, and legends.
- When developing a chart, make sure you specify a chart title.
- A chart title uses a large font size and concise wording to clearly describe what the chart depicts.
- a label describes what each axis represents.
- When a chart shows multiple categories, use a legend to help the reader distinguish between categories.

### Corporate Reporting Standards
- When developing any type of visualization, be mindful of any existing corporate reporting standards.
- For instance, your organization may have a style guide for reporting.
- A style guide: is a set of standards that drives consistency in communication.
- style guides define the use of a variety of branding elements, including page layout, font selection, corporate color codes, logos, and trademarks.
- Style guides can also incorporate watermarks. Typically, text or a logo, or a watermark is superimposed over a report or web page.
    - If you do not want people to share your visualization outside your organization, you could use an “INTERNAL USE ONLY” watermark

#### Documentation Elements
- To help establish trust, you can incorporate documentation elements, including version numbers, reference data sources, and reference dates.
- Reference dates include the initial creation date, report run date, and data refresh date.

#### Version Number
- a numeric value that refers to a specific version of a report.
- help you keep track of changes to content and layout over time.
- Reference data sources identify where data in the report originates.

#### Reference Data Sources
- help people understand what to expect in terms of data recency

#### Frequently Asked Questions
- When developing a report or a dashboard, it is good to maintain a set of frequently asked questions (FAQs)
- A FAQ provides answers to people's most common questions.

#### Appendix
- use an appendix to include supporting details that are inappropriate to include in the main body

### Understanding Dashboard Development Methods
- are dynamic, their design, development, and delivery mechanisms are more complex than the considerations for developing reports

#### Consumer Types
- C-level executives: CEOs, CFOs (most senior leadership)
- dashboard needs to consolidate critical performance metrics with the ability to get additional detail on an as-needed basis to assist people with C-level responsibilities in making strategic decisions
-  spend sufficient time identifying the key performance indicators (KPIs) crucial to senior leaders
-  KPI: a metric that leadership agrees is crucial to achieving the organization's business objectives.


# Module 4: Data Governance 
## Chapter 8: Defining Data Governance
### Data Governance Concepts
- Data governance: a set of policies, procedures and controls that an organization develops to safeguard its information while making it useful for transactional and analytical purposes.
- Governments have a method of creating, interpreting and enforcing laws, part of this process ensures that these laws are known to the citizenry
- for organizations, data governance is an umbrella term covering the creation, interpretation and enforcement of data use
  
- organizations develop numerous policies to govern their data, these policies promote data quality, specify the use of data attributes and define access to different data domains.
- additional governance policies identify how to secure data, comply with regulations, protect data privacy and deal with data over time.

- an organization invests a significant amount of time and resources to define, develop, implement and control access to data.
- for data governance to succeed, all levels of an organization must appreciate the importance of well-governed data.

#### Data Governance Roles
- stewardship: denotes looking after something, like an organization or property.
- Data stewardship: the act of developing the policies and procedures for looking after an organization's data quality, security, privacy and regulatory compliance.
- organizational data steward/data steward: the person responsible for data stewardship, and is responsible for leading an organizations data governance activities
- works with various data owners to establish policies

- Data owner: a senior business leader with overall responsibility for a specific data domain.
- data domain/data subject area: contains data about a particular operational division within an organization, finance, human resources and physical plant are all examples of operational divisions
- data owners work with the data steward to establish policies and procedures for their data domain.

- subject area data steward: works in the owner's organisation and understand nuances that apply within that organizational unit. Works on behalf of their data owner to handle daily tasks e.g. processing access requests as people rotate in and out of roles is a responsibility a data owner may delegate to their subject area data steward.
- to implement data governance policies, data stewards work with data custodians.

- Data custodian: a role given to someone who implements technical controls that execute data governance policies. Are frequently information technology employees who configure applications, dashboards and databases.
- for example: unique laws govern an organization's finances, people and physical plant.

- Data access requirements determine which people need access to what data. Access requirements differ by data subject area and can be as granular as a single field. e.g. managers need access to details about their employees, including their names and contact information

- data classification matrix: deines categories, descriptions and disclosure implications for data
- vital to consider data classification when considering access requirements to ensure proper data stewardship.

- a data steward works with a data owner to establish broad classifications, with subject area data stewards to develop procedures for granting access to information, and with data custodians to ensure the appropriate technical controls are in place to protect information.

Table 1: sample data classification matrix

#### Access Permissions
- good practice to use role-based access to grant people permission to access data
- role-based access: means that instead of giving access to individual people, you grant access to the role they occupy

- An alternative to role-based access is user-based access, which assigns permissions directly to individuals
- user-based access is dangerous because it increases operational complexity and the potential for mistakes

#### Group Permissions
- best to start visualizing people within an organization when creating data access roles
- An organization chart documents the reporting within an organization and informs how you develop roles.
- when developing a role-based access strategy, it is common to implement user group-based permissions.

#### Data Use Agreements
- a data use agreement (DUA): a contractual document for transferring private data between organizations
- should establish a DUA before sharing data with an outside party and it is essential to understand the classification for each piece of data when crafting a DUA.
- the more sensitive a data element is, the more critical it is to prepare appropriate sharing-related language
- the data sensitivity level should inform your DUA needs

- A DUA provides details governing the transfer, use and disclosure of reporting protocols for the data
    - Identifying who will receive the data
    - Identifying how the data can be used
    - Prohibiting the further distribution of the data
    - Establishing the method of transfer
    - Identifying how the recipient will protect the data

- An Institutional Review Board (IRB): a body that formally reviews and approves any sharing of this data

#### Security Requirements
- encryption: the process of encoding data with a key so that only authorized parties can read it
- encryption key: a series of letters, numbers and symbols used during the encoding process to make data unreadable
- once the data is encrypted, you can only access it by decrypting it with a valid key.

- must encrypt data at rest as well as data in transit
- data at rest is data that exits in permanent storage, locations = databases and flat files.
- e.g. Oracle and Microsoft have Transparent Data Encryption (TDE) as part of their database offering.
- TDE ensures the database files and log files are encrypted and even if an unauthorized party gains access to the database server, the database files themselves are encrypted.
- more challenging to secure flat files, because many of the devices are portable.

- Data in transit: data that is actively moving between one location and another
- during data transmission, you must encrypt the connection between the locations to ensure the data's security

- Transmitting data over the internet uses HyperText Transfer Protocol (HTTP)
- To ensure data security, use Transport Layer Security (TLS) as the cryptographic protocol for encrypting the connection
- adding TLS on top of HTTP = Hypertext Transfer Protocol Secure (HTTPS)

- ETL processes copy data between transactional and analytical systems. When copying files between the transactional and analytical servers, use the Secure Copy Protocol (SCP) or the Secure File Transfer Protocol (SFTP). Both establish an encrypted tunnel to copy data.
- Data masking, or data obfuscation, replaces sensitive information with a synthetic version
- e.g. You may use production data to populate your testing and training environments. While testing or training, using a simulated instead of an actual SSN doesn't diminish the testing or training use case. To protect individual privacy and minimize organizational risk, you can implement a data masking strategy for sensitive information.

- Deidentifying data: The process of removing identifiers that can compromise individual privacy. How you deidentify depends on your use case. One way of deidentifying data is to share only aggregated or summarized data, another way is to remove variables from the data.
- Reidentifying data: this happens when you take de-identified datasets and join them in a way that establishes the identity of individuals.

#### Storage Environment Requirements
- local storage: the storage media on an individual device, such as a hard drive in a laptop. Encrypting local storage - always have the encryption key:
    1. create a password for encrypting the local storage
    2. determine the operating system
    3. use the encryption tool appropriate for the chosen operating system.

- shared drive: where groups of people can collaborate on shared documents. Apart from encrypting the physical media, you need to consider who needs access to the share and the type of access they need. when considering access, you need to think about reading, creating, updating and deleting content.

- user-facing cloud-based storage is similar to a shared drive, except that the contents reside on computers run by the cloud provider instead of an internal IT team.
- By default, cloud storage offerings like Microsoft OneDrive, Google Drive, Box and Dropbx all automatically encrypt files using login credentials.
- when evaluating cloud storage offerings, an organization needs to assess the available administrative controls to minimize the risk of unintended data sharing.

- Amazon Web Services, Microsoft, and Google are three large providers of cloud infrastructure.
- essential to ensure encryption at rest
- consider using a customer-managed encryption key. With a customer-managed key, the cloud service provider can't decrypt and use your data.

#### Use Requirements
- Use requirements: specify how to collect, process, use, store, retain and remove data.
- consider requirements along each stage of the data life cycle from the moment you create data until the point at which it gets removed or archived.
- determining and documenting use requirements at each stage of the data life cycle facilitates effective data governance.

- for data processing, identify where people can work with organizational data. You need to think through data sensitivity, encryption at rest and encryption in transit.

- from a data retention perspective, you need policies that specify how long to keep data. There are legal data retention obligations to consider. i.e. you need to retain tax-related data for seven years.

- In addition to retention, think about data deletion requirements. Once the cost of keeping the data exceeds its value to the organization, you need to govern its removal.

- An acceptable use policy (AUP): defines an individual's responsibilities when accessing, using, sharing and removing organizational data. AUPs describe acceptable locations for storing propriety information; what to do in the event of theft, loss or unauthorized disclosure; and methods of disposal.

#### Entity Relationship Requirements
- Entity Relationship Diagrams (ERDs) give database designers a way of visualizing the relationships between individual entities in a standardized format.
- Implementing foreign keys for the ERD relationships enforces data constraints.
- To avoid data linkage problems, organizations invest in data professionals who design analytical systems. As part of the design process, data architects look for duplicate data across source systems and create linking tables,

#### Data Classification Requirements
- Data classification: the process of analyzing data and organizing it into risk-based categories.
- When classifying data, you put data elements into one of four classifications, similar to those in the data classification matrix.
- Instead of Public, Internal, Sensitive, and Highly Sensitive, you may come across Public, Internal-Only, Confidential, and Restricted.
- it is vital to understand the attributes of each category so that you can make the appropriate category assignment.

- NOTE: South Africa has requirements such as the POPIA (The Protection of Personal Information Act) which governs the law of data protection and privacy in South Africa. The act was passed to regulate the right to privacy, as enshrined by section 14 of the Constitution of South Africa. 
Personally Identifiable Information (PII) is any data that can uniquely identify a person and the information below can be applied to other countries.

1. Personally Identifiable Information:
    * Personally Identiable Information (PII) is any data that can uniquely identify a person. In the United States, the National Institute of Standards and Technology (NIST) defines PII as follows: any information about an individual maintained by an agency, including (1) any information that can be used to distinguish or trace an individual's identity, such as name, social security number, date and place of birth, mother's maiden name, or biometric records; and (2) any other information that is linked or linkable to an individual, such as medical, educational, financial, and employment information.
    * According to NIST, PII falls into two categories: Linked and linkable. Linked PII is data that you can use to uniquely identify someone, including: full name, social security number, date and place of birth, driver's license number, passport number, credit card numbers, addresses, telephone numbers, email addresses and login credentials and passwords.
    * Linkable PII: information that you can use in combination with other identifying information to identify, trace or locate an individual. Data elements like country, province, city, post code, gender, and race are all examples of linkable PII, since you can join that data to identify a perso

2. Protected Health Information:
    * In the United States, the Health Insurance Portability and Accountability Act (HIPAA) is a comprehensive healthcare law that regulates the security and privacy of health data. HIPAA applies to two categories of information.
    * Under HIPAA, Protected Health Information (PHI) is the broad category of data elements identifying an individual's health information. Information can be a individual's past, current or future health status and covers providing healthcare, processing healthcare payments or processing insurance claims. Alternatively, Electronic Protected Health Information, or e-PHI, is any PHI you store or transmit digitally.
    * While HIPAA is a broad regulation, under the Privacy Rule provision, it identifies 18 data elements as PHI: names, All geographic identifiers smaller than a state, including street address, city, county, precinct, and zip code, ates other than year that relate to an individual, including birth date, admission date, date of treatment, etc., telephone numbers, fax numbers, email addresses, social security number, medical record numbers, health plan beneficiaty numbers, account numbers, certificate or license numbers, vehicle identifiers and serial numbers including license plate, device identifiers and serial numbers, web uniform resource locators (URLs), internet protocol (IP) address numbers, biometric identifiers including finger, retinal, voice and facial prints, full-face photographs and other unique identifying number, characteristic or code unless otherwise permitted by the privacy rule for re-identification.
    * PHI has a broad scope by design. However, there are two provisions in place if you need to share medical data without patient consent. The first is Expert Determination, where you use statistical and scientific principles or methods to make the risk of identifying an individual very small. The second is Safe Harbor, where you deidentify a dataset by removing any PHI data elements.
    * The PHI provisions of HIPAA apply only to covered entities. A covered entity is an organization legally obligated under HIPAA to protect the privacy and security of health information. There are three different types of covered entities under HIPAA which are healthcare providers (physicians, hospitals, clinics etc.), health insurance plans and healthcare information clearinghouses.
    * A business associate agreement (BAA) requires that the business partner also complies with HIPAA provisions.
    * exceptions to HIPAA include: employement records, student education that is covered by the Family Educational Rights and Privacy Act (FERPA) and de-identified data.

</details>

<details>
<summary>Data Governance Accelerator</summary>
    
# Chapter 1: Defining Data Governance
## Understanding Data Governance
### What is meant by data governance
- **governance:** the manner in which an entity chooses to oversee the control and direction of an area of interest
- typically takes the form of how decisions are made, regulated and enforced
- when entities grow in complexity, formal governance becomes important. Left ungoverned = chaos
- data governanace is simply about proactively managing the quality of your data to help your organization achieve its strategy and goals (video 1)

### What is data governance
- **NOTE:** governance is the system that formalizes control, processes, and accountabilities so that specific results such as meeting goals or sustaining standards can be attained.
- project governance e.g. focuses on a process for how project decisions are made and hoe communications are managed between stakeholders
- land governance e.g. deals with issues relative to land ownership and the rules under which decisions are made around land use and control

- well-managed data can be transformational and it can support the desirable qualities of a data-driven culture
- this is when decisions at all levels of the organizations are made using data in an informed and structured manner such as that they deliver better outcomes internally and to customers

- risk is minimized, and data compliance and regulatory requirements can be met with ease when there is successful data governance
  
- EIM (enterprise information management): a discipline within an organization that acts in recognition of the value of its information assets (fancy term for data with specific value to an organization, i.e. customer or product record)
- governing and managing data well is a central enabler of EIM, includes using technologies and processes to elevate data to be shared enterprice asset

### Data Governance Versus Data Management
- **data governance** is focused on roles and responsibilities, policies, definitions, metrics, and the lifecycle of data
- **data management** is the technical implementation of data governance e.g. databases, data warehouses and lakes, application programming interfaces (APIs), analytics software, encryption, data crunching, and architectural design anf implementation are all data management features and functions

### Data Governance versus Information Governance 
- **data governance** = focused on data, independent of its meaning e.g. governing the security of patient data and staff data from a policy and process perspective, despite their differences
- **information governance** is concerned with the meaning of the data and its relationship in terms of outcomes and value to the organization, customers and other stakeholders

### The Value of Data Governance
- **NOTE:** data governance is driven by a desire to increase the value of data and reduce the risks associated with it. It forces a leap from an ad hoc approach to data to one that is strategic in nature
- Advantages of good data governance:
    - imrpoved data quality
    - expanded data value
    - increased data compliance
    - improved data-driven decision-making
    - enhanced business performance
    - greater sharing and use of data across the enterprise and externally
    - increased data availability and accessibility
    - improved data search
    - reduced risks from data-related issues
    - reduced data management costs
    - established rules for handling data

- **IMPORTANT:** data governance does not emerge by chance. It's a choice and requires organizational commitment and investment

## Creating a Data Governance Program
- basic steps for creating a data governance program
    - Defining the vision, goals, and benefits
    - Analyzing the current state of data governance and management
    - Developing a proposal based on the first two steps, including a draft plan
    - Achieving leadership approval
    - Designing and developing the program
    - Implementing the program
    - Monitoring and measuring performance
    - Maintaining the program

- achieved through a set of common elements
- most common elements of a data governance program:
  
    ![image](https://github.com/Nolu-M/Python/assets/119700411/eec864ee-fdfd-4e9c-bae8-d8757f079703)

## Developing a Data Governance Framework
- organizations must implement a program relative to its level interest, as well as its needs, budget and capabilities
- **data governance framework:** a basic set of guiding concepts and a structure in which to apply them
- **NOTE:** While there are many framework variations to choose from, including ISACA’s Control Objectives for Information and Related Technologies (COBIT) IT governance framework, they share some common components that address people, processes, and technology.
- common components of a data governance framework (not in a a specific order, exception = leadership and strategy, which is prerequisite for the rest of the framework):

    ![image](https://github.com/Nolu-M/Python/assets/119700411/de7f9e35-9049-4ec9-8753-11babccb7fd5)

### Leadership and Strategy
- data governance program = aligned with the strategy for the organization e.g. how can data governance support the role that data plays in enabling growth in specific markets
- data plays a role in many aspects of organizational strategy, including risk management, innovation and operational efficiencies

### Roles and Responsibilities
- every data governance framework includes the identification and assignment of specific roles and responsibilities, ranging from the information technology (IT) team to data stewards

### Policies, Processed and Standards
- there are policies, process and standards that guide reponsibilities and support uniformity across the organization
- each of these must be designed, developed and deployed
- **IMPORTANT:** Policies, processes, and standards must include accountability and enforcement components; otherwise it’s possible they will be dead on arrival.

### Metrics
- data governance program must have a mechanism to measure whether it is delivering the expected results
- metrics allow us to see if the efforts made are delivering on the promise of the program
- based on the metrics, you and your team can make continuous improvements (or radical changes) to ensure that the program is producing value

### Tools
- tools include for master data management, data catalogs, search, security, integration, analytics and compliance
- ease-of-use and automation = better management and deriving value from data

### Communications and Collaboration
- high-quality communications are key
- it could be in-person meetings, emails, newsletters and workshops
  

## Preparing for Data Governance
- data governance requires careful treatment, beginning with understanding whether an organization is ready to accept it
- involves determing the extent to which a data culture exists
- can conclude that an immature, reactive data culture, where data is simply handled in an adhoc manner, is an entirely different experience than a sophisticated data-driven culture
- prerequisites for data governance include ensuring that the organization's strategy is fully aligned with the proposed program
- any misalignment is the number one reason why data governance program deployements fail

### What is data culture?
- culture will always defeat the greatest strategies almost every time
- e.g. designing and deploying a data governance program for an organization that has little or no data culture
- every organization has some form of a data culture; it just might not be in an ideal state

### Assessing the Data Culture
- increase chances of success = understand the data culture of your organization and determine how to broaden and mature it if necessary (need an environment for success)
- **NOTE:**data culture is how your organization values data and how it manages and uses it. There’s a wide chasm between companies that simply manage data as a consequence of doing business versus those that consider data central to how their organization operates and makes decisions (the latter being the qualities exhibited by a mature data culture).

- effective data cultures support and empower all employees, from newest --> CEO, to access and use meaningful and timely data for their work
- such cultures ensure that employees have attained the skills they need to use data analytics and can make good data-driven decisions

- to succeed, leverage the enormous power and value of data --> this aknowledgement and the actions that senior leaders take to foster the use of data is the primary success factor in the development and maturity of an effective data culture
- trust comes next --> take data-driven decisions if they trust the data they're using, this is built when data is high-quality, its origin and value are understood, team members know how it can contribute to the goals of the business.

- to start --> assess maturity of your organization's data culture, interview leaders and team members
- also observe how people make decisions, how decisions are communicated and the degree to which data is currently governed and managed

## Managing the Data Culture
- consider the following to better prepare the organization for data governance:
    1. help leaders communicate value of data and model the type of behaviour that demonstrates that data is a priority --> must include positive results of using data
    2. Provide basic tools and education for data use that include manipulating dat, analytics, data cleaning, basic query commands and visualization and (spreadsheets)
    3. show progress, even if it's small
    4. resistance & frustration are part of the journey --> find ways to bring comfort and rewards to team members, provide feedback and positive discussion

### Assessing Data Governance Readiness
- basic checklist of items to help determine data governance readiness of organization:
    - basis of data culture exists
    - program is aligned with business strategy
    - senior leadership is committed to the progam and its goals
    - senior leadership understands this is a strategic, enterprise program and not just the IT department
    - one or more sponsors have been identified at an executive level
    - program has the commitment to fund its creation and to maintain it in the long term
    - organization understands this is an ongoing program and not a one-off project
    - return-on-investment (ROI) has been documented
    - legal and compliance teams (internally or externally) understand and support the goals of the program
    - fundamental data skills exist for the data governance journey
    - the IT organization is capable and resourced to support the program


# Chapter 2: Exploring a World Overflowing with Data
## Defining Data
- data governance is not the same as data management

### Why all the focus on data?
- data: refers to collections of digitally stored units; stuff that is kept on a computing device
- these units represent something meaningful when processed for a human or a computer
- datum: single units of data and multiple units of data
- raw data: data in abstract and the most basic form

- data also defined based on its captured format. Specifically, at a high level, it falls into one of the following categories:
    - structured: data that has been formatted to a set structure; each data unit fits into a table in a database and it is ready for analysis.
    - unstructured: data that are stored in a native format must be processed to be used and further work is required to enable analysis
    - semi-structured: data that contains additional information to enable the native format to be searched and analyzed
- data processing term has been replaced with information technology (IT)

## Welcome to The Zettabyte Era
- qualitative and quantitative nature of data types:
    ![image](https://github.com/Nolu-M/Python/assets/119700411/0937778e-74b9-4d6c-9dd5-c96cc65b0771)

- a Zettabyte is a big number. A really big number. It’s 1021, or a 1 with 21 zeros after it. It looks like this: 1,000,000,000,000,000,000,000 bytes.
- by 2020 = 64 zettabytes of data, the number continues to grow
- **datasphere:** used to describe all the data created; projected to reach over 100 zettabytes by 2023 and may double in 3-4 years
- 1 terabyte drive = one billion of those drives to store just one zettabyte of data

- A = 01000001, “hello” converted to binary reads: 01001000 01100101 01101100 01101100 01101111
- Yottabyte and Brontobyte possible in the near future
    ![image](https://github.com/Nolu-M/Python/assets/119700411/af721e91-6a7c-4c4f-8222-ad3b43506e36)

    ![image](https://github.com/Nolu-M/Python/assets/119700411/bf3d0e88-75d3-427f-a2e5-0aafdcaae424)

## From Data to Insight
- the assumption is that you have data for a reason; it must be converted to information to have meaning.
    ![image](https://github.com/Nolu-M/Python/assets/119700411/134f9660-1317-4d6f-b03b-16d2e24f2f0e)

- *knowledge* = information applied coupled with broader contextual concepts, practical application and experience; knowledge is actionable
- *wisdom* = knowledge where reasoning, values, and the broader universe of our knowledge, and deep experiences are applied
    - with wisdom, we know what to do with knowledge --> determine its contextual validity
    - all wisdom includes knowledge, but not all knowledge is wisdom
- *insight* = an outcome that can emerge from knowledge but is best demonstrated through a combination of knowledge and wisdom
```
                            INSIGHT
                              |
Ensuring that Columbia Records make the decision to sign Harry Styles before anyone else does
                              |
                           WISDOM
                              |
One Direction was a very successful band with talented and popular individuals,
and knowing that Harry Styles is a creative artist who now wants a solo record deal
                              |
                         KNOWLEDGE
                              |
Harry Styles has aspirations to become a solo artist and is looking for a record deal
                              |
                        INFORMATION
                              |
Harry Styles is a singer and was in the group, One Direction
                              |
                            DATA
                              |
                        Harry Styles
```
![image](https://github.com/Nolu-M/Python/assets/119700411/898cc7a3-0cda-40e1-bf43-13b2b26a2b04)

![image](https://github.com/Nolu-M/Python/assets/119700411/4581317e-0d79-4dcc-bf63-663e44e74507)

## The Role of Data in the 21st Century
- the value of data that has been added over many decades has not remained flat
- since mid-20th century, as more computers came online = role of data has grown
- both quantity and quality of data have increased and the availability of it to so many people
- the arrival of the internet in the mid-1990s resulted in the reality of the Information Industry Association's 1970's motto, "Putting information at your fingertips."
- In the late 1980s, Bill Gates, co-founder and former CEO of Microsoft would later build on this and champion the idea that eventually, “any piece of information you want should be available to you.” 
- **NOTE:** In these early decades of the 21st century, we are producing more data than we can handle, and the depth, breadth, and quality of the data that is being used are reshaping not just the tools and capabilities of our industries and cities, but the nature of how we learn, socialize, and entertain ourselves. It’s also elevating risks that we may previously have characterized as annoyances to a world today where a cyberattack can result in millions of dollars of losses in hours.

## Data-Driven Decision-Making
- data helps us all make better decisions
- e.g. deciding on a restaurant based on reviews; less complex end

- entering a new market with an existing product/service = deep understanding that can come from rich sets of data
- if data exists and the tools to process and interpret it = good position to make the right decision
- without good data and the skills and tools to analyze it = bad and costly decisions may result
- **IMPORTANT:** The availability of abundant good quality data has been a boon for decision-making.
    - Consider this; if you decide based on bad data, your challenges will be entirely different.
    - *Abundant data* is a product of the *21st century*, but *quality data* is the product of *deliberate actions*.
    - Data governance plays a central role when aspiring for data quality.

## Data is The New Oil
- coined by Clive Humbly in 2006
- data is driving and growing new economies
- data has value but must be processed to be useful
- e.g. oil is refined to make gas, plastics etc. and data must be organized and analyzed to understand patterns, make decisions, identify problems and feed other systems
- without the processing; oil and data are notably messy and unusable in their raw form

- oil powered industrial economies of the 19th and 20th centuries, data is powering the digital economies of the 21st century
- big economic powerhouses are being powered by data i.e. technology firms Facebook & Google
- many are moving data management from a cost centre to a profit centre by making data power their businesses and generate new sources of revenue

- like oil, those who control large repositories of high-value data have disproportionate power

## Data Ownership
- **TIP:** For something to be properly managed, someone needs to be responsible. We create accountability in job descriptions and projects. Without that, how will we know that something will get done?

### Data Ownership
- **data ownership:** the rights a person, team or organization has over one or more data sets
- may span from lightweight oversight and control to rigorous rules that are legally enforceable
    - e.g. data associated with intellectual property --> items such as copyrights and trade secrets; will have high degrees of protection, from accessibility rights to who can use the data for what purpose.

## Data Architecture
- **Enterprise Architecture (EA):** designing technical needs of an organization to support its business strategy
- using standards and established principles, organizations can analyze, design, plan and implement the right technologies, policies and projects to support business goals

- **data architecture:** is a subset of EA
    - is the agreed blueprint for how data supports an organization's functions and technologies
    - in other words, it is how data design and management decisions are made to align with EA and in turn, with the business
- **NOTE:** When high-quality enterprises and data architectures both exist, organizations run more smoothly, and they can transform as conditions (either internally or in the marketplace) dictate. The absence or poor implementation of both can stifle digital transformation efforts, create high levels of complexity, and increase the possibility of failure

- data architecture considers and supports the following:
    1. ensuring data is available to those who need it and are approved to use it
    2. Reducing the complexity of accessing and utilizing data
    3. Creating and enforcing data protections to support organizational policies and obligations.
    4. Adopting and agreeing to data standards
    5. Optimizing the flow and efficient use of data to eliminate bottlenecks and duplication

- data architecture = direct reflection of data governance
- established and functioning data architecture signals the organization values data, manages it as a critical business asset and has controls in place to ensure that it aligns with business needs
- data architecture = cross-organizational responsibility
  
## The Lifecycle of Data
![image](https://github.com/Nolu-M/Python/assets/119700411/bcbaad99-9b8e-46fb-91d0-cadbe6a4ac75)

1. *Creation:* data comes into being; manual or automated and gets created internally or externally through various activities i.e. system inputs and outputs
2. *Storage:* data must be stored after being created; will be contained and managed in a database --> local hard drive, server or cloud service
3. *Usage:* data may need to be processed; cleansing it of errors, transforming it to another format and securing access rights
4. *Archival:* identify data that is not being used currently --> move to a long-term storage system and out of production environment --> can be retrieved & used later
5. *Destruction:* there's a point where destruction makes sense or is required by regulation/policy. data destruction involves making data inaccessible and unreadable; can include the physical destruction of a device i.e. a hard drive

- **NOTE:** The idea that data is in different states at different times is an essential context of data governance. Depending on the stage of its life, data may be treated differently and have unique requirements. For example, the security needs of data being regularly used will differ from data in an archival state.

## Understanding the Impact of Big Data
- Romans used ledgers to keep track of their various activities across their expansive empire
- 20th century: The Cold War was instrumental in the technological leaps that resulted in microprocessors and the classical computing we use today
    - by-product = the space race between the U.S. and the Soviet Union, accelerated innovation in computing and telecommunications

### The Role of The U.S. Census in The Information Revolution
- processing data in some form of computing device has been around since the late 1800s
- the origin of data processing --> the need for a mechanism to better tabulate the results of the U.S. constitutional requirement to conduct a population census every 10 years
- counting all the people and other data points in the 1880 census = took almost 8 years
    - Tabulating Machine Company, founded in 1896 = automated and commercialized the processing of the data
      
- to count census results --> handwritten results are converted to punched holes in cards e.g. if a result for an individual was a “man,” then this was represented by a punched hole
- a rod would attempt to pass through the hole to make an electrical connection with a pad on the other side
- electrical connection made = a counter would progress with an addition of one
- these punch cards would be considered a form of data storage

- Tabulating Machine Company = International Business Machines, IBM
- IBM infiltrated the industry and had the desire to increase automation in the office, military, academia and factories

- these major developments and others culminated in what we know as the *third industrial revolution:* the information age
- data became raw material feeding a new generation of productivity and ideas
- connectivity provided the arteries for information to freely flow across devices, organizations and geographies with few limitations

- result = data creation, storage and use exploded
- data volume and velocity had become so unwieldy that it was creating a data swamp
- data swamp: out-of-control amounts of data; makes it difficult for traditional software applications to manage
- big data: the scale and challenge of all the data

## Defining Big Data
- **NOTE:** Big data is structured and unstructured data that is so massive and complex in scale, that it’s difficult and often impossible to process via traditional data management techniques.

### Defining Big Data
- defined through 5 Vs:
    1. Volume: the sheer scale of data being produced is unprecedented and requires new tools, skills and processes
    2. Variety: a lot of legacy file formats, such as CSV and MP3, and with new innovations, new formats are emerging all the time. This requires different methods of handling, from analysis to security.
    3. Velocity: With so many collection points, digital interfaces, and ubiquitous connectivity, data is being created and moved at increasing speed
    4. Variability: The fact that the creation and flow of data are unpredictable
    5. Veracity: The quality, including accuracy and truthfulness, of large volumes of disparate sets of data, can differ considerably, causing challenges to data management

### Drivers of Big Data
- **NOTE:** Big data was a thing even before Android and Apple smartphones and apps started generating data. This was before we had connected billions of devices, called the Internet of Things (IoTs), which would eventually begin collecting all manner of data. Big data even predates videos of cats published every day on social media platforms.
- 3rd decade of 21st century --> many devices connected, world in digital transformation therefore volume of data being created had experienced a Cambrian explosion
- in 2021, global technology generated 79 zettabytes of data --> 180 zettabytes in 2025

### Consequences of Big Data
- **IMPORTANT:** For starters, up to 80 percent of data is unstructured. That’s a challenge right there. The vast majority of organizations struggle with unstructured data. In addition, a lot of this data is duplicative. Some of it will be bad data, which means it can’t be trusted, has errors, or includes some other substantive challenge
- **NOTE:** data at scale is providing incredible value to all types of organizations. It’s also the source of remarkable innovation, from self-driving cars to optimized supply chains.
- 19th century U.S. retailer John Wanamaker stated: half his advertising budget was wasted but he just didn’t know which half
    - Marketers using the latest technology can better understand the marketplace in granular detail.
    - They can target specific audiences, and even specific individuals, where the chance of a sale is highest.

### What about small data?
- **NOTE:** Think about all the spreadsheets that come by your inbox, the short surveys, or those go-to lists that we’ve all compiled and can’t live without. It’s not nearly as glamorous as big data, but in some cases, it may be argued as valuable
- big data = meaningful when broken into smaller, more manageable chunks --> an increasingly popular definition of small data
- smaller, logically arranged data can be the way to make sense of big data; can be the only way sometimes

### Enter the Realm of Smart Data
- small data = new term that defines big data
- For example, marketing teams can target potential customers with precision. Analytics applications can use high-quality real-time data generated in a manufacturing setting.
- smart data uses new processes and tools to make the data more useful
    - e.g. increasing use of artificial intelligence (AI) is now being applied to find patterns in unstructured big data and extract the data that is most relevant for a given application
    - AI reduces time, lowers errors and enables the creation of data subsets that may not have been previously possible
    - smart data solutions are often applied at the point of collection rather than a post-processing solution

# Chapter 3: Driving Value through Data
## Identifying the Roles of Data
- critical to ensure that data is high quality, secure, compliant and accessible to the right people at the right time
- **NOTE:** Data matters to everyone

### Operations
- each business has different needs, and operational functions reflect these specific requirements i.e. payroll, order management and marketing
- performance of operations is quantified by data e.g. in HR function, they'll want to know how many openings there are, how long openings are taking to fill and who is accepting offers
  
- in HR --> data is created by the activities of the function e.g. candidates enter data when they apply for a position, data is entered when evaluating an applicant and all along the way the supporting systems log a variety of automated data i.e. time, data and how long an application took to complete online
- in this example and others; data is created in abundance as a result of and in support of functions

- operations --> use data to make decisions, enable systems to run and deliver data to internal and external entities e.g. regional sales team will deliver their monthly results to headquarters to be presented to vice presidents or the C-suite

- many data operations are automated e.g. a warehouse inventory system may automatically generate a replenishment order when stock drops to a certain level
- e.g. all the notifications that systems generate based on triggers i.e. email notification

### Strategy
- every organization has a strategy; this is about creating a plan that supports objectives and goals
- about understanding the challenges to delivering on the organization's purpose and then agreeing on the proposed solutions to those challenges
- strategy can be adopted at the department and division levels, but the intent is the same: understand the journey ahead and make a plan

- strategy --> implementation; requires the support of operations to realize its goals
- strategy and operations = two sides of the same coin

- creating a strategy = begins with analysis of the environment --> some conclusions on what has been gathered --> a plan is developed, driven by some form of guiding principles
    - principles may be derived from the nature of the work, the values of the founders etc.

- **TIP:** Deeply tied to all these steps is the availability of good quality data that can be processed and analyzed and then turned into actionable insights.
- there needs to be room for other perspectives i.e. strength of belief that people with experience bring to the discussion and right mix of data and non-data sources must be considered, too much of one or the other may not deliver the expected results

- **NOTE:** consider ongoing process, when it comes to the best practices for strategy development. No need to update the strategy every month, as they are intended to last for several years but revist the strategy every 6 months and tweak it as necessary. Revisions should be guided by new data (new knowledge or new insights)

### Decision-Making 
- highest form of value derived from data is the ability to make better-informed decisions
- **NOTE:** Without even creating a single unit of raw data, there’s a universe of existing data and information at our fingertips. In addition, increasing numbers of easy-to-use analysis capabilities and tools are democratizing access to insight

- within organizations, access to abundant data and information has resulted in quicker, timeous and better-quality business decisions e.g. executives can understand their strengths, weaknesses, opportunities and threats closer to real time
- **IMPORTANT:** While there’s little surprise that data-driven decision-making is a fundamental business competency, it all hinges on decision-makers getting access to quality data at the right time. Abundant and out-of-date data are not synonymous with data value. Bad data may be worse than no data. Bad data processed into information and then used as the basis for decisions will result in failure. The outcome of decisions based on bad data could range from a minor mistake to job termination right up to the closing of the business.

### Measuring
- organizations = continuous state of measurement
- what gets measured gets managed but some things are hard to measure and not everything gets measured
- **TIP:** Data measurements can be quantitative or qualitative. Quantitative data is most often described in numerical terms, whereas qualitative data is descriptive and expressed in terms of language.

- **NOTE:** The type of information desired directly correlates to the measurement approach. This is going to inform your choices of at least what, when, where, and how data is captured. A general rule is only to capture and measure what matters.
- William Bruce Cameron = “Not everything that can be counted counts, and not everything that counts can be counted.”
    - teaches us that being overly passionate to believe that you can always find relevance in any type of data, be the mere fact that you can identify data elements.

### Monitoring
- ongoing process of collecting and evaluating the performace of e.g. a project, process, system etc
- collected results compared against some existing values or desired targets e.g. a machine on a factory floor may be expected to produce 100 widgets per hour
    - monitoring in order to inform whether this expectation is being met
 - monitoring also helps to ensure the continuity, stability and reliability of that being supervised

 - **NOTE:** Involved in monitoring is the data produced by the thing being evaluated. It’s also the data that is produced as a product of monitoring. For example, the deviation from the expected result.
 - the data produced through monitoring feedss reports, real-time systems and software-based dashboards

 - monitoring: another process that converts data into insight and as such, exists as the mechanism to guide decisions
 - role of data in measurement and monitoring = go hand-in-hand (measure something you want to monitor)
 - data is a type of connective tissue that binds business functions
 - this required oversight and controls, as stakeholders often have different responsibilities and permissions e.g. people responsible for providing measurement data on processes may belong to a different team from those who have to monitor and report on the measurement data
 - thos who take action may also belong to a different department in the organization

 - Data monitoring: also the process of evaluating the quality of data and determining if it is fit for purpose
    - achieving this requires processes, technologies and benchmarks
    - data monitoring begins with establishing data quality metrics and then measuring results over time on a continuous basis
    - monitoring metrics may include areas such as completeness and accuracy
  
### Insight Management
- data forms the building blocks of many business functions
- business insight: information that can make a difference
- **IMPORTANT:** insight management means ensuring that data and information are capable of delivering insight

- begins with gathering and analyzing data from different sources
- to determine what data to process = those responsible for insight management must understand the organization's information needs, be knowledgeable about what data has value and must know how information flows across the organization and who it must reach

- with data gathered and processed, analytics will be applied - this is the enterpretation of data and it imlications

- insight management: involves designing and creating the most effective manner to communicate any findings --> different mechanisms for different audiences
- **TIP:** For an insight to be most valuable, it must be the right information, at the right time, in the right format, for the right people. But this in general is no simple task.
- knowledge management: the organizational support structures and tools to enable insight to be available to employees for whatever reason they need it

### Reporting
-  Creating, delivering, receiving, and acting on reports are fundamental functions of any organization
-  content of a report, which can be summarized or detailed, contains data and information in a structured manner
    - e.g. an expenditure report would provide basic overview of the purpose of the report and then support it with relevant information
    - could include a list of all expenditures for a department over a certain period or it could be a total amount --> depends on audience and purpose
- **NOTE:** Reports are typically online or physical presentations of data and information on some aspect of an organization. Sometimes a report is given verbally in person or via a live or recorded video. It is developed for a particular audience with a specific purpose

- purpose of reporting is about improved decision-making
- right information, in the right format, at the right time, business leaders are empowered to make better decisions, solve problems, and communicate plans and policies.

### Other Roles for Data
1. **Artificial Intelligence (AI):**
    1. data considered fuel of AI and it required a high volume of good data
    2. large quantities of data = outcomes of AI imporve and from this data AI learns patterns, identifies relationships, and determines probabilities, and is used to improve the quality and use of data in organizations
2. **Problem-solving:**
    1. data plays a role in how a problem is defined, determining what solutions are available, evaluating which solution to use and measuring the success or failure of the solution that is chosen and applied
3. **Data reuse:**
    1. data that has been collected, used and stored can be retrieved and used by a different team at another time - they need permissiong, including access and legal rights
    2. e.g. sales team collects name and address to fulfill and order, same data later used by marketing team to create awareness about other products and services
    3. data reuse = positive, it reduces data collection duplication and increases value of data but it must be managed with care so that it doesn't break data rules
    4. **NOTE:** master data = high-value shared data sets and in governance are subject to master data management.

## Improving Outcomes with Data
- how data can be leveraged to acquire its maximum value begins with recognizing that data is an organization asset
- **NOTE:** Perhaps the function that is most associated with data is the process of exploring it and looking for insights. Called data analytics, this is a comprehensive organizational function that requires skilled staff and tools. With the emergence of big data, data analytics has become more complex and requires deeper skills, but it’s also made data more valuable and important to the business

## Approaching Data as an Asset
- asset: something owned by a person, an organization or government with the exception that it can bring some economic benefit, including generation of income, reduction of expenses or an increase in net worth
- **NOTE:** An asset can be tangible or intangible. Tangible assets are physical things such as inventory, machines, and property. That’s stuff you can see and touch. An intangible asset is the opposite; it’s a non-physical thing like software, copyrights, a brand, and goodwill. Data is an intangible asset.

- Listing the value of assets presents the true state of any organization and reflects its financial health and capturing and valuing assets is required for determining tax obligations and for acquiring loans
- economic value of data examples:
    - Improves operations.
    - Increases existing revenue.
    - Produces new forms of revenue.
    - Builds relationships with customers and other stakeholders.
    - Improves the quality of products and services.
    - Contributes to competitive advantage.
    - Enables innovation.
    - Reduces risk.
- you need to know what you have and where it is, as well as have an expression of its value
- if data has no value, consider whether you should be managing it

- data as an asses --> is it good or bad, pay attention to the data's accuracy, completeness, validity etc.
- need to understand how the data is being managed and who has responsibility for it

- **Bottom line:** Data is an asset and for its value to be leveraged, it must be governed. This may be one of the most important motivations for good data governance.

## Data Analytics
- data analytics: the process of examining data in order to produce answers or find conclusions
    ![image](https://github.com/Nolu-M/Python/assets/119700411/a8818235-22f2-49a9-bc28-bcc2a009c563)

- four primary types:
    - Descriptive: existing data sets of historical data accessed, analyzed for stakeholders about performance of a key performance indicator (KPI) = insight on past performance
    - Diagnostic: analysis tries to glean from data the answer to why something happened = takes descriptive analysis and looks at the cause
    - Predictive: techniques are used to determine what may occur in the future. it applies tools and techniques to historical data and trends to predict the likelihood to certain outcomes
    - Prescriptive: focuses on what action should be taken --> in combination with predictive analytics, prescriptive techniques provide estimates of the probabilities of a variety of future outcomes

    ![image](https://github.com/Nolu-M/Python/assets/119700411/13a1cfc7-0d85-418a-8344-87ae283e0e2a)

## Data Management
- **data management:** is the implementation of data governance
- all organizations implement data management; what matters is the degree of sophistication that is applied to managing the value and quality of data sets --> if it's on the low side, data may be a disadvantage than an advantage
- poor data management = data silos across an organization, security and compliance issues, errors in data sets and overall low confidence in the quality of data

### Who would choose to make decisions based on bad data?
- well-executed data management can translate to reduced data security breaches, and lower compliance, regulatory and privacy issues
- **data management processes** involve the collection, storage, organization, maintenance and analytics of an organization's data
    - includes the architecture of technology systems such as that data can flow across the enterprise and be accessed whenever and by whom it is approved for use
    - responsibilities = areas such as data standardization, encryption and archiving

- **NOTE:** In summary, good data management provides the opportunity for significantly enhanced organizational performance.

### Governing Data
- governing data: means that some level of control exists to support a related policy e.g. organization may decide to reduce risk, needs to be a policy that requires data to be backed up every day
    - the control would be the documentation of the process and enforcement of that policy
    - if in the review of the policy adherence, data wasn't getting backed up = governance was not working for some reason

- success of governing data can be reduced to 3 essential factors:
    - **People:** handling and benefiting from data is still a highly people-centric exercise, even in a machine-centric context --> people are the responsible for defining, designing and maintaining data use and in governing data, people are responsible for quality and they oversee and manage all related processes and responsibilities
    - **Policies:** data policy = a set of adopted rules by an organization that apply to the handling of data in specific conditions and for particular desired outcomes and these policies apply in areas such as quality, privacy, retention and security. Number of policies = reflection of size of organization, the industry and the degree to which data is considered a high-priority asset
    - **Metrics:** what gets measured gets managed but you need to consider how the data is measured. Metrics must be in support of both technical and business needs.
 
# Chapter 4: Transforming through Data
## Examining the Broader Value of Data
- **data democratization:** the ability of team members to access data that they need for their work without having to rely on specialists
- **IMPORTANT:** As organizations grow and more systems are employed, eventually no single person knows what data is available and where it is in the enterprise. Without this knowledge, the ability to properly govern your data and leverage its value is greatly hampered. Without deliberate actions, data democratization becomes elusive.

- **data silo:** a data repository controlled by an entity in an organization but not frequently shared or known by other parts of the business
    - hinder business efficiencies because they reduce collaboration and increase data inconsistencies
    - they are a source of risk, including security and regulatory issues
 
- data governance helps eliminate unnecessary data siloes and make data discoverable and available whenever and wherever it adds value
- data catalogs are an essential way that data governance can help solve these limitations

- data sprawl: a term for the myriad of data types and sources that most businesses grapple with today
- can find information about an organization by Googling rather than using your own internal search systems but if the data is protected behind the organization's firewall, a public search engine won't help
- knowing what data is available is essential for the following reasons:
    - Better informed decision-making.
    - Ensuring compliance and regulatory requirements.
    - Lower costs by avoiding duplicate system and data efforts.
    - Improved data analytics and reporting.
    - Higher performing systems.
    - More efficient operations.
    - Reducing data inconsistencies across the enterprise.

## Data Catalogs
- can assist team members find data by creating an enterprise search engine which can have some limitations such as the discoverability of confidential data that is deliberately siloed
    - common purpose is to provide you with the location of the data
- data discoverability = creation of an enterprise data catalog
    - data catalog: lists the availability of data sets and includes a wide range of valuable details about that data

- essential benefits of data catalogs:
    - finding data: helps users identify and locate data that may be useful
    - Understanding data: answers a wide variety of data questions i.e. its purpose and who uses it
    - making data more useful: creates visibility, describes value and provides access to information
    ![image](https://github.com/Nolu-M/Python/assets/119700411/49cf038a-358b-4554-8823-5b9c0d1fcf1a)

- metadata: contains data about the data (why datalogs are valuable)
- three types of metadata:
    - Technical metadata: data about the design of a data set i.e. its tables, columns, file names etc
    - Business metadata: organizational data i.e. business description, how it is used, its relevancy, an assessment of data quality and users and their interactions
    - Operational metadata: data such as when the data was last accessed, who accessed it, and when it was last backed up
- examples of metadata:
    ```
    - Associated systems.
    - File names.
    - File locations.
    - Data owners.
    - Data descriptions.
    - Dates created.
    - Dates last modified.
    - List of database tables and views.
    - Data stewards.
    - Size of data sets.
    - Quality score.
    - Comments.
    ```
- with a data catalog, an organization can:
    ```
    - Know what data it has (and by extension, know what data is missing).
    - Reduce data duplication.
    - Increase operational efficiencies and innovation.
    - Understand data quality.
    - Manage compliance.
    - Enjoy cost savings from improved operations.
    ```
- **NOTE:** a data catalog is often the basis for delivering successful data governance and data management.

## Case Study: Unlocking Data Silos With a Data Catalog
### background
- European power company embraced data governance in support of its mission of decarbonizing the production of electricity
- organizaion generates and distributes energy across multiple countries
- data is essential for daily operations e.g. evaluating equipment performance
- business must adhere to the regulatory requirements in all countries where they operate - also comply with Europe's General Data Protection Regulations (GDPR): governs the use of personal data

#### Problem Statement
- how to power its mission by enabling business units and partners to collaborate using the business and technical data locked away in siloed systems, while also ensuring a high degree of data compliance

#### The solution
- solution was in the implementation of data catalog with robust data governanc functionality
- data catalog facilitated collaboration and innovation by enabling vastly improved search and discovery of data across the organization
- compliance requirments were improved by the catalog interface guiding compliant behaviour using workflows --> the data taught people how to use data compliantly and ensured they followed the relevant policies based on the data at hand

#### Results and Lessons Learned
- lessons gleaned from their data governance journey included:
    - make data governance part of hw all datt users work with data, not an external task force or project
    - start small and grow steadily

- curate metadata facilitates data search and discovery across the organization
- business glossary helps define standard terminology to ensure that all users have a common understanding of critical business terms

- by using a data catalog to put the right data into the right hands ata the right time (with the right compliance guidance), the organization build trust in their data
- this in turn, generated efficiency and profitability, along with reduced risk

### From Data to Insights
- whether an organization uses insight to support decisions or drive actions is a choice
- when insights are used primarily to drive action, the value of the underlying data is truly realized
- actionable data is the most valuable data to an organization

- acquiring and applying insight from data means defining the following:
    1. Context: Understanding the environment and objectives of the outcome
    2. Need: determining how insight will help to accomplish the objective
    3. Vision: having ideas about how insight will elp and what that might look like in practice
    4. Outcome: specifying how insights will be adopted and success will be measured

- these dimensions can be used to answer questions such as:
    ```
    - What data is required?
    - Does the data exist?
    - Is it current?
    - Is it easily available?
    - What format is the data in?
    - What kind of data analysis is required?
    - How will the data be presented?
    ```
- **IMPORTANT:** Those tasked with delivering insights often cite data quality, data volume, work effort, and integrating data from various sources as the top reasons that make it difficult and create a deterrent to adoption.

## Data Analytics
- analytics unlocks the power embedded in good-quality data

- data analysis: concerned with identifying a data set, examining it and reporting on any findings
    - subset of data analytics and focuses on what data from the past tells us
- data analytics: a complete science that involves collecting, cleaning, organizing, storing, administering and analyzing data --> informs you about the past and helps you project into the future

- the source of data for analytics is one or a combination of the following:
    - **First-party data:** Data that an organization collects
    - **Second-party data:** Data that is obtained from another organization
    - **Third-party data:** Aggregated data obtained from a provider

- typically uses of contemporary data analytics and techniques include:
    ```
    - Vastly improved decision-making
    - Focused marketing campaigns
    - Understanding the competitive landscape
    - Designing more innovative products
    - Better customer service
    - Improved operations
    - Insights on customer behavior
    ```

## Data Monetization
- *an asset:* something owned that has the expectation of delivering value
- data falls into the same category as assets such as copyrights and software

- data doesn't show up on the balance sheet --> those assets that are required to be included in the accounts are carefully assessed so that an accurate picture can be captured of an organization's financials

- *data valuation:* without a process to place a price on a data set; value of a given data set may be highly subjective and may differ considerably between perspectives of team members
- Without this knowledge, it’s much harder to take advantage of the opportunities that some data sets may provide, such as business growth and operational excellence.

- *data monetization:* when data provides an economic benefit to an organization
- Data valuation, while generally recommended in larger enterprises, is a requirement for advanced data monetization such as selling or licensing data

- ways to determine data valuation:
    - Cost value method: value calculated by determining production cost, storage and replacement of data; doesn't necessary account for economic value that the data can produce
    - Market value approach: value calculated by researching how comparable data is being priced in the open market; great if market-based comparable data exists; doesn;t work for vast number of data sets that are not traded
    - Economic value approach: value calculated by measuring impact a data set has on the business's bottom line; difficult method
    - With-and-without method: value calculated by quantifying impact on cash flow if a data set needs to be replaced; with or without data scenarios are explored and the difference between cash flow is used to determine data value; challenging to pinpoint specific impact on data set

- *data asset management:* a business must know what data sets it has and understand their value; it must have a plan for utilization and a mechanism to measure return on investment

## Data-Driven Decision Making
- **NOTE:** data-driven decision-making (DDDM) is the process of using data to drive business decisions
- DDDM can be effective anc contribute to high performance when an organization has data culture and specific skills and tools

- organizations that excel in DDDM do so through deliberate actions and investments;
- executives who demonstrate DDDM are role models for the entire enterprise; enabling the right people use the right data at the right time required data security and data-use policies = core cunctions of data governance

- six step process to data-driven decision-making
    1. **Define the objectives:** understanding the objectives relative to the effort anf their alignment with organizational goals; helps scope the work and define metrics = useful to work backwards
    2. **Identify the data:** in addition to using a data catalogue, enterprise search etc requires engaging with impacted stakeholders --> getting input from a diverse group of people & teams helps; consult data stewards, owners etc with data governance responsibilities
    3. **Prepare the data:** if data is easily accessible and high-quality = good shape; otherwise deep data science skills are needed to prepare the data for use in data analytics platform
    4. **Analyze the data:** complex analysis = tools like ETL architecture; data extracted from one system and made ready and available for use in another; visualizations such as graphs, charts used
    5. **Determine the findings:** display data in a variety of ways and ask questions about it
    6. **Take action:** make decisions which would result in actions

## Developing a Data Strategy for Improved Results
reasons that organizations don’t take a proactive approach to managing data:
    - “If it ain’t broke”, why fix it?
    - It’s too expensive and time-consuming to focus on data.
    - It’s far too complicated.
    - Data management and governance — what is that?
- **NOTE:** The purpose of any type of strategy is to agree on a set of guiding principles that inform decision-making in support of a desired outcome. In simple terms, it’s the roadmap on how to reach your goals.

- people must agree on how decisions will be made and how resources will be allocated
- strategy = have clarity and make it easy for all leaders and team members to know what they need to do, what to avoid and how actions should be prioritized

- some organizations do not have a current and well-communicated strategy; hard to create a strategy and often a bureaucratic effort when some leaders believe all the energy should be on execution every day

- strategies consider the vision, mission as well as guiding principles and can apply to processes and assets too
- needed in order to elevate data to become a strategic resources; strategy should reflect the size and complexity of your businesses and the industry in which you operate
- good strategy = guide decision-making & resource allocation around data in support of organization; it will demonstrate and communicate data as a priority and ensure success of the organization is optimized 

## Creating a Data Strategy
before jumping in after creating a data strategy, consider the following characteristics as a guide:
- **Data maturity:** the degree to which the organization already uses and optimized data and has experience & skills, as well as the quality of the existing data

- **Industry and size:** two frameworks = *defense* - deals with fundamental areas such as data security and quality and *offense* - using data for insight management and market-facing initiatives; every organization does both but most emphasize on over the other depending on industry & size

- data strategy should account for these 5 areas of data requirments:
    - **Identify:** data should be clearly defined and described i.e. file name, format and metadata
    - **Store: Provision:** design & develop capabilities for supporting the place and process for hosting data and how it will be shared, accessed and processed
    - **Provision: determine processes to share & reuse data and define guidelines for access
    - **Process:** raw dat transformed, including processes for data cleansing, standardization and integration with other data sets
    - **Govern:** institute processes to manage and communicate data policies for data use with the organization

- four data strategy components:
    1. **Alignment with the business:** data strategy = subset of overall business strategy, therefore, it must support and advance larger goals of organization; map out goals clearly/how they support business strategy
    2. **Identifying roles and responsibilities:** requires people to take specific actions
    3. **Data architecture:** processes, systems and applications that support working with data; include defining data storage needs and analysis tools --> also includes data catalogs, a data warehouse & the tools for data pipelines, movement of data and related ETL functions; data strategy should support data architecture scalability etc.
    4. **Data management:** broad umbrella of activities that manage full lifecycle of data in an organization; recognizes that data is a strategic asset and must have the attendant processes, procedures, policies, skills and tools to ensure it is treated in such as manner --> includes management of data security & privacy, quality, metadata, integration, master data management and analytics

- **NOTE:** Data governance establishes the rules for data use, and data management ensures that, in the act of realizing data value in the organization, these rules are followed. For example, a data governance policy may state that data with a certain confidentiality classification may only be accessible by a specific role level in the organization. Data management will be the processes, tools, and staff that ensure that this governance rule is followed.

    ![image](https://github.com/Nolu-M/Python/assets/119700411/284a9e9a-d112-4bce-98f1-4c412afee92e)

## Managing and Monitoring Your Data Strategy
- have a buy-in, a roadmap and execution underway, but accompanying data governance and data management functions must also be in place
- **TIP:** All strategies must be open to periodic modification. It’s not realistic to expect a strategy to be fixed for its duration in a fast-moving business world. Your evolving customer expectations, organizational needs, the economy, and more all play a role in forcing a strategy to adapt.

- a strategy is created with information you have + assumptions; as strategy plays out, errors and gaps can be found
- it will become apparent whether objectives, goals and metrics were correctly calibrated = problematic if any are off the mark --> triggers you to go back and review plan & make adjustments

- **NOTE:** The worst thing you can do is design a strategy, implement it, and place the plan on a shelf only to revisit it three to five years later. Unfortunately, this happens more often than not. It is something you experience often in your organization.

- monitoring your data strategy = having right metrics, getting feedback regularly from participants and auditing related outcomes
- all strategies, including data strategy = regulalarly reviewd & modified as necessary.

</details>


<details>
<summary>Power BI</summary>
    
# 1. Get started with Power BI - 3 modules
## Module 1 - Describe the capabilities of Microsoft Power BI
### Describe using Power BI to build data-driven analytics
- Microsoft Power BI (Business Intelligence): a collection of software services, apps and connectors that work together to turn unrelated sources of data into coherent, visually immersive and interactive insights
- lets you easiily connect to your data sources, clean and model your data without affecting underlying source, visualize (or discover) what's important and share that with anyone/everyone
- consists of a **Microsoft Windows desktop application** ---> **Power BI Desktop**, an **online SaaS (Software as a Service) service** ---> **the Power BI service** and **mobile Power BI apps** that are available on phones and tablets
- these three elements are designed to let people create, share and consume business in a way that serves them or their role most effectively.

### Explore the different Power BI elements
- to create Power BI Solutions, several building blocks which are elements that help with the data being presented and its appearance to those users who are consuming it.
    - elements = datasets, reports and dashboards, organized into workspaces and created on capacities.

#### Capacities
- core Power BI concept representing a set of resources used to host and deliver your Power BI content
- are shared (shared with other Microsoft customers) or dedicated (fully committed to single customer, require subscription)
- by default, *workspaces are created on a shared capacity*.

#### Workspaces
- containers for dashboards, reports, datasets and dataflows in Power BI
- two types:
    1. **My workspace:** personal workspace for any Power BI customer to work with their own content, only have access to your My workspace, can share dashboards and reports for collaboration use workspace.
    2. **Workspaces:** used to collaborate and share content with colleagues, can add colleagues to your workspaces and collaborate on dashboards, reports and datasets, with one exception = all workspace members need Power BI pro licenses. Also the place to create, publish and manage apps for organization - staging areas & containers for content that makes up a Power BI app.
        - app = a collection of dashboards and reports built to deliver key metrics to the Power BI consumers in organization.
        - apps are interactive, consumers can't edit them and app consumers as well as colleagues who have access to apps don't need Pro licenses.

#### Semantic models
- a collection of data that you import or connect to, also can source data from dataflows
- associated with workspaces, single semantic model can be part of multiple workspaces
- when workspaces is opened, associated semantic models are listed under **semantic models tab**, each representing a collection of data e.g. semantic model can contain data from an Excel workbook on OneDrive, an on-premises SSAS tabular semantic model and/or Salesforce semantic model
- semantic models added by one workspace member are available to other workspace members with an admin member, or contributor role.

#### Shared semantic models
- important to establish standardized semantic models that can be the 'one sources of truth' discovering and reusing those standardized semantic models is key
- expert data modelers create and share optimized semantic models, report creators can start with those semantic models to build accurate reports
- organization = consistent data for decisions & a healthy data culture
- to consume shared semantic models, choose **Power BI semantic models** when creating Power BI report

#### Reports
- one or more pages of visualizations i.e. line charts, maps, and other elements
- can be created from scratch, import them from shared dashboards or have Power BI generate them when connecting datasets
- e.g. when you connect to an Excel workbook that contains Power View sheets, Power BI creates a report based on those sheets, and when you connect SaaS application, Power BI imports a prebuilt report
- two models to view and interact with reports:
    - Reading view: report opened by user
    - Editing view: individuals that have edit permissions, used to modify different elements on the report an how they're presented
- workspace opened =  associated reports listed under **Reports** tab, each report represents one or more pages of visualizations based on only one og the underlying datasets

- when you open an app = presented with a dashboard, to access underlying report, select dashboard tile that was pinned from a report
- by default, report opens in Reading view, select **Edit report** to open in editing view

#### Dashboards
- single canvas that contains zero or more tiles and widgets
- each tile pinned from a report or from Q&A displays a single visualization created from a dataset and pinned to the dashboard
- why create dashboards:
    - to see all information for decision making
    - to monitor important information
    - ensure colleagues are on the same page, viewing and using same information
    - monitor health of business, product, business unit etc.
    - create personalized view of larger dashboard and show all metrics that matter
- when dashboard open, associated dashboards listed under **Dashboards tab**, select to open

#### Template Apps
- enable Power BI partners to build Power BI apps with little or no coding and deploy them to any Power BI customer
- Power BI partner can create a set of out-of-the-box content for customers and publish it yourself

- can build tamplate apps that allow customers to connect within their own accounts
- domain experts can unlock data in a way that is easy for their business users to consume

### Describe cleaning and transforming data in Power BI Desktop
- cleaning and transforming data is how you prepare data for use
- use the Power BI Desktop application for transforming and cleaning data
- Power BI Desktop has 3 views:
    - **Report view:** can create queries to build compelling visualizations you can share
    - **Data view:** see data in your report in data model format, can add measures, create new columns and manage relationships
    - **Model view:** get a graphical representation of relationships established in data model and manage or modify them as needed
- Power BI Desktop includes the **Power Query Editor tool:** can help you shape & transform data for models and visualizations
- select **Edit** from **navigator** window to launch Power Query Editor, can also be launched from Power BI Desktop using **Transform Data** button on Home ribbon

#### Transforming data
- process of putting data into a format what is useable
- examples of available transformations include removing a column from table, dupicating column under a new name or replacing values

#### Clean data
- Power Bi visualization and modeling tools work best with columnar data
- a table layout that looks good to the eye might not be optimal for automated queries e.g spreadsheet that has headers that span multiple columns
  ![image](https://github.com/Nolu-M/Python/assets/119700411/68c8d24c-4575-44f9-ac7e-f9b7d4e2f9cb)
- when cleaning data, might combine those rows into a single item to better format the data to fit your needs or may have a series of numeric data that would need to be aggregated to display better

### Describe using AI Insights to spot trends and anomalies
- anomalies and trends in your data can be identified as you intercat with the data and consume elements such as reports, dashboards and visualizations
- it notifies you of any interesting insights and provides explanations for them
- it works out-of-th-box on any report, so you can automatically start getting insights from your reports without any setup

- Power BI has multiple insights features that use artificial intelligence (AI):
    - **Insights for reports:** Analyzes data and finds anomalies and trends in your data as you interact with reports
    - **Insights for individual visuals:** Analyzes and explains the fluctuations of data points in visuals.
    - **Insights for dashboard tiles:** Looks at the data being used to render that tile and presents them in interactive visuals.
    - **Quick Insights for datasets:** Automatically generate data insights on a dataset in the Power BI service.
    - **AI Insights for data models in Power Query:** Provide access to pretrained machine learning models from Azure Cognitive Services.

##### Notifications
- important part of the Insights capabilities in Power BI
- Power BI automatically runs insights analysis, when it identifies insights = presented with a notficiation (can choose to see or ignore insights)
- great way to proactively interact with suggested insights to ensure you are not missing anything important i.e. if sales in specific region have increased
- top insights = noteworthy, based on factors like recency and significance of the trend or anomaly

#### Get insights on reports and visuals
- notification capabilities alert and notify you of insights as you're on reports
- as you're working on Power BI reports and visuals, can select **Get insights** to open the Insights pane
- pane only shows insights about the current report page, and it updates when you select a different image on the report
    - when working on individual visualizations, select **More options (...)** in upper-right corner of a visual, then **Get insights** to see insights about just that visual

#### Insights
insights pane currently shows 3 types of insights:
- Anomalies: something out of the ordinary from what is expected e.g. smart thermostat reading 100F instead of 72F, which would be considered an anomaly
- Trends: a pattern found in time-series datasets e.g. company's sales are steadily increasing through the month of April
- Key Performance Indicator (KPI) analysis: helps evaluate current value against a defined target e.g. company sets sales goal at 1.2 million, currently they are at 1 million

#### Anomalies
- an abnormality in time-series data, such as unexpected spikes and dips in the data
- algorithm = a boundary around what is considered a normal or expected value, any value found outside this boundary is marked as an anomaly
- three types of anomaly insights
    1. Significant anomaly: the anomaly has a high score, anomaly score = how far the point is from expected range
    2. Recent anomaly: the most recent anomaly in the measure
    3. Anomaly summary: insight type summarizes multiple anomalies in the measure
- when anomly in data is flagged, Power BI runs an analysis across different dimentions in data model to look for spikes/dips in the measure that correlates to anomaly, they're shown as possible explanations ranked by strength
  
    ![image](https://github.com/Nolu-M/Python/assets/119700411/5094fa4b-473f-41f1-9c2d-00dbe573931d)
  
#### Trends
- occurs when theres a prolonged increase or decrease in time-series data
- Power BI algorithm follows a series of steps to find meaningful trends by
    - first performs data smoothening, interpolation and time-series sampling.
    - trends are then identifies for statistical significance based on slop and length of a change in value
    - algorithm removes noise like seasonality and outliers e.g. if sales jump in December, algorithm doesn't mark that as noteworthy trend because it's common for sales to jump during holidays
- four main trends flagged:
    - **Long trend:** significant and the longest trend within a single series or across multiple series in a visual
    - **Steep trend:** trend is signifcant and steepest trend with a single series or across multiple series in a visual
    - **Recent trend:** trend is significant and most recent within single or across multiple series in a visual
    - **Trend reversal:** recent trend ina single series or across multiple series in a visual where the reversal is significant, compared to the previous trend segment

- when trend is flagged, Power BI looks for and identifies categories that most influence the increase/decrease in the identified trend
- possible explanations are ranked based on the relative contributions from different categories to the increase/decrease trend
  
    ![image](https://github.com/Nolu-M/Python/assets/119700411/34401e99-c0d3-496e-9aab-80e099c2032f)

#### KPI analysis
- KPI analysis with a target looks at the variance of the current value to its target, significant = variance if high or low compared to other segments
- KPI analysis without a target looks at the value itself and flags ones that are high or low compared to other segments

- KPI analysis explanations --> Power BI looks for and identifies categories that have higher or lower than anticipated values
- for KPI analysis **with** target --> possible explanations, are ranked based on **Z-scores of the difference of the value from the target**
- KPI analysis **without** a target --> possible explanations are ranked based on **Z-scores of the value itself**

### Build a basic dashboard
- with Power BI you can easily create and share a dashboard with a manager by connecting to a data source i.e. Excel spreadsheet
    - **prepare data:** data is in a format that Power BI can easily consume
    - **build a report:** report contains visuals to be included in dashboard, buile either with Power BI Desktop or Power BI service
    - **pin the report visuals to a dashboard:** dashboards = primary element that users use to view data, can include data from multiple reports as needed
    - **share a link to the dashboard:** any users with the link and necessary permissions are able to view and interact with the data

#### Prepare the data
- prepare data for consumption = data cleansing and transforming using Power Query, if connecting to Excel sheet --> make sure datd is in a flat table and each column contains right data type, total operations are handled in Power BI as we create the visuals

#### Upload your data to the Power BI service
- Power BI service = create reports that connect to your data sources, includes Excel files
- can attach to a dataset, and Power BI creates a blank dashboard where you're able to place visuals later

#### Build your report
- once connected to data, create a new report or edit an existing report --> edit report using editing view, on the right = **Visualizations, Filters and Fields** panes
- Excel workbook table = **Fields** pane

#### Pin to a dashboard
- dashboards are easy to build because you are determining which visuals from your created reports you want to include
- easy to have detailed dashboards that include data from multiple data sources, even if those data sources might be unrelated

#### Share a link to your dashboard
- initially dashboards that you create one are only visible to the person that created them, however, by sharing the link to your dashboard and report with others who have a Power BI account, they too can interact with it, but can't save changes.
- if you allow it, they can reshare with others or build a new report based on the underlying dataset

### Consider the business value of Power BI
- Miami Heat basketball team used Power BI to transform their customer interactions and business operations - were able to boost season ticket sales by 30% and save appr. $1 million on operations
- they wanted to understand the family of customers that enter their arena or interact with them online and the challenge was to understand a single customer when there are so many
- by analyzing their data, the Miami Heat operations team increased their revenue but also improved the allocation of resources by predicting customer behaviour

## Module 2 - Explore what Power BI can do for you 
### What can I do with the Power BI service as a consumer?
- Power BI makes the job easier by converting all that data into charts and graphs to help you visualize your data in meaningful ways
- data updates and refreshes automatically, so you can work with your colleagues from the same dashboards and reports
- content is not static = explore data further by looking for trends, insights and other business intelligence
- intuitive features of Power BI allow you to slice content and ask questions using own words

#### How to know if you're a Power BI consumer
- the way you interact with Power BI depends on job role --> consumer = receives dashboards, reports and apps from designers who create them, also work in online version of Power BI = Power BI service to review & interact with data

#### Safely interact with content
- can explore and interact with content, filter, slice, subscribe and export content without affecting underlying dataset or original dashboards, reports or apps
- changes can be saved but they only affect your view of the content and you revert to the original default view by **selecting reset button**

#### Display details on a visual
- visuals are made up of datapoints, hovering over datapoint = view details
    ![](https://learn.microsoft.com/en-us/training/modules/explore-power-bi-service/media/1-1/power-bi-hover.gif)
  
#### Show data that is used to create a visual
- **show data feature** = to view data that Power BI is using to build a visual and selected visual expands to fill the canvas, and the data displays under or alongsied the visual

#### Export data
- can export data and view it in Microsoft Excel --> when exporting to Excel you are creating a separate document, a spreadsheet that isn't part of Power BI
- changes made to Excel do not impact the data in Power BI
- can export entire reports to PowerPoint or PDF
#### Cross highlight and cross filter report content
- highlight or select a value in one visual and instantly view its impact on the other visuals
    ![](https://learn.microsoft.com/en-us/training/modules/explore-power-bi-service/media/1-1/power-bi-cross-filter.gif)

#### Collaborate with colleagues
- can add personal comment or start a conversation with colleagues about a dashboard etc.

#### Let Power BI work for you
- Power BI sends information to you by email, on a schedule that you set

##### Subscribe to reports and dashboards
- can subscribe to report pages and dashboards, snapshot sent to you by email

##### Get alerts when your data reaches a threshold
- notified when data changes beyond or beneath a threshold that you've set, use data alerts.
- email is sent when the value passes any upper or lower limit that is set
- you have the tools to explore and interact with the data to find answers to questions and to discover new insights. Additionally, you can:
    - Ask questions by using natural language.
    - Collaborate with your team.
    - Share what you discover.
    - Take action from your desk or on the go.
- Power BI is straightforward and delivers powerful data-backed business intelligence to help you answer questions, make decisions, track progress, make predictions, stay up-to-date on a regular cadence, etc.

### View content in the Power BI service
- **content:** apps, dashboards, and reports. Content is created by Power BI designers, who share it with colleagues like you
1. Home canvas displays and organizes your favorite and most recent content, along with recommended content and learning resources. Each piece of content displays as a tile, with a title and icon. Selecting a tile opens that content.
2. The global search box lets you search for content by title, name, or keyword.
3. On the side navigation pane, you can view lists of content and select the one to open.

#### Home canvas
- can view all content that you have permission to use
- also updates with recommended content and learning resources

##### Key metrics at a glance
- Home canvas = you can view all the content that you have permission to use
- Each piece of content is a tile, and selecting a tile takes you to that piece of content. For example, selecting a tile for a dashboard opens the dashboard.

#### Most important content at your fingertips
##### Favorites and frequents
- contains links to the content you visit most often or that you’ve tagged as a favorite

##### Recent and My apps
- displays the content you've visited most recently
- The **My apps** section lists apps that have been shared with you; the most recent apps are listed here.

##### Featured apps
Power BI displays a set of featured apps. Selecting an app tile opens the app.

##### Explore the navigation pane
- Use the navigation pane to locate and move between dashboards, reports, and apps
- The nav pane organizes your content into categories that are similar to what you’ve already seen on the Home canvas.
- To open one of these content sections and display a list of all items, select the heading.

##### Search all of your content
- You can enter the full or partial name of that dashboard and search for it.
- Additionally, you can enter your colleague’s name and search for content that they've shared with you.
- The search is scoped to look for matches in all the content that you own or have access to.











# 2. Get and transform data with Power BI
## Module 1 - Get data in Power BI
### Get data in Power BI
#### Get data from files
- **flat file:** a type of file that has only one data table and every row of data is in the same structure, file doesn't contain hierarchies
- e.g. comma-separated values (.csv) files, delimited text (.txt) files, and fixed width files. Another type of file would be the output files from different applications, like Microsoft Excel workbooks (.xlsx)
-  can find a list of the available options when you use the Get data feature in Power BI Desktop

##### Flat file location
- local
- OneDrive for Business
- OneDrive - personal
- SharePoint - Team Sites
Using a cloud option such as OneDrive or SharePoint Team Sites is the most effective way to keep your file and your semantic model, reports, and dashboards in Power BI in-sync

##### Connect to data in a file
- **TIP:** The Home tab contains quick access data source options, such as Excel, next to the Get data button.

##### Select the file data to import
- After the file has connected to Power BI Desktop, the Navigator window opens = shows you the data that is available in your data source (the Excel file in this example).
- can select a table or entity to preview its contents, to ensure that the correct data is loaded into the Power BI model.
- Select the check box(es) of the table(s) that you want to bring in to Power BI. This selection activates the Load and Transform Data buttons

  ![image](https://github.com/Nolu-M/Notes-code/assets/119700411/3276d66e-3f9d-4bef-acd2-9d8c19c249f6)

- Load button to automatically load your data into the Power BI model
- Transform Data button to launch the Power Query Editor, where you can review and clean your data before loading it into the Power BI model

##### Change the source file
- might have to change the location of a source file for a data source during development, or if a file storage location changes
- keep your reports up to date, you'll need to update your file connection paths in Power BI
- Power Query provides many ways for you to accomplish this task, so that you can make this type of change when needed.
    1. Data source settings
    2. Query settings
    3. Advanced Editor

**Warning:** If you are changing a file path, make sure that you reconnect to the same file with the same file structure. Any structural changes to a file, such as deleting or renaming columns in the source file, will break the reporting model.

- try changing the data source file path in the data source settings. Select Data source settings in Power Query. In the Data source settings window, select your file and then select Change Source. Update the File path or use the Browse option to locate your file, select OK, and then select Close.

    ![image](https://github.com/Nolu-M/Notes-code/assets/119700411/9f1ff98e-638c-4fa8-90b3-6bcb1b114330)







# 3. Model data with Power BI

# 4. Build Power BI visuals and reports

# 5. Distribute Power BI insights - 2 modules
## Module 1 - Publish and share in Power BI
### Introduction to using workspaces
sharing reports and dashboards with coworkers and friends

##### Share and collaborate with colleagues in Power BI
- Publish your reports from **Power BI Desktop** to the **Power BI service**.
- Create **Apps** that package a dashboard, report, and dataset to send to your colleagues, who can use the content pack as a starting point and further enhance it.
- Create **Groups**, which you can use as a security model to identify a subset of users who have access to dashboards, reports, and datasets that you create.
- **Publish to the web** so that live reports can be embedded in a webpage.

### Publish Power BI Desktop reports
- After you've completed writing your report, select the Publish button on the Home tab
- Power BI packages your report and data, including visualizations, queries, and custom measures, and uploads them to the Power BI service
- **NOTE:** It's common to refer to Power BI Desktop reports as .pbix files, which is the extension that they're given in Microsoft Windows.
- When the upload is complete, a dialog box appears, informing you that the publishing process succeeded, and provides a link to your report in the Power BI service.

### Print and export dashboards and reports
- In the Power BI service, select File in the top-left side of the service and then select Print this page to open a print dialog box.

#### Export data from a visual
- You can also export the data from any visual in the Power BI service. Select the ellipsis on any visual and then select Export to .csv.
- You can also print or export directly from a report. When you are viewing a report in the Power BI service, select File > Print to open the print dialog box.

#### Manually republish and refresh your data
- To update reports and datasets that you've already published from Power BI Desktop to the Power BI service, select Publish on the Home tab.
- When you republish a report in the Power BI service, you're prompted to confirm that you want to replace the previous dataset and reports.
- When you select Replace, the datasets and reports in the Power BI service are overwritten with the new datasets and reports.

### Introducing Power BI Mobile
- keep track of data while on the move
- Sign in to your account by using your Power BI service account information.
- first screen displays all the content to which you have access, including reports, dashboards, and groups. The workspace also includes sample dashboards that you can explore for inspiration.

- Tap any dashboard to open it. Within a dashboard, you can tap a dashboard tile to focus on it in a larger view. Note any insights that you discover by tapping the Annotate button.
    - **Annotate feature** allows you to draw on a focused tile to highlight areas of interest. The annotation tools are along the bottom of the screen.
    - Share your annotated tile by tapping the Share link.

### Create workspaces in Power BI
- **workspace:** defines a set of users who have access to specific dashboards, reports, and datasets.
- Workspaces are places to collaborate with colleagues to create and refine collections of dashboards, reports, and paginated reports
- 2 types of workspaces in Power BI:
    - **Classic workspaces:** groups are based on the groups in Microsoft 365. If you've been using Microsoft 365 groups to manage your group's email, calendar, and documents, then you'll find that Power BI offers the same features. When you create a group in Power BI, you're actually creating an Microsoft 365 group.
    - **New workspaces:** are now the default workspace in Power BI
        - Assign workspace roles to user groups: security groups, distribution lists, Microsoft 365 groups, and individuals.
        - Create a workspace in Power BI without creating a Microsoft 365 group.
        - Use more granular workspace roles for more flexible permissions management in a workspace.
        - The Power BI admin can control who can create workspaces in Power BI.
#### Setting up a new workspace
- By clicking on Workspaces users can Create a workspace which will allow everybody or nobody in an organization to create new workspaces.
- They can also limit creation to members of specific security groups.

#### Setting up a classic workspace
- same steps as setting up a new workspace, with an additional step
- In the workspace dialog box you need to click on revert to classic to set up a classic workspace
- In the Create a workspace dialog box, under Advanced you can click on Specific users and groups and type email addresses, security groups, and distribution lists. Then select Save to save the group.

#### Build apps
- Click on the workspace you published your Power BI Desktop report to, and select the Create app button in the upper right corner to start the process of creating and publishing an app from the workspace.
- **NOTE:** You cannot publish an app from "My Workspace"
- On Setup, fill in the name and description to help people find the app
- Choose whether to distribute the app to specific people or to groups, and then give the app a title. Provide a detailed description in the Description box so that people know what your app provides.
- On the bottom of the dialog box, you can upload an image for the app and then select the dashboard to include in the app. When you publish, the app is added to the organization's content gallery.

### Use apps
- Select the workspace that you previously created
- Power BI imports the dashboards, reports, and datasets that are in the app
- Create a copy of the app that you can use to make changes and keep it disconnected from the published version of the app. By creating a copy

### Update apps
- To edit an app that you created previously and see how other people use your app, start in the Power BI Service in My Workspace.
- Anytime that you make changes to the app you can click on Update app in the upper right hand side of the screen.
- The Update app dialog box will open, you can make your changes and click Update app.
- Power BI processes those changes and publishes the updated app to the app gallery.
    - If the distribution list is large you may get a notification like the one below. Anyone who has connected to your app will receive a message that the app has changed, and they will have the option to accept the changes or to keep the older version.
    - As the app owner, you can manage the versions that your colleagues are using.

### Integrate OneDrive for Business with Power BI
- use your Power BI and Office365 groups to collaborate and share by using Microsoft OneDrive for Business
- can use your Power BI and Office365 groups to collaborate and share by using Microsoft OneDrive for Business
- OneDrive for Business is a potential storage location for your Power BI content that provides version history --> can share your files with an Office365 group to enable several people to work on the same Power BI or Excel files.

- To connect to a PBIX (Power BI Desktop) file on OneDrive for Business, sign in to the Power BI service and select Get Data. Under Create new content, select Files, and then select OneDrive - Business. Highlight the file and then select Connect.

- Your content appears on the left-hand side navigation bar. File changes on the OneDrive for Business page will automatically reflect in the Power BI environment and will be recorded in the version history.

### Publish to web
- share a Power BI report on a webpage or share it through email. This feature of Power BI is often referred to as Publish to web.
-  select the report that you want to share so that it's displayed on the canvas. Then from the menu, select Share. A dialog box will appear so that you can share a link to the report
-  Power BI presents a dialog box where you can:
    - Share a link using email, which shows the report as a webpage
    - Copy the link to the report
    - Share the report using Microsoft Teams
    - Embed live data in a Microsoft PowerPoint file
 
 - can paste the email link into a browser and see your report as a webpage and can interact with that webpage just as you would if you were viewing the report in Power BI.

## Module 2 - Explore data in Power BI
### Introduction to the Power BI service
![image](https://github.com/Nolu-M/Notes-code/assets/119700411/bd50196b-465a-4201-b687-9f439bc58492)

- The Power BI service is the natural extension of Power BI Desktop
- can use its features for uploading reports, creating dashboards, and asking questions of your data by using natural language.
- can use the service to set data refresh times, share data with your organization, and create customized apps.
  
### Quick insights in Power BI
- Power BI service can automatically look for insights in a dashboard, report, or dataset
- From the list of items in your workspace, select the ellipsis beside the dataset that you're interested in and then select Get quick insights
    - Power BI searches the data for patterns and after about 15 seconds, the notification changes to let you know that Power BI found some insights.
    - select the View insights button on the notification, you're presented with a page of visuals. You can scroll down through the page to view and consider the visuals

- With Quick Insights, you can let Power BI do the work to spot outliers and trends in your data. Use those findings in your dashboards or continue to refine and filter to get to the insights that you need

### Create and configure a dashboard
- Dashboards in Power BI are one-page collections of visualizations that are created from within the Power BI service. You can create dashboards by pinning visuals from reports.
- To pin a visual, open its report on the Power BI service. Hover over the visual that you want to pin and select the pin icon.

- can select a destination dashboard for the visual from the drop-down menu or create a new dashboard.
- You can pin visualizations from multiple reports and pages to a single dashboard, allowing you to combine different datasets and sources into a single page of insights.
- After a visual has been pinned to a dashboard, it's called a tile
- dashboards appear in the navigation pane on the left side of the Power BI service
- Hover over a tile and select the pencil icon to open the Tile details form, where you can change information in the Title or Subtitle fields.

- Select a dashboard tile to view the report from which it originated. You can also change that link by using the Set custom link field on the Tile details form.
-  can pin tiles from one dashboard to another, for example, if you have a collection of dashboards and want to create one summary board.
    - hover over the tile and select the pin icon. Dashboards are simple to create and to change. You can customize your one-page dashboard to show exactly the information that it should

### Ask questions of your data with natural language
- get answers about your data is by asking questions in the Q&A feature of Power BI
- **NOTE:** Currently, Power BI Q&A only supports answering queries that are asked in English; however, a preview is available for Spanish that can be enabled by your Power BI administrator.

#### Explore Q&A
- can use Q&A to explore your data by using the intuitive, natural language capabilities of Power BI and receive answers in the form of charts and graphs

#### 1. Ask a question









### Create custom Q&A suggestions

### Share dashboards with your organization

### Display visuals and tile in full screen











# 6. Introduction to Power BI administration - 2 modules
## Module 1 - Understand the Power BI administrator role
### Introduction
- Power BI allows business users to access the data wherever it resides and gain actionable business insights
- Power BI allows users to:
    - Harness data from Excel spreadsheets, on-premises data sources, big data, streaming data, and cloud services
    - content packs = deliver a curated experience with pre-built dashboards for popular SaaS applications
    - Experience their data with speed and agility
    - use live dashboards that maintain a real-time pulse on the business and provide critical insights
    - Create custom visuals that bring data to life and surface intelligence hidden in the sea of data.
    - Benefit from natural language queries that enable users to ask questions of their data in an intuitive way.
    - Access data and insights anywhere with dashboards accessible via the desktop, web or across mobile devices.

- users take advantage of world-class data analytics capabilities from historical data sets and delivers ability to see data as it's happening in real-time, minimizing the need to analyze historical data.
    - Transitioning from historical intelligence to actionable real-time insights
    - Power BI seamlessly integrates with Microsoft business applications (apps) like Dynamics 365 and Office 365, arming users with insights directly within the Microsoft apps
    - integrating intelligence at the point of action leads to automation within systems that trigger commands based on preset thresholds, further operationalizing business insight throughout an organization.

### Power BI tools
- tools to promote optimal use fall into two categories:
    1. Power BI desktop
    2. Power BI service

#### Power BI desktop
- **Power Query Editor:** primary data preparation experience, connect wide range data sources & apply hundreds of different data transformations by previewing data and selecting transformations from the UI
- **Data modeling:**  Supports the process of creating a visual representation of a whole information system or parts of it to delineate connections between data points and structures
- **Visualization:** After you have a data model, you can drag fields onto the report canvas to create visuals, visual = graphic representation of the data in your model

#### Power BI service
- **datasets:** A source of data ready for reporting and visualization.
- **Reports:** Generate reports from the Power BI service from My Workspace or in a new workspace experience. You can also create reports from endorsed datasets
- **Dashboards:** A single page, often called a canvas, that tells a story through visualizations
- **Workspaces:** containers for dashboards, reports, workbooks, datasets, and dataflows, *My workspace* is the personal workspace for any Power BI customer to work with your own content and *Workspaces* are used to collaborate and share content with colleagues
- **Dataflows:** Reusable transformation logic that can be shared by many datasets and reports

### Steward or captain?
Are you a steward or a captain?
    ![image](https://github.com/Nolu-M/Notes-code/assets/119700411/4a26444e-7436-4e2c-9a34-cb998ff88e3b)

### Power BI administrator role
- helps the business and empowers the organization while enforcing rules and limits
- ![image](https://github.com/Nolu-M/Notes-code/assets/119700411/f62239e9-80a5-4cec-8007-b19e38fc295e)
- To administer Power BI for organization = must be one of the following roles:
    - Office 365 Global Administrator
    - Power BI Service Administrator
    - Microsoft Power Platform Service Administrator

- Key tasks such as licensing are managed by the Office 365 Global or billing administrator, and subscriptions are managed in the O365 admin tool.
- Power BI capacity and workspace administrator aren't part of Azure and are configured in Power BI.
- Microsoft Power Platform service administrator uses Microsoft Power Platform admin center to manage environments and settings for Power Apps, Power Automate,     - and the following customer engagement apps, Dynamics 365 Sales, Customer Service, Field Service, Marketing, and Project Service Automation.

### Typical administrative tasks

1. Office 365 global administrator:
    - **Assigning licenses:** In the Power BI service, users have defined capabilities based on the type of per-user license they have (free or Pro) and whether the content they're interacting with is in a workspace assigned to a Power BI Premium capacity. Licenses are assigned in the O365 portal and you must be a global or user - account administrator to assign these licenses.
    - **Audit logging:** Gather telemetry data, unique users - launches for Power BI users. 
3. Power BI administrator:
    - **Controlling access:** Control user access to record-level and task-based privileges.
    - **Controlling Power BI tenant features:** Tenant settings are managed in the admin portal and can restrict capabilities and features to a limited set of users.
    - **Activity log:** Knowing who is taking what action on which item in your Power BI tenant can be critical in helping your organization fulfill its requirements, like meeting regulatory compliance and records management. 
    - **Monitoring usage:** Monitor how your dashboard and reports are being used. Views per day, unique users per day, views per user, and shares per day are a few of the metrics that can be reported on and monitored.
4. Microsoft Power Platform administrator:
    - **Manage gateways**: On-premises data gateways act as a bridge, providing quick and secure data transfer between on-premises data - data that isn't in the cloud, and Power BI, Power Automate, Logic Apps, and Power Apps services.

### Typical administrator tools
![image](https://github.com/Nolu-M/Notes-code/assets/119700411/c74deb47-aa93-4c0c-9b4d-881b6887392b)

- **Power BI admin portal:** Used to manage a Power BI tenant, including the configuration of governance policies, usage monitoring, and provisioning of licenses, capacities, and organizational resources
- **Power BI gateway management:** view and manage on-premises data gateways
- **Microsoft Power Platform admin center:** Provides a unified portal for administrators to manage environments and settings for Power Apps, Power Automate, and customer engagement apps (Dynamics 365 Sales, Dynamics 365 Customer Service, Dynamics 365 Field Service, Dynamics 365 Customer Insights - Journeys, and Dynamics 365 Project Service Automation).
- **Microsoft 365 admin center:** manage users and their license assignment and you can launch into many of the individual admin centers from here.
- **Security & compliance center:** administrators can come here to search the Audit log to see Power Automate audit events.
- **Azure Active Directory portal:** Advanced Azure AD management tasks such as conditional access is managed here, any developer application registration is also done here and it's also where you start setup of your on-premises gateways.
- **Powershell:** owerShell cmdlets for app creators and administrators, you can automate many of the monitoring and management tasks that are only possible manually today in Power Apps.
- **REST APIs:** Automate common Power BI administrator tasks with REST APIs. 

## Module 2 - Establish a Power BI environment
### Introduction
- **Power BI tenant:** an additional service subscription and a part of an Office 365 suite that is attached to a domain
    - When setting up a Power BI environment, you need to understand in which Azure data store the Power BI tenant will be located. Tenant location is based on an organization's Office 365 country;region or Azure Active Directory (AAD) data center.
    - Power BI tenant should reside in the same Azure region as other O365 services the organization uses.
 
#### How to determine where your Power BI tenant is located
- find region tenant is in and:
    - In the Power BI service, in the top menu, select help (?) then About Power BI.
    - Look for the value next to Your data is stored in. It's the region where your tenant is located. value is also the region where your data is stored unless you're using capacities in different regions for your workspaces.

#### How the data region is selected
- based on the country or region you select when you create the tenant.
- selection applies to sign up for both Microsoft 365 and to Power BI, because this information is shared. If this is a new tenant, select the appropriate country/region from the list when you sign up
- Power BI chooses a data region closest to your selection, which determines where data is stored for your tenant.
- **IMPORTANT:** You cannot change the country/region selection after you create the tenant.

#### Other things to keep in mind about tenant location
- Power BI tenants are created in an Azure Data Center.
- Tenant location is based on Office 365 country/region or Azure Active Directory data center.
- Think about other Azure services the organization might be considering. Choosing the wrong location could result in Egress charges.

### User accounts versus guest accounts
- **User accounts** are created in the Azure AD tenant. These users can consume content based on access level and license type
- **Guest accounts:** are external to the organization. These accounts are part of Azure AD B2B and B2C, and enable users external to the organization to consume or even edit content. The B2C approach allows users with accounts like @gmail and @outlook to view Power BI content.

#### User accounts
- Exist within the organization
- Can create and consume content based on access and license
- Mobile app can be used

#### Guest accounts
- External to the organization
- Part of Azure AD B2B & B2C
- Can consume content (or edit with appropriate permissions)
- Must have direct URL to shared content
- Can be consumer accounts such as @outlook.com or @gmail.com)
- **NOTE:** The Power BI mobile app cannot be used for external content.

### Power BI licensing
There are two ways for users to get a license:
- Power BI admins can assign an existing license to users.
- Users can use their work or school account to sign up for a free Power BI Desktop license, or purchase a Power BI Pro, or Power BI Premium.
    ![image](https://github.com/Nolu-M/Notes-code/assets/119700411/f7a67a1e-9d27-4ed7-a396-7ffa759b0f94)

#### Who can purchase and assign licenses?
- must have a Microsoft 365 admin role to purchase or assign licenses for your organization.
- ![image](https://github.com/Nolu-M/Notes-code/assets/119700411/3a35174e-f2bf-4fa6-9eb8-04272128f639)

#### License types
- To use the Power BI service, users must sign in with an identity that Azure Active Directory supports for commercial licenses.
- can add Power BI to any Microsoft license that uses Azure Active Directory for identity services. Some licenses, such as Microsoft 365 E5, include a Power BI Pro license, so no separate sign-up for Power BI is needed.
- two kinds of Power BI licenses for organizations:
    - **standard, self-service Power BI Pro license**, Microsoft 365 admins assign per user licenses. There's a per user monthly fee for Power BI Pro licenses. This license type enables collaboration, publishing, sharing, and ad-hoc analysis. Content is saved to shared storage capacity that is fully managed by Microsoft.
    - **Power BI Premium license** allocates a capacity to an organization. Suitable for enterprise BI, big data analytics, and cloud and on-premises reporting, Premium provides advanced administration and deployment controls.

- Dedicated compute and storage resources are managed by capacity admins in the organization.
- In addition to other Premium advantages, content stored in Premium capacity can be accessed by and distributed to users who don't have Power BI Pro licenses. At least one user must have a Power BI Pro license assigned to use Premium, and content creators and developers still need a Power BI Pro license.

- **NOTE:** The two types of licenses aren't mutually exclusive. You can have both Power BI Premium and Power BI Pro. In this configuration, content stored in Premium capacity can be shared with all users and shared capacity is also available. 

</details>

<details>
    <summary>Cloud Computing</summary>
    
# Module 1: Cloud Computing Fundamentals
## 1. Understanding Cloud Computing

### What is the Cloud
- cloud computing has revolutionized how organizations operate by offering essential features like on-demand access to computing power and storage = unlimited scalability and flexible pricing models
- cloud technologies focused on cost reduction and shifting technology expenditures from capital to operational expenses

- Five characteristics defined by National Institute of Standards and Technology (NIST):
  - **On-Demand Self-Service:** Cloud services consumers can provision services on an as-needed basis, without the need to work with the CSP (Cloud service provider) directly i.e. compute power, additional storage, new websites, or even database services. Consumer = expand (or reduce) services without need for human assistance from CSP.
  - **Broad Network Access:** Client devices and traditional server deployments are able to access cloud-based resources across the network.
  - **Resource Pooling:** Cloud service provider (CSP) pools resources in a multitenant model and adjusts resource allocation on an on-demand basis, and the specific distribution of hardware resources is abstracted from the consumer. Pool network, storage, and compute capabilities and then dynamically and automatically allocate those resources to consumers on an on-demand basis.
  - **Rapid Elasticity:**Resources are provisioned and released to adjust for changes in demand and consumption = manual or automatic process.
  - **Measured Service:** Monitored, controlled and billable. CSPs meter the utilization of their resources. 

### Cloud Computing Ecosystems
#### Cloud Computing Ecosystem
Ecosystem of participants defines the market - 3 categories:
- **Consumers of Services:** Everyday end-users (like yourself or your colleagues) that use cloud services in their day-to-day business activities. Examples include Microsoft OneDrive, Google Drive and iCloud.
- **Provider of Services:** Examples of providers include Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform (GCP), IBM Cloud , Oracle Cloud Infrastructure and Alibaba Cloud.
- **Designer of Services:** Companies that specialise in designing and implementing cloud technologies include Accenture, Deloitte, Capgemini, IBM, PricewaterhouseCoopers (PwC), Cognizant, Wilpro, Tata Consultancy Services (TCS), Infosys, and DXC Technology.

##### Understanding Cloud Concepts
- *Cloud computing* = method of providing shared computing resources, including applications, computing, storage, networking, development and deployment platforms as well as business processes.
- *Standardization* = implementation of services using consistent approach supprted by a set of consistent interfaces.
- *Automation* = process triggered based on business rules, resource availability, and security demands. Required to support a self-service provisioning model, for efficiency = automation ensures after provisioned service is no longer needed, it is returned to the resource pool.

- Microsoft 365, Slack or DocuSign service are cloud based services

### Understanding Cloud Deployment Models
#### Cloud Components and Clients
3 main components in a cloud services solution = client platform from which cloud services being accessed, data center where cloud services are being hosted and network connection between those two points.

![image](https://github.com/Nolu-M/Notes-code/assets/119700411/525dad69-7484-4dce-900e-3d3085617f2e)

![image](https://github.com/Nolu-M/Notes-code/assets/119700411/ebd2cb22-d139-49ee-89db-5616d8da2a58)

- cloud services include storage, email, e-commerce, office suites, and development environments, among others
-  The primary operating systems used on these client devices include Microsoft Windows, Apple macOS, Linux, iOS, and Android.
-  network serves as the pathway connecting the client devices to the data centers of the CSPs

- cloud service infrastructure can be managed internally by a single organization for its own use or managed by a CSP that provides services to many organizations. These two models can be combined into a hybrid solution:
    1. **Public cloud:** A CSP owns the cloud deployment and allocates its resources to external, unaffiliated customers. Those customers share the public cloud’s resources without knowing precisely where their data is in relation to that of any other organization.
    2. **Private cloud:** Services are provided to only a single organization.
    3. **Hybrid cloud:** There is a combination of two or more private, public, or community deployments.
 
#### Types of Cloud Computing

**NOTE: Clouds come in different versions, depending on your needs. There are two primary deployment models of the cloud: public and private. Most organizations will use a combination of private computing resources (data centers and private clouds) and public services, where some of the services existing in these environments interact with each other — which is what we call a hybrid cloud environment.**

- **multicloud environment:** a variety of public cloud services to support different developer and business units. Grown in popularity because developers want access to the platform of their choice, and businesses want the flexibility to move between vendors.

![image](https://github.com/Nolu-M/Notes-code/assets/119700411/3d89af23-47cd-4f88-9d84-3c443cc0b5aa)

##### The Public Cloud
- public cloud = a set of hardware, networking, storage, services, applications, and interfaces owned and operated by a third party for use by other companies or individuals.
- CSPs offer public cloud services to virtually any customer. Customers use a subscription model to pay for access.

- Amazon and Microsoft are two major public cloud vendors (though they each also offer private cloud deployment options)

##### The Private Cloud
- a set of hardware, networking, storage, services, applications, and interfaces owned and operated by an organization for the use of its employees, partners, or customers.
- can be created and managed by a third party for the exclusive use of one enterprise.
- The organization retains complete control of the cloud deployment but can leverage the advantages of cloud technologies.
- sits behind a firewall, highly automated with a focus on governance, security, and compliance.





## 2. Embracing the Business Imperative
## 3. Architectural Considerations for the Cloud environment
## 4. Managing a Hybrid and Multicloud Environment
## 5. Standards in a Multicloud World
## 6. A closer Look at Cloud Services












</details>






