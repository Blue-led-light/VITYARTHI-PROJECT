def state_colleges(name, marks, drop_years):
    if drop_years > 3:
        return False

    subjects = ["Physics", "Chemistry", "Mathematics", "Biology"]
    total = sum(marks.get(subject, 0) for subject in subjects)

    return total >= 180