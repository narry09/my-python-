string = "communication"

def find_vov(string):
    vowels =  'aeiouAEIOU'
    return len([c for c in string if c in vowels])

print(find_vov(string))