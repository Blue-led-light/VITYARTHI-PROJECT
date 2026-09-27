def neet(name, marks, drop_years):
    subjects = ["Physics", "Chemistry", "Biology"]
    total = sum(marks.get(subject, 0) for subject in subjects)
    biology = marks.get("Biology", 0)

    return total >= 150 and biology >= 33