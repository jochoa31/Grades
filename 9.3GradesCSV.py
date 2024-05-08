import csv

# Open the CSV file for writing with file named grades.csv
with open('grades.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)
    
    # Prompt the user to enter student information
    while True:
        firstname = input("Enter student's first name (or 'q' to quit): ")
        if firstname.lower() == 'q':
            break
        lastname = input ("Enter student's last name:")
        exam1 = int(input("Enter exam 1 grade: "))
        exam2 = int(input("Enter exam 2 grade: "))
        exam3 = int(input("Enter exam 3 grade: "))
        
        # Write the student record to the CSV file
        writer.writerow([firstname, lastname, exam1, exam2, exam3])
        
        print("Student record saved to grades.csv.")
        print()