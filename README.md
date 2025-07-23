# Callback_and_Decorator
This repo introduces Callback and Decorator in Python. <br >
The document is referred to the following websites:<br >
[1] Callback functions in Python – A Complete Overview: https://www.askpython.com/python/built-in-methods/callback-functions-in-python<br >
[2] Understanding CallBacks using Python Part 1: https://medium.com/analytics-vidhya/understanding-callbacks-a22e8957a73b<br >
[3] Understanding CallBacks using Python — Part 2: https://medium.com/analytics-vidhya/understanding-callbacks-using-python-part-2-e71c17fed7e2<br >

## Callback:
What is a callback function:<br >
A callback function is a function that I can pass as an argument into another function. <br >
A function is a callback function if it satisfies 2 factors:<br >
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

