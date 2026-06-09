#question 1
student_records={'ram':'ram@gmail.com',
                  'shyam':'shyam1232@gmail.com'}
name=input('enter username:')
print(student_records.get(name,'not found'))

student_records={'ram':'ram@gmail.com',
                  'shyam':'shyam1232@gmail.com'}
name=input('enter username:')
if name in student_records:
    print(student_records[name])
else:
   print('contactnot found')

   #question 2 

   shopping_list={'milk''orange'}
bought={'milk'}
unbought_items=shopping_list.difference(bought)
print(unbought_items)
if not unbought_items:
  print('shopping complete')
else:
  print(f'brough items: {unbought_items}')  

  #question 3


#question 4

votes = ["Blue", "Red", "Blue", "Green", "Blue"]

blue_count = votes.count("Blue")
if blue_count >= 3:
    print("Blue wins")
else:
    print("Blue did not win")


#question 5    

grades = {"Ram": 92, "Sita": 88}
student_name = "Ram"
if student_name in grades:
    print(grades[student_name])
else:
    print("Grade is not available")


#question 6

applicant = {"name": "Priya", "skills": ["Java", "SQL"], "experience_years": 1}
required_skills = {"Python", "Java"}

has_skill = any(skill in required_skills for skill in applicant["skills"])
has_experience = applicant["experience_years"] >= 2

if has_skill and has_experience:
    print("priya qualifies")
else:
    print("priya does not qualify")


    #question 7


banned_items = {"scissors", "knife", "lighter"}
weight = float(input())
item = input().lower()

if weight <= 7 and item not in banned_items:
    print("Bag allowed")
else:
    print("Bag not allowed")

    #question 8

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Shyam', 'salary': 500}
}
sample_dict['emp3']['salary'] = 8500


#question 9

ram_items = {"apple", "banana", "orange"}
laxman_items = {"grapes", "mango"}

if ram_items.isdisjoint(laxman_items):
    print("they picked completely different items")
else:
    print("they have some common items")


    #question 10

    my_list = [10, 20, 30]
my_tuple = (10, 20, 30)
my_set = {10, 30}          
my_dict = {'b': 20}        

val = 20

if val in my_list and val in my_tuple:
    if 'b' in my_dict and val not in my_set:
        print('Path A')
    else:
        print('Path B')
else:
    print('Path C')


#question 11
#The value for a becomes 30.

#question 12
#= [1,2,3]

#question 13
# not found 

#question 14
# 2

#question 15
# my_set.add(40)

#question 16

menu = {"Pizza": 15, "Burger": 10, "Salad": 8}
order = 'Pizza'

if order in menu:
    print(menu[order])
else:
    print("item not found")


    #question 17

    student_data = {"name": "Sam", "score": 85}

if student_data["score"] >= 80:
    student_data["status"] = "Pass"
else:
    student_data["status"] = "Review"

print(student_data)


#question 18

database = {"admin": "1234", "user": "abcd"}
user_input = 'admin'
user_pass = '1234'

if user_input in database and database[user_input] == user_pass:
    print("Login Successful")
else:
    print("Login Failed")


    #question 19

    emails = ['ram123@gmail.com', 'hari77@gmail.com']
blacklisted_emails = {'hari77@gmail.com'}
current_email = 'hari77@test.com'

if current_email in emails and current_email not in blacklisted_emails:
    print("Email Sent")
else:
    print("Blocked")

    #question 20

    inventory = {'A1': 50, 'B2': 0, 'C3': 10}
restricted_zones = {'B2', 'Z9'}
target = 'B2'

if target in inventory:
    if target not in restricted_zones and inventory[target] > 0:
        print("dispatch item")
    else:
        print("stock error")
else:
    print("invalid zone")


    #question 21

    valid_courses = {"python", "robotics", "java"}
hs_grades = [9, 10, 11, 12]

name = input()
course = input()
grade = int(input())

student_records = {
    "name": name,
    "course": course,
    "grade": grade
}

if student_records["course"] not in valid_courses:
    print(f"{student_records['name']} selected an invalid course.")
else:
    if student_records["grade"] < 9:
        print("grade too low")
    elif student_records["grade"] > 12:
        print("grade too high")
    else:
        if student_records["course"] == "robotics" and student_records["grade"] == 9:
            print(f"{student_records['name']} is not eligible for {student_records['course']} grade too low")
        else:
            print(f"{student_records['name']} is approved for {student_records['course']}")