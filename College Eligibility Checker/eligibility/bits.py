def bits(name, marks, drop_years):
    if drop_years > 1:
        return False

    subjects = ["Physics", "Chemistry", "Mathematics"]
    pcm = sum(marks.get(subject, 0) for subject in subjects)

    return (
        pcm >= 225
        and marks.get("Physics", 0) >= 60
        and marks.get("Chemistry", 0) >= 60
        and marks.get("Mathematics", 0) >= 60
    )