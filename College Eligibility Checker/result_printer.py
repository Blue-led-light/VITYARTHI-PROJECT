def print_results(name, drop_years, marks, results):
    print("\nYour result is ready!")
    print(f"Name: {name}")
    print("Class: 12th")
    print(f"Drop years: {drop_years}")

    print("\nYour marks:")
    for subject, mark in marks.items():
        print(f"{subject}: {mark:g}/100")

    print("\nEligibility check:")

    for exam, eligible in results.items():
        message = get_result_message(exam, eligible, drop_years)
        print(message)


def get_result_message(exam, eligible, drop_years):
    if exam == "JEE":
        if drop_years in (0, 1) and eligible:
            return "JEE: Great news! You are eligible for IITs and NITs."
        if drop_years == 2 and eligible:
            return "JEE: Nice! You are eligible for NITs."
        return "JEE: Not eligible this time."

    exam_display_names = {
        "NEET": "NEET UG",
        "State colleges": "State Government Colleges",
        "VIT": "VITEEE",
        "BITS": "BITSAT",
    }

    exam_name = exam_display_names.get(exam, exam)
    eligibility_message = "You are eligible!" if eligible else "Not eligible."

    return f"{exam_name}: {eligibility_message}"

