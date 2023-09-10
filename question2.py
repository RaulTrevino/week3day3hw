# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"

# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']


author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
sorted_lname= sorted(author, key=lambda x: x.split()[-1].lower())
#sorted puts name in abc order. x.split selects last name  with -1 and converts to lower case
print(sorted_lname)