College Eligibility Checker

Summary

This is a college's entrance rules, eligibility, small, class. After requesting the student's name, number of drop years, and major subject grades, the computer compares these to sample requirements for JEE, NEET UG, state government colleges, VITEEE, and BITSAT.

Features
- Rejects blank input while accepting a student's name
- Takes a non-negative number of drop years
Verifies scores in Physics, Chemistry, Mathematics, Biology, Computer Science, and English ranging from 0 to 100.
- Re-prompts the user if any value is invalid
Verifies eligibility using five distinct categories.
A final summary containing the student's information and outcomes is displayed.

Sample Rules

The project currently uses these example rules:
- **JEE:** Total of Physics, Chemistry, Mathematics, Computer, and English must be at least 375, and the student must have no more than two drop years. The result also distinguishes between zero/one drop year and two drop years.
- **NEET UG:** Total of Physics, Chemistry, and Biology must be at least 150, with at least 33 in Biology.
- **State government colleges:** Total of Physics, Chemistry, Mathematics, and Biology must be at least 180, with no more than three drop years.
- **VITEEE:** Total of Physics, Chemistry, and Mathematics must be at least 180, with at least 50 in Mathematics and no more than two drop years.
- **BITSAT:** Total of Physics, Chemistry, and Mathematics must be at least 225, with at least 60 in each subject and no more than one drop year.

 Technologies
 
- Python 3
- Standard library only; no external packages required

 Project Structure

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


 Installation and Run

1. Install Python 3 if it is not already installed.
2. Clone or download this repository and open a terminal in the project folder.
3. Run:
    python main.py
4. Enter your name, drop years, and marks when prompted.


 Testing

1. Run `python main.py` and give a legitimate name, `0` drop years and marks like `80` for all the subjects. Name: John Doe Marks: 80, 90, 75, 88, 92, 78 Eligibility Results: 1. Passed 2. Eligible for further education 3. Awarded distinction in Mathematics 4. Not eligible for scholarship 5. Recommended for advanced program
2. Run it again, this time with a blank name, and check that the application prompts for a legitimate name.
3. Enter a non-numeric figure for drop years or marks and ensure that the program prompts again.
4. Enter a negative drop year number or a number below 0 or above 100 and verify it is refused.
5. For each rule, test values near the threshold to validate results for both ineligible and eligible cases.

Screenshot

<img width="346" height="379" alt="Screenshot 2026-09-27 195317" src="https://github.com/user-attachments/assets/3f520185-5b93-439b-823b-b18d5ceb8765" />

