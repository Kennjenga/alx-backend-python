# Python Async Function

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without the help of Google:

### 1. `async` and `await` Syntax

- **Illustration**:

  ```python
  import asyncio

  async def main():
      print('Hello')
      await asyncio.sleep(1)
      print('World')

  asyncio.run(main())
  ```

### 2. How to Execute an Async Program with `asyncio`

- **Illustration**:

  ```python
  import asyncio

  async def say_hello():
      await asyncio.sleep(1)
      print('Hello, Async!')

  asyncio.run(say_hello())
  ```

### 3. How to Run Concurrent Coroutines

- **Illustration**:

  ```python
  import asyncio

  async def task1():
      await asyncio.sleep(1)
      print('Task 1 completed')

  async def task2():
      await asyncio.sleep(2)
      print('Task 2 completed')

  async def main():
      await asyncio.gather(task1(), task2())

  asyncio.run(main())
  ```

### 4. How to Create `asyncio` Tasks

- **Illustration**:

  ```python
  import asyncio

  async def my_task():
      await asyncio.sleep(1)
      print('Task executed')

  async def main():
      task = asyncio.create_task(my_task())
      await task

  asyncio.run(main())
  ```

### 5. How to Use the `random` Module

- **Illustration**:

  ```python
  import random

  def random_number():
      return random.randint(1, 100)

  print(random_number())
  ```
