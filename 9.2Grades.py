# 9.2 with read from grades.txt
#Class average program with sentinel-controlled iteration.
# initialization phase
#Open file in read mode
with open('grades.txt','r') as file:
    lines = file.readlines()

total = 0  # sum of grades
grade_counter = 0 # number of grades entered

# processing phase
for line in lines:
    grade = int(line.strip())
    print(grade)
    total += grade
    grade_counter += 1

#print total,count,average
print(f'\nTotal: {total}')
print(f'Count: {grade_counter}')
if grade_counter > 0:
    average = total / grade_counter
    print(f'Average: {average:.2f}')
else:
    print('No grades found in the file')