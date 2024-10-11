# Type Annotations in Python 3

![Python --- strongly dynamically typed](./strongly dynamically typed.png)

Type annotations in Python 3 allow you to specify the expected data types of function arguments and return values. This helps improve code readability and maintainability by making the code's intent clearer. Here's an example:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

In this example, `name` is expected to be a string, and the function returns a string.

## Specifying Variable Types

You can also use type annotations to specify the types of variables:

```python
age: int = 25
height: float = 5.9
is_student: bool = True
```

## Duck Typing

Duck typing is a concept in Python where the type or class of an object is less important than the methods it defines. If an object implements the required methods, it can be used in place of another object. This is often summarized as "If it looks like a duck and quacks like a duck, it must be a duck."

For example:

```python
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(duck):
    duck.quack()

d = Duck()
p = Person()

make_it_quack(d)  # Quack!
make_it_quack(p)  # I'm quacking like a duck!
```

## Validating Code with mypy

`mypy` is a static type checker for Python. It checks the type annotations in your code and ensures that they are being used correctly. To use `mypy`, first install it:

```sh
pip install mypy
```

Then, run `mypy` on your Python file:

```sh
mypy your_script.py
```

If there are any type errors, `mypy` will report them, helping you catch potential bugs early.
