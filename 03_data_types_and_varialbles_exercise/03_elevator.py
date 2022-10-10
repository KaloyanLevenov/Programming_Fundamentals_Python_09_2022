number_of_people = int(input())
capacity = int(input())
courses = 0
while number_of_people > 0:
    courses += 1
    number_of_people -= capacity
print(courses)
