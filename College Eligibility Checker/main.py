from student_data import student_data

from eligibility.bits import bits
from eligibility.jee import jee
from eligibility.neet import neet
from eligibility.state_colleges import state_colleges
from eligibility.vit import vit
from result_printer import print_results


name, drop_years, marks = student_data()

results = {}

results["JEE"] = jee(name, marks, drop_years)
results["NEET"] = neet(name, marks, drop_years)
results["State colleges"] = state_colleges(name, marks, drop_years)
results["VIT"] = vit(name, marks, drop_years)
results["BITS"] = bits(name, marks, drop_years)

print_results(name, drop_years, marks, results)