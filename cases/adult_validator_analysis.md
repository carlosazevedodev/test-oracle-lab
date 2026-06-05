# Case Study: Adult Age Validator

## Requirement

A user should be considered an adult only if they are 18 years old or older.

## Buggy Implementation

```python
def is_adult(age: int) -> bool:
    return age >= 16
