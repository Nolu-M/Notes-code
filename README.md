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

# Day 2:
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

# Day 3:
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

# Day 4:
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




</details>









