# We have every employee happiness, and we're scaling
# how many of them are happy
employee_happiness = input()
happiness_improvement_factor = int(input())
# Converting the string of numbers as a list of integers
employee_happiness_as_list_of_integers = list(map(int, employee_happiness.split(' ')))
# Comprehension which multiply each element in list of integers with hapiness factor and add it in new list multi_happy
multiplied_happiness = [(happiness * happiness_improvement_factor) \
                        for happiness in employee_happiness_as_list_of_integers]

average_happiness = sum(multiplied_happiness) / len(multiplied_happiness)
# Comprehension which select only the emplyees with greater than average happiness
happy_employees = [employee for employee in multiplied_happiness if employee >= average_happiness]

if len(happy_employees) >= len(multiplied_happiness) / 2:
    print(f'Score: {len(happy_employees)}/{len(multiplied_happiness)}. Employees are happy!')

else:
    print(f'Score: {len(happy_employees)}/{len(multiplied_happiness)}. Employees are not happy!')
