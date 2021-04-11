from sys import argv
script_name, production, salary_hour, bonus = argv
print('Salary = ', float(production)*float(salary_hour)+float(bonus))