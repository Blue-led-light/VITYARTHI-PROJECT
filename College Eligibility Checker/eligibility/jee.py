def jee(name, marks, drop_years):
    if drop_years > 2:
        return False

    subjects = ("Physics", "Chemistry", "Mathematics", "Computer", "English")
    total_marks = sum(marks.get(subject, 0) for subject in subjects)

    return total_marks >= 375
