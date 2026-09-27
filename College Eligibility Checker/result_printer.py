def print_results(name, drop_years, marks, results):
    print("\nYour Result is Ready")
    print(f"Name: {name}")
    print("Class passed: 12th")
    print(f"Drop years: {drop_years}")

    print("\nYour marks:")
    for subject, mark in marks.items():
        print(f"{subject}: {mark:g}/100")

    print("\nAll Exams:")

    for option, result in results.items():
        if option == "JEE":
            if drop_years == 0 or drop_years == 1:
                if result:
                    print("JEE: Congrats You are eligible for IITs, NITs")
                else:
                    print("JEE: Not Eligible")
            elif drop_years == 2:
                if result:
                    print("JEE: Congrats You are eligible for NITs")
                else:
                    print("JEE: Not Eligible")
            else:
                print("JEE: Not Eligible")

        elif option == "NEET":
            if result:
                print("NEET UG: Congrats You are Eligible")
            else:
                print("NEET UG: Not Eligible")

        elif option == "State colleges":
            if result:
                print("State Government Colleges: Congrats You are Eligible")
            else:
                print("State Government Colleges: Not Eligible")

        elif option == "VIT":
            if result:
                print("VITEEE: Congrats You are Eligible")
            else:
                print("VITEEE: Not Eligible")

        elif option == "BITS":
            if result:
                print("BITSAT: Congrats You are Eligible")
            else:
                print("BITSAT: Not Eligible")