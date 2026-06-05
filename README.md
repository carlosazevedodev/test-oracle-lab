# test-oracle-lab
# Test Oracle Lab

A Python project focused on software quality analysis, requirement validation, and test effectiveness.

## Overview

One of the most common problems in software development is assuming that passing tests automatically mean the implementation is correct.

In reality, test suites can be incomplete, poorly designed, or misaligned with the actual business requirements. As a result, incorrect implementations may pass all tests while still violating the intended behavior.

This repository contains practical examples that demonstrate the difference between:

* Passing tests
* Correct implementations
* Well-defined requirements
* Effective test coverage

## Objective

The goal of this project is to analyze situations where:

* Requirements are partially or incorrectly validated.
* Tests pass despite implementation defects.
* Edge cases are missing from the test suite.
* Boundary conditions are not covered.
* Test coverage creates a false sense of correctness.

## Example Scenario

### Requirement

A user should be considered an adult only if they are 18 years old or older.

### Buggy Implementation

```python
def is_adult(age: int) -> bool:
    return age >= 16
```

### Weak Tests

```python
def test_adult_user_returns_true():
    assert is_adult(20) is True

def test_child_user_returns_false():
    assert is_adult(10) is False
```

### Result

All tests pass.

However, the implementation incorrectly classifies 16 and 17-year-old users as adults.

### Problem

The test suite validates only obvious scenarios and fails to verify the actual business rule.

This demonstrates a common quality issue where passing tests do not guarantee that the underlying requirement has been satisfied.

## Repository Structure

```text
test-oracle-lab/
│
├── src/
│   └── validators.py
│
├── tests/
│   ├── test_weak_tests.py
│   └── test_strong_tests.py
│
├── cases/
│   └── adult_validator_analysis.md
│
├── requirements.txt
└── README.md
```

## Topics Covered

* Requirement Analysis
* Test Validation
* Boundary Testing
* Edge Cases
* Software Quality
* Root Cause Analysis
* Test Design
* Technical Review

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the test suite:

```bash
pytest
```

## Why This Matters

In many software quality workflows, automated tests become the source of truth.

When tests are incomplete or misaligned with requirements, incorrect solutions can be accepted as valid. Identifying these situations requires technical judgment, critical thinking, and a deep understanding of how requirements, implementations, and tests interact.

This repository explores those scenarios through simple, reproducible Python examples.
