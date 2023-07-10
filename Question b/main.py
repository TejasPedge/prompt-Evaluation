
employees = [
    {"name": "John", "salary": 3000, "designation": "developer"},
    {"name": "Emma", "salary": 4000, "designation": "manager"},
    {"name": "Kelly", "salary": 3500, "designation": "tester"},
]


def max_salary_employee(employees_data) :
    
    maxSalary = max(employees_data, key = lambda emp: emp['salary']);

    return maxSalary

result = max_salary_employee(employees);

print(result);