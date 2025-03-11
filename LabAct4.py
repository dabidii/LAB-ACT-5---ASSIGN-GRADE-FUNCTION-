assign_grade = int(input("What’s your grade? Enter a score (0-100): "))

if assign_grade > 100:
    print(f"{assign_grade}? That’s over 100. Try again with a score between 0 and 100.")
elif assign_grade >= 90:
    print(f"{assign_grade} gets you an A. Nice work, keep it up!!.")
elif assign_grade >= 80:
    print(f"{assign_grade} is a B. Solid effort you did well:).")
elif assign_grade >= 70:
    print(f"{assign_grade} means a C. Try a bit more, i know you can do it!!.")
elif assign_grade >= 60:
    print(f"{assign_grade} is a D. Maybe take a breathe and do better again?Fight more!!.")
elif assign_grade >= 0:
    print(f"{assign_grade} is an F. Rough one. Need help studying?")
else:
    print(f"{assign_grade}? Negative scores don’t work. Use 0 to 100.")
