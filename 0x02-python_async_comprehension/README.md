# Asynchronous Comprehensions and Generators

### How to Write an Asynchronous Generator

- **Definition**: An asynchronous generator is a function that contains `async def` and uses `yield` to produce a series of values over time.
- **Syntax**:
  ```python
  async def async_gen():
          for i in range(10):
                  yield i
  ```
- **Usage**: Asynchronous generators are used with `async for` loops to iterate over the values they produce.

### How to Use Async Comprehensions

- **Definition**: Async comprehensions allow you to use asynchronous generators within list, set, dict, and generator comprehensions.
- **Syntax**:
  ```python
  result = [i async for i in async_gen()]
  ```
- **Benefits**: They provide a concise way to create collections from asynchronous data sources.

### How to Type-Annotate Generators

- **Type Hints**: Use `Generator`, `AsyncGenerator`, `Iterator`, and `AsyncIterator` from the `typing` module to annotate generators.
- **Example**:

  ```python
  from typing import AsyncGenerator

  async def async_gen() -> AsyncGenerator[int, None]:
          for i in range(10):
                  yield i
  ```

Understanding these concepts will help you effectively use asynchronous programming features in Python, improving the efficiency and readability of your code.

## Resources

- **PEP 530 – Asynchronous Comprehensions**: [PEP 530](https://www.python.org/dev/peps/pep-0530/)
- **What’s New in Python: Asynchronous Comprehensions / Generators**: [Python Docs](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep530)
- **Type-hints for generators**: [Type Hints](https://docs.python.org/3/library/typing.html#typing.Generator)
