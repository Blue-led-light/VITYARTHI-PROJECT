from eligibility.bits import bits
from eligibility.jee import jee
from eligibility.neet import neet
from eligibility.state_colleges import state_colleges
from eligibility.vit import vit
from collect_student_data import collect_student_data
from result_printer import print_results


def main():
    name, drop_years, marks = collect_student_data()
    results = {
        "JEE": jee(name, marks, drop_years),
        "NEET": neet(name, marks, drop_years),
        "State colleges": state_colleges(name, marks, drop_years),
        "VIT": vit(name, marks, drop_years),
        "BITS": bits(name, marks, drop_years),
    }
    print_results(name, drop_years, marks, results)


if __name__ == "__main__":
    main()