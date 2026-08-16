# Pair Python Programming — Exercises

## Overview

Python Exercises for Senior Engineers (built-in libraries only).

Work in pairs and complete any 7 of the questions below. Each question should be solved with clear, well-documented Python code using only the standard library.

---

## Exercises (choose any 7)

1. Unique elements from a list
	- Write a function that takes a list and returns a new list containing the unique elements from the input (preserve order if possible).

2. Perfect number checker
	- Write a function to check whether a number is perfect. A perfect number equals the sum of its proper divisors (excluding the number itself).

3. Max–min digit difference
	- Write a function that accepts a number (or string of digits) and returns the difference between the largest and smallest numbers that can be formed using its digits.
	- Example: input `"213"` -> `321 - 123 = 198` (return `198`).

4. Pizza toppings loop
	- Write a loop that repeatedly prompts the user to enter pizza toppings until they enter a sentinel value such as `quit`.
	- For each topping entered, print a message like "I'll add <topping> to your pizza." Ensure the loop handles case-insensitive `quit` and empty input.

5. Movie ticket price loop
	- A theatre charges tickets by age:
	  - under 3: free
	  - 3 to 12: $10
	  - over 12: $15
	- Write a loop that asks users for their age and prints the ticket price. Allow repeated queries until the user chooses to stop.

6. Fibonacci series (two implementations)
	- Implement functions that generate/display the Fibonacci sequence both recursively and iteratively (without recursion).

7. Favorite pizzas (list and loop)
	- Think of at least three favorite pizzas and store their names in a list.
	- Use a `for` loop to print each pizza name.
	- Modify the loop to print a sentence for each pizza, e.g. "I like pepperoni pizza."
	- After the loop, print a final line that states how much you like pizza (a short paragraph of 2–3 sentences).

8. Loop with squares and conditional continue
	- Iterate over numbers 0 through 9, compute each number's square, and check if the number is divisible by 2.
	- If divisible by 2, `continue` the loop; otherwise, print the number and its square.

9. Anagram checker
	- Explain what an anagram is and write a function to determine whether two given strings are anagrams of each other. Handle case and whitespace appropriately.

10. Set union without duplicates
	- Write a Python program that returns a new set containing unique items from two sets (i.e., the union), ensuring there are no duplicate items in the result.

---

## Capstone Project (choose 1)

Select one of the capstone projects below and implement a clean, well-tested solution.

### Task 1 — Rule-based Chatbot

- Build a rule-based chatbot that:
  - Responds to greetings, simple questions, and farewells.
  - Uses regular expressions for pattern matching.
  - Maintains basic context (a short memory of previous user inputs) to provide context-aware replies.
  - Categorizes responses into: greetings, questions, farewells, and unknowns.

### Task 2 — AI-Powered Data Cleaning Assistant

- Build a Python tool to detect and resolve common data quality issues in structured datasets (CSV or Excel). Features should include:
  - Missing value detection and imputation strategies
  - Outlier detection
  - Data type correction
  - Duplicate detection and resolution

---

## Submission notes

- Include example inputs and outputs for each exercise you complete.
- Keep solutions in separate, clearly named Python modules or notebooks.
- Add brief docstrings and, where appropriate, unit tests demonstrating correctness.

Duplicate Detection 

 