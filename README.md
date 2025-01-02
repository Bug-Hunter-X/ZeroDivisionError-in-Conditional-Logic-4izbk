# ZeroDivisionError in Conditional Logic

This repository demonstrates a Python code snippet that contains a subtle `ZeroDivisionError`. The error is not immediately obvious because it depends on the input values.  This example helps to showcase how easily logic errors can lead to unexpected runtime exceptions.

## How to reproduce:

1. Clone the repository.
2. Run `bug.py` with the input `a = 0` and `b = any value`.  The code will raise a `ZeroDivisionError`.
3. Run `bug.py` with the input `a = any value (not 0)` and `b = any value`. The code will run without error. 
4. Run `bugSolution.py` to see a corrected implementation that handles potential `ZeroDivisionError`. 

## Understanding the bug:

The `ZeroDivisionError` is caused by dividing `b` by `a` when `a` is 0. This situation is easily missed if one doesn't carefully check the conditions in the `if` statement.

## Solution:

The corrected version handles the potential error gracefully using exception handling or by explicitly checking for the condition that would cause the error before performing the division. 