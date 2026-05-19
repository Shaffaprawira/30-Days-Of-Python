pfe = 'Python for Everyone'
cfa = 'Coding for All'

try:
    print(cfa.rfind('i'))
except ValueError:
    print("Character not found")
finally:
    print("Execution completed")

print('You cannot end a sentence with because because because is a conjunction'.find('because'))