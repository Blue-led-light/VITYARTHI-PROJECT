def vit(name, marks, drop_years):
    if drop_years > 2:
        return False

    pcm = (
        marks.get("Physics", 0)
        + marks.get("Chemistry", 0)
        + marks.get("Mathematics", 0)
    )

    return pcm >= 180 and marks.get("Mathematics", 0) >= 50