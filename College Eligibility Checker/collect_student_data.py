from read_mark import read_mark


def collect_student_data():
    print("Enter your name:", flush=True)
    name = input().strip()

    while not name:
        print("Name cannot be empty.")
        name = input().strip()

    while True:
        try:
            drop_years = int(
                input("Enter number of drop years (if none, type 0): ")
            )

            if drop_years >= 0:
                break

            print("Drop years cannot be negative.")

        except ValueError:
            print("Please enter a valid number.")

    marks = {}
    for subject in [
        "Physics",
        "Chemistry",
        "Mathematics",
        "Biology",
        "Computer",
        "English",
    ]:
        marks[subject] = read_mark(subject)

    return name, drop_years, marks