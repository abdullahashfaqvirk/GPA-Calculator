print("--------------------------------------------------------")
print("  Grading Point Average (GPA) Calculator (PUCIT/FCIT)")
print("--------------------------------------------------------")

def letter_grade(per): # per is for percentage
    # This function returns the grades and grade points
    if per >= 85:
        grade = "A"
        point = 4
    elif per >= 80:
        grade = "A-"
        point = 3.70
    elif per >= 75:
        grade = "B+"
        point = 3.30
    elif per >= 70:
        grade = "B"
        point = 3
    elif per >= 65:
        grade = "B-"
        point = 2.70
    elif per >= 61:
        grade = "C+"
        point = 2.30
    elif per >= 58:
        grade = "C"
        point = 2
    elif per >= 55:
        grade = "C-"
        point = 1.70
    elif per >= 50:
        grade = "D"
        point = 1
    else: 
        grade = "F"
        point = 0
    return grade, point


nums = int(input("Enter Total Number of Subjects: "))
print("Enter the Names of the Subject with their Credit Hours")

sub = [] # Subjects
cre = [] # Credit Hours
numb = [] # Obtained Marks

print("--------------------------------------------------------")
name = input("Enter Your Name: ")

for num in range(nums):
    print("--------------------------------------------------------")
    subjects = input("Subject: ")
    credit_hour = float(input("Credit Hour: "))
    number = float(input("Marks Obtained: "))

    sub.append(subjects)
    cre.append(credit_hour)
    numb.append(number)

print("--------------------------------------------------------")

grades_points = [] # Storing grades and grade points in the list
for i in range(len(numb)):
    grade = letter_grade(numb[i])
    grades_points.append(grade)


# GPA Calculating
sum = 0
for i in range(len(cre)):
    mul = cre[i] * grades_points[i][1] # Multipling the credit hours with grade points
    sum = sum + mul

cre_sum = 0
for i in range(len(cre)):
    cre_sum += cre[i]

gpa = sum/cre_sum
print("--------------------------------------------------------")
print(f"Your GPA is {round(gpa,2)}!")
print("--------------------------------------------------------")

# Creating a file 
with open("MyReport.txt","w") as f:
    line = "--------------------------------------------------------"
    f.write(line + "\n")
    f.write("  Grading Point Average (GPA) Calculator (PUCIT/FCIT)\n")
    f.write(line + "\n")
    f.write("Name: " + name + "\n")
    for num in range(nums):
        f.write(line + "\n")
        f.write("Subject: " + sub[num] + "\n")
        f.write("Credit Hour: " + str(cre[num]) + "\n")
        f.write("Obtained Marks: " + str(numb[num]) + "\n")
        f.write("Grade: " + grades_points[num][0] + "\n")

    f.write(line + "\n")
    f.write(f"GPA is {round(gpa,2)}!\n")
    f.write(line)
