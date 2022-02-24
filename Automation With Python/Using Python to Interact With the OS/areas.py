# import math


# def triangle(base,height):
#     return base*height/2

# def rectangle(base,height):
#     return base*height

# def circle(radius):
#     return math.pi*(radius**2)

# def donut(outside_radious,inside_radius):
#     return circle(outside_radious)-circle(inside_radius)




from http.client import ResponseNotReady
from urllib import response
import requests
import socket
import os

def check_localhost():
   localhost=socket.gethostbyname('localhost')
   return localhost == "127.0.0.1"


def check_connectivity():
   request = requests.get("http://www.google.com")
   response = request.status_code
   return response == 200

print(check_connectivity())
print(check_localhost())

import shutil
import psutil
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage < 75
# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything ok")
      
# Writing to the files
with open("spider.txt","w") as file:
   file.write("And itsy bitsy spider climbed the sprout again")
   

# Iterating through the contents of a file
with open('spider.txt') as file:
   for line in file:
      print(line.strip())
      
print(os.path.getsize("spider.txt"))

file= "spiders.txt"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
       print(os.path.isfile(file))
       print("File not found")
       

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename,"w") as file:
    timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
    time= datetime.date.fromtimestamp(timestamp)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(time))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd
import csv
# Writing to a csv file
hosts=[["workstation.local","192.168.5.25"],["Webserver.cloud","10.2.5.6"]]
with open("hosts.csv",'w') as hosts_csv:
  writer=csv.writer(hosts_csv)
  writer.writerows(hosts)
  
users=[{
  "name": "Sol Mansi" , "username":"solm", "department":"IT Infrastructure"
},{
  "name": "Lio Nelson" , "username":"lion", "department":"User Experience"
},{
  "name": "Charlie Grey" , "username":"greyc", "department":"Development"
}]
 
keys=["name","username","department"]
with open('by_Department.csv','w') as by_department:
  writer= csv.DictWriter(by_department,fieldnames=keys)
  writer.writeheader()
  writer.writerows(users)
  
  

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename,'r') as file:
    # Read the rows of the file into a dictionary
    writer = csv.DictReader(file)
    # Process each item of the dictionary
    for row in writer:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename,'r') as file:
    # Read the rows of the file
    rows = csv.reader(file)
    next(rows)
    # Process each row
    for row in rows:
      name,color,typeflower = row
      # Format the return string for data rows only

      return_string += "a {} {} is {}\n".format(color,name,typeflower)
    return return_string

#Call the function
print(contents_of_file("flowers.csv"))




import csv

def read_employees(csv_file_location):
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
  employee_list = []
  for data in employee_file:
    employee_list.append(data)
  return employee_list

def process_data(employee_list):
  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])
  
  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)
  return department_data

def write_report(dictionary, report_file):
  with open(report_file, "w+") as f:
    for k in sorted(dictionary):
      f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()

employee_list = read_employees('employees.csv')
print(employee_list)

dictionary = process_data(employee_list)
print(dictionary)

write_report(dictionary, 'report.txt')