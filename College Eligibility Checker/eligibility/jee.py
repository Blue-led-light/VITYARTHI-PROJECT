def jee(name, marks, drop_years):
    subjects = ["Physics", "Chemistry", "Mathematics", "Computer", "English"]
    total = sum(marks.get(subject, 0) for subject in subjects)

    if drop_years > 2:
        return False

    return total >= 375