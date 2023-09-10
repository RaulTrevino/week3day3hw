# Filter out all of the empty strings from the list below

# Output: ['Argentina', 'San Diego', 'Boston', 'New York']

# 1
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]


filtered_places=list(filter(lambda string:True if string not in "  " else False, places))
print(filtered_places)


