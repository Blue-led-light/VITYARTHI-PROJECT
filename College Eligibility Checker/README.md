# College Eligibility Checker

## What this project does

This is a small Python program that takes a student's Class 12 marks and checks them against a few sample eligibility rules.

The student enters their name, number of drop years, and marks in six subjects. The program then shows the result for JEE, NEET UG, state government colleges, VITEEE, and BITSAT.

The rules in this project are simplified examples for learning. They are not official admission criteria.

## Features

- Takes the student's name and checks that it is not blank.
- Accepts a non-negative number of drop years.
- Validates marks so they stay between 0 and 100.
- Checks five different eligibility categories.
- Prints the student's marks and eligibility results at the end.
- Keeps input, eligibility checks, and output in separate files.

## Example rules

The project currently uses the following sample rules:

- **JEE:** At least 375 total marks in Physics, Chemistry, Mathematics, Computer, and English, with no more than two drop years.
- **NEET UG:** At least 150 total marks in Physics, Chemistry, and Biology, with at least 33 marks in Biology.
- **State government colleges:** At least 180 total marks in Physics, Chemistry, Mathematics, and Biology, with no more than three drop years.
- **VITEEE:** At least 180 total marks in Physics, Chemistry, and Mathematics, with at least 50 marks in Mathematics and no more than two drop years.
- **BITSAT:** At least 225 total marks in Physics, Chemistry, and Mathematics, with at least 60 marks in each of those subjects and no more than one drop year.

These are only sample rules and should not be used as official admission advice.

## Project structure

```text
main.py
collect_student_data.py
read_mark.py
result_printer.py
eligibility/
    bits.py
    jee.py
    neet.py
    state_colleges.py
    vit.py
```

Each part of the program has a simple job:

- `collect_student_data.py` handles the student's input.
- `read_mark.py` validates individual marks.
- The files inside `eligibility/` contain the different checks.
- `result_printer.py` handles the final output.
- `main.py` connects everything together.

## Running the project

You only need Python 3.

From the project folder, run:

```bash
python main.py
```

Then enter the requested details when the program asks for them.

## Basic testing

A few useful things to test are:

1. Enter normal marks and check that all five results are printed.
2. Leave the name blank and make sure the program asks again.
3. Enter text instead of a number for drop years or marks.
4. Try a negative number of drop years.
5. Try marks below 0 or above 100.
6. Test marks just below and just above the eligibility limits.
