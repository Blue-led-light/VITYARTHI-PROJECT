def read_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter {subject} marks out of 100: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if 0 <= mark <= 100:
            return mark

        print("Marks must be between 0 and 100.")