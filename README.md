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
<summary> Data Analytics Week-1</summary>
    
# Day 1:
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
      
### learning new Computing Skills
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



</details>









