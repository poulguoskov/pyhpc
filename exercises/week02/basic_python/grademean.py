import sys

grades = [float(g) for g in sys.argv[1:]]
mean = sum(grades) / len(grades)
print(f"{mean} {'Pass' if mean >= 5 else 'Fail'}")