# Part 1 - 1 - ask user to enter how many courses finished and store into variable num_of_courses
num_of_courses = int(input("How many courses did you finish? "))

course_marks = []     # Part 1 - 2 - declare empty list course_marks

counter=1             # initial the counter

# Part 1 - 3 - loop to allow enter marks for course based on num_of_courses
while counter <= num_of_courses:     
    # store the marks into course_marks list
    course_marks.append(int(input("Enter your mark for course " f"{counter} : ")))  
    counter +=1   # increment the loop counter

# Part 2 - 1, define and initial the variable total
total = 0   

# Part 1 - 4 - print the items of course_marks list 
for x in course_marks:
    total += x       # Part 2 - 1, calculate the total marks
    print(x) 

# Part 2 - 1, define and inital variable average, calculate and print the average
average = 0
average = float(total / num_of_courses)   
print("Your average for your " f"{num_of_courses} courses is: " f"{average}")

# Part 3 - 1, print the grade based on average
if average >= 90  and average <= 100:
    print("Your grade is A+")
elif average >= 80 and average <=89:
    print("Your grade is B")
elif average >=70 and average <=79:
    print("Your grade is C")
elif average >= 60 and average <=69:
    print("Your grade is D")
elif average < 60:
    print("Your grade is F")
    