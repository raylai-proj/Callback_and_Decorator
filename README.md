# Callback_and_Decorator
This repo introduces Callback and Decorator in Python. <br >
The document is referred to the following websites:<br >
[1] [Callback functions in Python – A Complete Overview](https://www.askpython.com/python/built-in-methods/callback-functions-in-python)<br >
[2] [Understanding CallBacks using Python Part 1](https://medium.com/analytics-vidhya/understanding-callbacks-a22e8957a73b)<br >
[3] [Understanding CallBacks using Python — Part 2](https://medium.com/analytics-vidhya/understanding-callbacks-using-python-part-2-e71c17fed7e2)<br >
[4] [Programiz - Python Decorator (With Examples)](https://www.programiz.com/python-programming/decorator)<br >
[5] [A Practical Guide to Python's @property Decorator (with Examples)](https://dev.to/amohgodwin/a-practical-guide-to-pythons-property-decorator-with-examples-26mo)<br >
[6] [Reddit - Can you explain what decorator is like I’m 5?](https://www.reddit.com/r/Python/comments/935uzw/can_you_explain_what_decorator_is_like_im_5/)<br >
[7] [Geekster - Datetime.Strftime() Function In Python](https://www.geekster.in/articles/python-strftime/)<br >
[8] [Python strftime cheatsheet](https://strftime.org/)<br >
[9] [datetime — Basic date and time types](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp)<br >
[10] [GeekforGeeks - Extract time from datetime in Python](https://www.geeksforgeeks.org/python/extract-time-from-datetime-in-python/)<br >

## Callback:
What is a callback function:<br >
A callback function is a function that is passed as an argument to another function and is invoked inside that function.<br >
A function is considered a callback function if it satisfies two conditions:<br >
- It is passed as an argument into another function.<sub>[1]</sub><br >
- It is called from inside that function.<sub>[1]</sub><br >

Therefore, when I pass a function (called A) as an argument into another function (called B), and function B calles the function A in it. Then function A is a callback function.<br >
## Advantage of callback function:
1. Separate the base function and custom behavior: Developers can generate customized callback functions, in the mean time, not affect the original base function. <br >
2. The base function can remain clean and reusable.<br >
3. Allow the base function to extend different customized behaviors.<br >
## Callback Example<sub>[2]</sub>:
```python
def caller(callback):
    """Accept function and calls in it."""
    print(
        "1. Caller accepts function as an argument.\n"
        "2. Caller calls that function in its own function."
    )
    callback()
    print(
        "When these 2 factors satisfied, the function that caller accepts is a callback function."
    )


def callback_func():
    """Input as an argument of another function."""
    print(
        "\n*\nThis is a callback function which is an argument of another function.\n*\n"
    )

caller(callback_func)
```
## Decorator:
What is a decorator:<br >
1. A decorator is a type of callback function usage, which it accepts a function as an argument and wrap it to a new function.<sub>[4]</sub><br >
2. In using decorator, python provides a method adding `@` with decorator's name in front of function to wrap that function to a new function.<br >
A function is a decorator if it satisfies 2 factors:<br >
- The function accepts another function and returns a new function.<br >
- The function has `@[function_name]` in front of another function.<br >

The difference between callback and decorator is that:<br >
Unlike the callback function works when it is **called**, the decorator works when it is **defined**.<br >
Here is a good explanation which I found according to **catcradle5**<sub>[6]</sub>:<br >
> A function that takes a function and returns a function. It's useful if you want something to be done before or after a function is executed and you also want to apply this to a lot of functions.<br >

## Advantage of decorator compare to callback:<br >
1. Decorator with `@[function_name]` automatically wraps the function into the new function, unlike callbacks has to manually pass into functions everytime.<br >
2. Decorator wrap the function at **definition**, unlike callbacks wait until **calling** phase.<br >

## Decorator Example<sub>[7][8][9][10]</sub>:<br >
```python
def decorator_func(callee):
    """Accept callee function and decorate it with wrap_func and return new function."""

    def wrap_func(*args, **kwargs):
        """Wrap up callee to new function."""
        first_run = datetime.datetime.strptime(FRISTRUN, "%Y-%m-%d %H:%M:%S")
        first_run = first_run.strftime("%A %#I:%M:%S %p, %B %d, %Y")
        print(f"The decorator_func build at {first_run}.")
        callee(*args, **kwargs)
        print("Funciton was wrapped up")

    # The decorator_func accept callee function and return type has to be a function.
    return wrap_func


@decorator_func
def check_today(current):
    """Check today to compare to the first time the code was developed."""
    current = current.strftime("%A %#I:%M:%S %p, %B %d, %Y")
    print(f"Today, we run the function at {current}")

# Demonstrate decorator.
today = datetime.datetime.now()
check_today(today)
```
## @Property decorator:<br >
What is @property decorator:<br >
@property decorator is a python decorator turns a class method into a property, so you can access it like class attribute.<sub>[2]</sub><br >
## Advantage of @property:<br >
1. Instead of calling a method `object.method()`, you can access it like class attribute `object.method`.<sub>[2]</sub><br >
## @property example:<sub>[2]</sub><br >
In addition to @property, python also provide @[function_name].setter and @[function_name].deleter to complete attribute functionalities:<br >
```python
class proj_progress(object):
    """A class allows user access attribute with . using @property."""

    def __init__(self, date):
        """Initialize project progress object with deadline."""
        self._deadline = date

    @property
    def deadline(self):
        """Get current deadline of project."""
        try:
            return self._deadline
        except Exception as e:
            print(f"Exception: {e}")

    @deadline.setter
    def deadline(self, date):
        """Set up new deadline of project."""
        self._deadline = date

    @deadline.deleter
    def deadline(self):
        """Delete self._deadline property."""
        try:
            del self._deadline
        except Exception as e:
            print(f"Exception: {e}")

# Demonstrate @property.
new_proj = proj_progress(date=90)
print(f"new_proj deadline is {new_proj.deadline} days")
new_proj.deadline = 120
print(f"Updated new_proj deadline is {new_proj.deadline} days")
del new_proj.deadline
print(f"Let's find out if deadline still exist: {new_proj.deadline}")
```
## Code Explanation:<br >
- @property: Allow access new_proj's deadline as access attribute `print(new_proj.deadline)`<br >
- @deadline.setter: Allow set new deadline as like change value of an attribute `new_proj.deadline = 120`<br >
- @deadline.deleter: Allow delete a property as like delete an attribute `del new_proj.deadline`<br >
