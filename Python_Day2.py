# Exercise 2 

# Using list comprehension, create a list of names of 4 letters or more and capitalize each name

names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']

capitalized_words = []

for name in names1:
    if len(name ) >= 4:
        capitalized_words.append(name.capitalize())

print(capitalized_words)



# Exercise 1 

# Create a list of numbers that are less than ten using l_1 and list comprehension


# Your output should [1,5,8,9]

# Use the following list - [1,11,14,5,8,9]

l_1 = [1,11,14,5,8,9]


new_nums = [x for x in l_1 if x < 10]

print(new_nums)