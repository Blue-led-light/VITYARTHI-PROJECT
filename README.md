# College Eligibility Checker

## Overview

This is a small Python project I built to help students quickly compare their Class 12 marks with a few common college and entrance exam eligibility rules. The program asks for the student’s name, number of drop years, and their marks in major subjects, and then checks how they match up against sample criteria for JEE, NEET UG, state government colleges, VITEEE, and BITSAT.

It is meant for learning and demonstration, not for official admission decisions.

## Features

- Accepts a student’s name and rejects empty input
- Takes a non-negative number of drop years
- Validates marks from 0 to 100 for Physics, Chemistry, Mathematics, Biology, Computer, and English
- Re-prompts the user if any value is invalid
- Checks eligibility against five different categories
- Displays a final summary with the student’s details and results

## Sample Rules

The project currently uses these example rules:

- **JEE:** Total of Physics, Chemistry, Mathematics, Computer, and English must be at least 375, and the student must have no more than two drop years. The result also distinguishes between zero/one drop year and two drop years.
- **NEET UG:** Total of Physics, Chemistry, and Biology must be at least 150, with at least 33 in Biology.
- **State government colleges:** Total of Physics, Chemistry, Mathematics, and Biology must be at least 180, with no more than three drop years.
- **VITEEE:** Total of Physics, Chemistry, and Mathematics must be at least 180, with at least 50 in Mathematics and no more than two drop years.
- **BITSAT:** Total of Physics, Chemistry, and Mathematics must be at least 225, with at least 60 in each subject and no more than one drop year.

These checks are included only to show modular Python programming and are not official academic criteria.

## Technologies

- Python 3
- Standard library only; no external packages required

## Project Structure

├── main.py
├── collect_student_data.py
├── read_mark.py
├── result_printer.py
└── eligibility/
    ├── jee.py
    ├── neet.py
    ├── state_colleges.py
    ├── vit.py
    └── bits.py


Each file handles a specific part of the program. The main script brings everything together by collecting input, checking eligibility, and printing the final result.

## Installation and Run

1. Install Python 3 if it is not already installed.
2. Clone or download this repository and open a terminal in the project folder.
3. Run:
    python main.py

4. Enter your name, drop years, and marks when prompted.

No extra setup is needed for this project.

## Testing

1. Run `python main.py` and enter a valid name, `0` drop years, and marks like `80` for every subject. Check that the output includes the name, all six marks, and all five eligibility results.
2. Run it again with a blank name and make sure the program asks for a valid name.
3. Try entering a non-numeric value for drop years or marks and confirm that the program asks again.
4. Enter a negative drop-year count or a value below 0 or above 100 and make sure it is rejected.
5. Test values near the threshold for each rule to check both eligible and ineligible results.
