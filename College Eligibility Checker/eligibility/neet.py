def neet(name, marks, drop_years):
    total_marks = sum(
        marks.get(subject, 0)
        for subject in ("Physics", "Chemistry", "Biology")
    )

    return total_marks >= 150 and marks.get("Biology", 0) >= 33
