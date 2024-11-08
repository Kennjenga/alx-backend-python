# Unit and Integration Testing

## Unit Testing

Unit testing is the process of testing that a particular function returns expected results for different sets of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

## Integration Testing

Integration tests aim to test a code path end-to-end. In general, only low-level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

## Running Tests

Execute your tests with:

```bash
$ python -m unittest path/to/test_file.py
```

## Resources

Read or watch:

- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
- [unittest.mock — mock object library](https://docs.python.org/3/library/unittest.mock.html)
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock)
- [parameterized](https://pypi.org/project/parameterized/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- **The difference between unit and integration tests**: Understand the scope and purpose of unit tests (testing individual functions or methods in isolation) versus integration tests (testing the interaction between multiple components or systems).

- **Common testing patterns such as mocking, parameterizations, and fixtures**:
  - **Mocking**: Learn how to replace parts of your system under test with mock objects and make assertions about how they have been used.
  - **Parameterizations**: Understand how to run a test with multiple sets of inputs to ensure your code works as expected for various cases.
  - **Fixtures**: Learn how to set up and tear down the test environment, ensuring that each test runs in isolation and has the necessary context to execute correctly.
