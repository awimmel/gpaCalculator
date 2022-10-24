# # Basic arithmetic and variable demonstration
# print("5 + 1:")
# print(5 + 1)
# print()
# print()

# # Addition
# print("(5 + 10):")
# x = 5
# x = x + 10
# print(x)
# print()
# print()

# print("(5 += 10):")
# x = 5
# x += 10
# print(x)
# print()
# print()

# # Subtraction
# print("(5 - 2):")
# x = 5
# x = x - 2
# print(x)
# print()
# print()

# print("(5 -= 2):")
# x = 5
# x -= 2
# print(x)
# print()
# print()

# # Multiplication
# print("(10 * 2):")
# x = 10
# x = x * 2
# print(x)
# print()
# print()

# print("(10 *= 2):")
# x = 10
# x *= 2
# print(x)
# print()
# print()

# # Division
# print("(10 / 2):")
# x = 10
# x = x / 2
# print(x)
# print()
# print()

# print("(10 /= 2):")
# x = 10
# x /= 2
# print(x)
# print()
# print()

# # If-else if-else demonstration
# grade = 'C'
# grade = grade.lower()
# score = 100
# print("If control structure:")
# if grade == 'a':
#     score = 4
# elif grade == 'a-':
#     score = 3.7
# elif grade == 'b+':
#     score = 3.3   
# elif grade == 'b':
#     score = 3
# elif grade == 'b-':
#     score = 2.7
# elif grade == 'c+':
#     score = 2.3
# elif grade == 'c':
#     score = 2
# elif grade == 'c-':
#     score = 1.7
# elif grade == 'd+':
#     score = 1.3
# elif grade == 'd':
#     score = 1
# elif grade == 'e':
#     score = 0
# elif grade == 'en':
#     score = 0

# print(score)
# print()
# print()

# # Looping demonstration. For loops, while loops, and lists
# print("For loop:")
# # Note that the for loop starts at 0 and ends at 4
# for i in range(5):
#     print(i)
# print()
# print()

# print("While loop:")
# x = 0
# # Numbers list, will contain each x value that is iterated through
# # List is an ordered data structure that can store numbers, strings, or other objects/data types (including those
# # defined by users!)
# numbers = []
# while x < 5:
#     x += 1
#     numbers.append(x)

# print(numbers)
# print()
# print()

# # Finally, we will iterate through the numbers array that we created. This will be done with a for loop
# print("Numbers for loop:")
# for number in numbers:
#     print(number)

# print()
# print()


# # Prompting the user for their own input and print the results
# number = input("Enter your favorite number: ")
# print(number)
# print()
# print()

# letter = input("Enter your letter grade: ")
# print(letter)
# print()
# print()

# # Creating and calling functions
# def print_basic():
#     print("Basic print function called!")
#     print()
#     print()

# print_basic()

# # Calculating GPA score corresponding to letter grade
# # letter is a parameter determined by the function call
# # The value returned allows the function to be treated as one of the mathematical expressions we saw earlier
# def score_calc(letter):
#     score = 100

#     # Finding the lowercase version of the letter so that the program accepts uppercase and lowercase inputs
#     letter = letter.lower()
#     if letter == 'a':
#         score = 4
#     elif letter == 'a-':
#         score = 3.7
#     elif letter == 'b+':
#         score = 3.3   
#     elif letter == 'b':
#         score = 3
#     elif letter == 'b-':
#         score = 2.7
#     elif letter == 'c+':
#         score = 2.3
#     elif letter == 'c':
#         score = 2
#     elif letter == 'c-':
#         score = 1.7
#     elif letter == 'd+':
#         score = 1.3
#     elif letter == 'd':
#         score = 1
#     elif letter == 'e':
#         score = 0
#     elif letter == 'en':
#         score = 0

#     # This line helps the function actually return a value    
#     return score

# # Now, let's put a few of the last steps together into a cohesive unit
# # First, we should prepare a way to store your grades so they can be called and your GPA can ultimately
# # be calculated
# # Let's combine a while loop with the user input functionality we learned earlier. By storing these inputs
# # in a list, we will be able to calculate your overall GPA
# # A while loop is needed here because we want to constantly check the user's input with the condition
# # If the user presses 'x', we want to escape the while loop and proceed to the rest of the program

# current_grade = input("Enter your first grade: ")
# grades = []
# while current_grade != 'x':
#     # Adding the previous grade to the array, reading in the next grade from the user
#     grades.append(current_grade)
#     current_grade = input("Enter your grade. If you are done entering a grade, enter x: ")

# print()
# print()

# # Next, we should iterate through the grades list and find the number of grade points
# # you have earned.
# # To do this, we should iterate through each element in the list and use our score_calc()
# # function from earlier
# overall_score = 0
# for grade in grades:
#     overall_score += score_calc(grade)

# # Finally, to receive your overall GPA, we will divide by your number of graded courses

# # len() finds the length of a list
# num_courses = len(grades)
# gpa = overall_score/num_courses

# # This demonstrates how to print a number along with a string to the console
# print("GPA: " + str(gpa))
# print()
# print()