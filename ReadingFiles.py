employee_file = open("employees.txt", "r") # read
#open("employees.txt", "w") #write
#open("employees.txt", "a") # append at the end, not read/write the existing
#open("employees.txt", "r+") # reading and writing
print(employee_file.readable()) # true
print(employee_file.read()) # outputs the whole content
print(employee_file.readline()) #outputs first line
print(employee_file.readline()) #outputs second line
#print(employee_file.readlines()) #outputs in a list
print(employee_file.readlines()[0]) #outputs in a list
#parse through a file
'''for employee in employee_file.readlines():
    print(employee)
employee_file.close()
'''