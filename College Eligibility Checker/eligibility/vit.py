def vit(name, marks, drop_years):
    if drop_years > 2:
        return False

    pcm_marks = sum(
        marks.get(subject, 0)
        for subject in ("Physics", "Chemistry", "Mathematics")
    )

    return pcm_marks >= 180 and marks.get("Mathematics", 0) >= 50
