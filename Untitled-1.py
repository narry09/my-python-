string = "communication"

def find_vov(string):
    vowels =  "aeiouAEIOU"
    return len([c for c in string if c in vowels])

print(find_vov(string))


select max(salary) as second_high
from employee
where salary < (select Max(salary) from employee);

