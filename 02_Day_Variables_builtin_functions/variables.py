
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

print('Length first name: ' + str(len(first_name)))
print('Length last name: ' + str(len(last_name)))
print('Length Difference between first and last name: ' + str(len(first_name) - len(last_name)))


numOne = 5
numTwo = 4
total = numOne + numTwo
diff = numOne - numTwo
division = numOne / numTwo
modulas = numOne % numTwo
exp = numOne ** numTwo
floor_division = numOne // numTwo

print(str(floor_division))


radius = 30
area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius

radius = input('What is the radius of the cirlce: ')
radius = float(radius)

area_of_circle = 3.14 * radius ** 2
circum_of_circle = 2 * 3.14 * radius

print('Area of the circle: ', area_of_circle)
print('Circumference of the circle: ', circum_of_circle)

