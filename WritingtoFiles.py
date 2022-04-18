employee_file = open("employees.txt", "a") #keeps appending
employee_file.write("\nJoe - Human Resource")
employee_file.close()

employee_file = open("employees1.txt", "w") #overwrites existing
employee_file.write("\nAsef - The Boss")
employee_file.close()