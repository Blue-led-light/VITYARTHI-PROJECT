def state_colleges(name, marks, drop_years):
    if drop_years > 3:
        return False

    subjects = ("Physics", "Chemistry", "Mathematics", "Biology")
    total_marks = sum(marks.get(subject, 0) for subject in subjects)

    return total_marks >= 180
