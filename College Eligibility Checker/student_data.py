from read_mark import read_mark


SUBJECTS = (
    "Physics",
    "Chemistry",
    "Mathematics",
    "Biology",
    "Computer",
    "English",
)


def student_data():
    name = input("Enter your name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()

    while True:
        try:
            drop = int(input("Enter number of drop years (if none, type 0): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if drop < 0:
            print("Drop years cannot be negative.")
            continue

        break

    marks = {}
    for subject in SUBJECTS:
        marks[subject] = read_mark(subject)

    return name, drop, marks
