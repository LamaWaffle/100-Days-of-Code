states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Kentucky", "California"]
states = states_of_america

# Specifies the indexed item listed, then changes its name.
states[0] = "Delawho??"

# Prints the indexed item from the list.
print(states[0])
print(states[-2]) # Will go backwards.

states.append("LamaLand")
states.extend(["New Landtown"])

# List data type and dictionary data type, notice the {} brackets
student_grades_list = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
student_grades_dict = {"Marry": 8.2, "John":4.2, "Stacey":5.9}

# Will add the list together.
mysum = sum(student_grades_list)
print(mysum)

length = len(student_grades_dict)
mean = mysum / length
print(mean)

max_grades = max(student_grades_list)
print(max_grades)

print(student_grades_list.count(10.0))

username = "Python3"
print(username.lower())

print(student_grades_dict.keys())